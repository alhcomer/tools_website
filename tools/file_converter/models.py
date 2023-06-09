import os
import uuid
from django.db import models
from .validators import FileValidator
from django.conf import settings
from .mystorage import CleanFileNameStorage


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


def get_unique_filename(instance, filename):
    # Generate a unique filename for the output file
    ext = os.path.splitext(filename)[1]
    unique_filename = f'{uuid.uuid4()}{ext}'
    return os.path.join(user_directory_path(instance, unique_filename))


allowed_extensions = [
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    "text/html",
    "application/vnd.oasis.opendocument.text",
    "application/pdf",
    "application/vnd.ms-powerpoint",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    "application/rtf",
    "text/plain",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "application/pdf"
]

validator = FileValidator(max_size=100000000, min_size=100, content_types=allowed_extensions)


class FileConversion(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user")
    input_file = models.FileField(upload_to=user_directory_path, validators=[validator,], storage=CleanFileNameStorage(), unique=True)
    output_file = models.FileField(upload_to=get_unique_filename)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_split_input(self):
        # TODO: Fix str representation of file path shown to user on FileConversion objects
        pass

    def get_split_output(self):
        pass


#TODO: configure user specific upload areas
# Maybe use https://stackoverflow.com/questions/34239877/django-save-user-uploads-in-seperate-folders