import os
from logger_service import get_custom_logger

putlog = get_custom_logger(__name__)


def format_upload_names(instance, filename) -> str:
    """
    Use to rename the file before upload and construct the full path
    :param instance: An instance of the class
    :param filename: file name of the uploaded file
    :return: A string of path.
    """
    putlog.debug('Image Upload request received, formatting name before upload.')

    old_name, ext = os.path.splitext(filename)

    new_name = f"{instance.name}{ext}"  # Create new name using model fields. Ex: instance.name

    location = 'images'  # The location inside the media root folder

    final_path = os.path.join(location, new_name)

    putlog.info(f'Old Name: "{filename}", Formatted Name: "{new_name}"')
    putlog.debug(f'Full path for Image : {final_path}')
    return final_path
