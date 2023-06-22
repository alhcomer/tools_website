from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from ..models import FileConversion
from ..converter import FileConverter
from ..views import file_converter
from django.contrib.auth import get_user_model

class FileConverterViewTest(TestCase):
    def setUp(self):
        # Create user object and testing input file
        User = get_user_model()
        self.user = User.objects.create_user(email="testuser", password="testpass")
        self.input_file = SimpleUploadedFile("test_file.txt", b"file_content", content_type="text/plain")

# https://chat.openai.com/share/8bacd22a-b9bc-4d8d-9f80-f8407754dfd5
# Above chat for help with testing