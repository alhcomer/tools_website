import aspose.words as aw
import os
from django.conf import settings


class FileConverter:
    def __init__(self, input_file, request):
        self.input_file = input_file
        self.user = request.user
        self.output_file = self.convert_file()

    def get_full_file_path(self):
        return settings.MEDIA_ROOT + f"user_{self.user.id}/{self.input_file.name}"

    def save_path(self):
        return settings.MEDIA_ROOT + f"user_{self.user.id}/"

    def convert_file(self):
        input_title = os.path.splitext(self.input_file.name)[0]
        doc = aw.Document(self.get_full_file_path())
        output_path = self.save_path() + input_title + ".pdf"
        #TODO: fix convert file so that it can convert to any extension
        doc.save(output_path)
        return output_path

        #Documentation here : https://pypi.org/project/aspose-words/

