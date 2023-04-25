import aspose.words as aw
from pathlib import Path

class FileConverter:
    def __init__(self, input_file):
        self.input_file = input_file
        self.output_file = self.convert_file()

    def convert_file(self):
        input_title = Path(self.input_file).stem
        doc = aw.Document(self.input_file)
        output_title = input_title + ".docx"
        #TODO: fix convert file so that it can convert to any extension
        output_file = doc.save(output_title)
        return output_file

        #Documentation here : https://pypi.org/project/aspose-words/