import aspose.words as aw
import os
from django.conf import settings
from io import BytesIO


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
        input_title = os.path.splitext(self.input_file.name)[0]
        doc = aw.Document(self.get_full_file_path())
        output_path = os.path.join(self.save_path(), input_title + '.pdf')
        doc.save(output_path)
        output_file_rel_path = os.path.relpath(output_path, settings.MEDIA_ROOT)
        return output_file_rel_path

        #Documentation here : https://pypi.org/project/aspose-words/

