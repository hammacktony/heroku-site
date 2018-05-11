import time
import glob

from config import cache
from masonite.app import App
from masonite.drivers.CacheDiskDriver import CacheDiskDriver
from masonite.managers.CacheManager import CacheManager
from masonite.view import view, View
from masonite.exceptions import RequiredContainerBindingNotFound
import pytest


class TestView:

    def setup_method(self):
        self.container = App()
        view = View(self.container)

        self.container.bind('View', view.render)
        self.container.bind('ViewClass', view)

    def test_view_compiles_jinja(self):
        assert view('test', {'test': 'test'}) == 'test'

    def test_view_extends_dictionary(self):
        view = self.container.make('View')

        assert view('test', {'test': 'test'}).rendered_template == 'test'

    def test_view_gets_global_template(self):
        view = self.container.make('View')

        assert view('/storage/test', {'test': 'test'}).rendered_template == 'test'
        assert view('/storage/static/test', {'test': 'test'}).rendered_template == 'test'

    def test_view_extends_without_dictionary_parameters(self):
        view = self.container.make('ViewClass')
        view.share({'test': 'test'})
        view = self.container.make('View')

        assert view('test').rendered_template == 'test'

    def test_render_from_container_as_view_class(self):
        self.container.make('ViewClass').share({'test': 'test'})

        view = self.container.make('View')
        assert view('test').rendered_template == 'test'

    def test_composers(self):
        self.container.make('ViewClass').composer('test', {'test': 'test'})
        view = self.container.make('View')

        assert self.container.make('ViewClass').composers == {'test': {'test': 'test'}}
        assert view('test').rendered_template == 'test'

    def test_composers_load_all_views_with_astericks(self):

        self.container.make('ViewClass').composer('*', {'test': 'test'})

        assert self.container.make('ViewClass').composers == {'*': {'test': 'test'}}

        view = self.container.make('View')
        assert view('test').rendered_template == 'test'

    def test_composers_with_wildcard_base_view(self):
        self.container.make('ViewClass').composer('mail*', {'to': 'test_user'})

        assert self.container.make('ViewClass').composers == {'mail*': {'to': 'test_user'}}

        view = self.container.make('View')
        assert 'test_user' in view('mail/welcome').rendered_template

    def test_composers_with_wildcard_lower_directory_view(self):
        self.container.make('ViewClass').composer('mail/welcome*', {'to': 'test_user'})

        assert self.container.make('ViewClass').composers == {'mail/welcome*': {'to': 'test_user'}}

        view = self.container.make('View')
        assert 'test_user' in view('mail/welcome').rendered_template
    
    def test_composers_with_wildcard_lower_directory_view_and_incorrect_shortend_wildcard(self):
        self.container.make('ViewClass').composer('mail/wel*', {'to': 'test_user'})

        assert self.container.make('ViewClass').composers == {'mail/wel*': {'to': 'test_user'}}

        view = self.container.make('View')
        assert 'test_user' not in view('mail/welcome').rendered_template

    def test_composers_load_all_views_with_list(self):
        self.container.make('ViewClass').composer(['home', 'test'], {'test': 'test'})

        assert self.container.make('ViewClass').composers == {
            'home': {'test': 'test'}, 'test': {'test': 'test'}}

        view = self.container.make('View')
        assert view('test').rendered_template == 'test'

    def test_view_share_updates_dictionary_not_overwrite(self):
        viewclass = self.container.make('ViewClass')

        viewclass.share({'test1': 'test1'})
        viewclass.share({'test2': 'test2'})

        assert viewclass.dictionary == {'test1': 'test1', 'test2': 'test2'}

    def test_view_throws_exception_without_cache_binding(self):
        view = self.container.make('View')

        with pytest.raises(RequiredContainerBindingNotFound):
            view('test_cache').cache_for('5', 'seconds')

    def test_view_cache_caches_files(self):

        self.container.bind('CacheConfig', cache)
        self.container.bind('CacheDiskDriver', CacheDiskDriver)
        self.container.bind('CacheManager', CacheManager(self.container))
        self.container.bind('Application', self.container)
        self.container.bind('Cache', self.container.make('CacheManager').driver('disk'))

        view = self.container.make('View')

        assert view(
            'test_cache', {'test': 'test'}
        ).cache_for(1, 'second').rendered_template == 'test'

        assert open(glob.glob('bootstrap/cache/test_cache:*')[0]).read() == 'test'

        time.sleep(2)

        assert view(
            'test_cache', {'test': 'macho'}
        ).cache_for(5, 'seconds').rendered_template == 'macho'

        time.sleep(2)

        assert open(glob.glob('bootstrap/cache/test_cache:*')[0]).read() == 'macho'

        assert view(
            'test_cache', {'test': 'macho'}
        ).cache_for(1, 'second').rendered_template == 'macho'

        time.sleep(1)

        assert open(glob.glob('bootstrap/cache/test_cache:*')[0]).read() == 'macho'

        assert view(
            'test_cache', {'test': 'macho'}
        ).cache_for('1', 'second').rendered_template == 'macho'

    def test_cache_throws_exception_with_incorrect_cache_type(self):
        self.container.bind('CacheConfig', cache)
        self.container.bind('CacheDiskDriver', CacheDiskDriver)
        self.container.bind('CacheManager', CacheManager(self.container))
        self.container.bind('Application', self.container)
        self.container.bind('Cache', self.container.make('CacheManager').driver('disk'))

        view = self.container.make('View')

        with pytest.raises(ValueError):
            view(
                'test_exception', {'test': 'test'}
            ).cache_for(1, 'monthss')
