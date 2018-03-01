import boto3
from masonite.contracts.UploadContract import UploadContract
from masonite.drivers.BaseUploadDriver import BaseUploadDriver


class UploadS3Driver(BaseUploadDriver, UploadContract):
    """
    Amazon S3 Upload driver
    """

    def __init__(self, Upload, StorageConfig):
        self.upload = Upload
        self.config = StorageConfig

    def store(self, fileitem, location=None):
        file_location = self.upload.driver('disk').store(fileitem)

        # Check if is a valid extension
        self.validate_extension(fileitem.filename)

        session = boto3.Session(
            aws_access_key_id=self.config.DRIVERS['s3']['client'],
            aws_secret_access_key=self.config.DRIVERS['s3']['secret'],
        )

        s3 = session.resource('s3')

        s3.meta.client.upload_file(
            file_location,
            self.config.DRIVERS['s3']['bucket'],
            fileitem.filename
        )

    def store_prepend(self, fileitem, prepend, location=None):
        fileitem.filename = prepend + fileitem.filename

        return self.store(self, fileitem, location)
