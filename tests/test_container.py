from masonite.app import App
from masonite.request import Request
from masonite.drivers.UploadDiskDriver import UploadDiskDriver
from masonite.contracts.UploadContract import UploadContract
from masonite.exceptions import ContainerError
import pytest


class MockObject:
    pass

class GetObject(MockObject):
    
    def find(self):
        return 1

class GetAnotherObject(MockObject):

    def find(self):
        return 2

class TestContainer:

    def setup_method(self):
        self.app = App()
        self.app.bind('Request', Request(None))
        self.app.bind('MockObject', MockObject)
        self.app.bind('GetObject', GetObject)

    def test_container_gets_direct_class(self):
        assert isinstance(self.app.make('Request'), Request)

    def test_container_resolves_object(self):
        assert isinstance(self.app.resolve(self._function_test), MockObject.__class__)

    def _function_test(self, MockObject):
        return MockObject

    def test_container_resolving_annotation(self):
        assert isinstance(self.app.resolve(self._function_test_annotation), MockObject.__class__)

    def _function_test_annotation(self, mock: MockObject):
        return mock

    def test_container_resolving_instance_of_object(self):
        assert isinstance(self.app.resolve(self._function_test_annotation), GetObject.__class__)
    
    def test_container_resolving_similiar_objects(self):
        self.app.bind('GetAnotherObject', GetAnotherObject)

        obj = self.app.resolve(self._function_test_find_method_on_similiar_objects)
        assert obj[0] == 2
        assert obj[1] == 1
    
    def _function_test_find_method_on_similiar_objects(self, user: GetAnotherObject, country: GetObject):
        return [user().find(), country().find()]

    def test_raises_error_when_getting_instances_of_classes(self):
        with pytest.raises(ContainerError):
            assert self.app.resolve(self._function_test_find_method_on_similiar_objects)

    def _function_test_double_annotations(self, mock: MockObject, request: Request):
        return {'mock': MockObject, 'request': Request}
    
    def test_container_resolving_multiple_annotations(self):
        assert isinstance(self.app.resolve(self._function_test_double_annotations)['mock'], MockObject.__class__)
        assert isinstance(self.app.resolve(self._function_test_double_annotations)['request'], Request.__class__)

    def test_container_contract_returns_upload_disk_driver(self):
        self.app.bind('UploadDiskDriver', UploadDiskDriver)
        assert isinstance(self.app.resolve(self._function_test_contracts), UploadDiskDriver.__class__)
    
    def _function_test_contracts(self, upload: UploadContract):
        return upload

    def _function_test_contract_and_annotations(self, UploadDiskDriver, request: Request, MockObject):
        return MockObject

    def test_container_injects_dependencies_in_any_order(self):
        self.app.bind('UploadDiskDriver', UploadDiskDriver)
        assert isinstance(self.app.resolve(self._function_test_contract_and_annotations), MockObject.__class__)

    def _function_not_in_container(self, NotIn):
        return NotIn

    def test_container_raises_value_error(self):
        with pytest.raises(ContainerError):
            assert self.app.resolve(self._function_not_in_container)

    def test_container_collects_correct_objects(self):
        self.app.bind('ExceptionHook', object)
        self.app.bind('SentryExceptionHook', object)
        self.app.bind('ExceptionHandler', object)
        
        assert self.app.collect('*ExceptionHook') == {'ExceptionHook': object, 'SentryExceptionHook': object}
        assert self.app.collect('Exception*') == {'ExceptionHook': object, 'ExceptionHandler': object}
        assert self.app.collect('Sentry*Hook') == {'SentryExceptionHook': object}
        with pytest.raises(AttributeError):
            self.app.collect('Sentry')
    
    def test_container_collects_correct_subclasses_of_objects(self):
        self.app.bind('GetAnotherObject', GetAnotherObject)
        objects = self.app.collect(MockObject)
        
        assert 'GetAnotherObject' in objects
        assert 'GetObject' in objects
