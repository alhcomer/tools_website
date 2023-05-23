import aspose.words as aw
import os
from django.conf import settings
from io import BytesIO
from .models import FileConversion
import uuid


class FileConverter:
    def __init__(self, input_file, request):
        self.input_file = input_file
        self.user = request.user
        self.output_file = self.convert_file()

    def get_full_file_path(self):
        # TODO: Check whether multiple chunks is appropriate given file validation sizes
        if self.input_file.multiple_chunks():
            raise ValueError("File is too large to be converted.")
        else:
            file_bytes = self.input_file.read()
            return BytesIO(file_bytes)

    def save_path(self):
        return os.path.join(settings.MEDIA_ROOT, f'user_{self.user.id}')

    def convert_file(self):
        input_filename, input_extension = os.path.splitext(self.input_file.name)
        output_filename = f'{input_filename}.pdf'  # Output file will have the same name as the input file, but with .pdf extension

        if FileConversion.objects.filter(user=self.user, input_file__contains=input_filename).exists():
            # If a FileConversion object with a similar input filename exists for the same user
            unique_filename = str(uuid.uuid4()) + '_' + output_filename
            output_filename = unique_filename

        output_path = os.path.join(self.save_path(), output_filename)

        doc = aw.Document(self.get_full_file_path())
        doc.save(output_path)

        output_file_rel_path = os.path.relpath(output_path, settings.MEDIA_ROOT)
        return output_file_rel_path
        #Documentation here : https://pypi.org/project/aspose-words/

