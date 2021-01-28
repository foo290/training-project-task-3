from django.db import models
from logger_service import get_custom_logger
from .file_upload_utils import format_upload_names

putlog = get_custom_logger(__name__)


class UploadImage(models.Model):
    # Fields :
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to=format_upload_names)

    def __str__(self):
        return self.name
