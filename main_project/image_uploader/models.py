import os
from django.db import models
from logger_service import get_custom_logger

putlog = get_custom_logger(__name__)


# Create your models here.


class UploadImage(models.Model):

    # Fields :
    name = models.CharField(max_length=20)

    # The third argument can be the field you want to use as name of the file, In this case it is : obj.name
    image = models.ImageField(upload_to=lambda obj, f_name: UploadImage.format_upload_names(obj, f_name, obj.name))

    @classmethod
    def format_upload_names(cls, instance, filename, format_by) -> str:
        """
        Use to rename the file before upload and construct the full path
        :param instance: An instance of the class
        :param filename: file name of the uploaded file
        :param format_by: A field which will be used to rename the file
        :return: A string of path.
        """
        putlog.debug('Image Upload request received, formatting name before upload.')

        old_name, ext = os.path.splitext(filename)
        new_name = f"{format_by}{ext}"

        location = 'images'  # The location inside the media root folder

        final_path = os.path.join(location, new_name)

        putlog.info(f'Old Name: "{filename}", Formatted Name: "{final_path}"')
        return final_path

    def __str__(self):
        return self.name
