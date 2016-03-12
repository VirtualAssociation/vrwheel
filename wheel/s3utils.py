from storages.backends.s3boto import S3BotoStorage
from django.contrib.staticfiles.storage import CachedFilesMixin


class OptimizedS3BotoStorage(CachedFilesMixin, S3BotoStorage):
    location = 'static'


class MediaS3BotoStorage(S3BotoStorage):
    location = 'media'