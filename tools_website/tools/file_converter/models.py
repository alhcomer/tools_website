from django.db import models

from django.conf import settings

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class FileConverter(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="file_conversions")
    input_file = models.FileField(upload_to=user_directory_path)
    output_file = models.FileField(upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)


#TODO: configure user specific upload areas
# Maybe use https://stackoverflow.com/questions/34239877/django-save-user-uploads-in-seperate-folders