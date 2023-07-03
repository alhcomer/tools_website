from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
from ..models import FileConversion
from ..converter import FileConverter
from ..views import file_converter
from django.contrib.auth import get_user_model

class FileConversionModelTest(TestCase):
    def setUp(self):
        # Create user object and testing input file
        User = get_user_model()
        self.user = User.objects.create_user(email="testuser", password="testpass")
        self.input_file = SimpleUploadedFile("test_file.txt", b"file_content", content_type="text/plain")

    def test_file_conversion(self):
        # Create FileConversion object and simulate file conversion
        file_conversion = FileConversion.objects.create(user=self.user, input_file=self.input_file)
        converter = FileConverter(file_conversion.input_file, self.user, '.pdf')
        converted_file = converter.convert_file()

        # Check FileConversion converted file and FileConverter converted file are the same
        self.assertEqual(file_conversion.output_file.name, converted_file)

        # Check FileConversion output file is saved properly
        self.assertTrue(FileConversion.objects.filter(output_file=converted_file).exists())


        


    