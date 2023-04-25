from django import forms
from django.core.validators import FileExtensionValidator
from .validators import FileValidator

conversion_choices = (
    ("1", "DOC"),
    ("2", "DOCX"),
    ("3", "HTML"),
    ("4", "ODT"),
    ("5", "PDF"),
    ("6", "PPT"),
    ("7", "PPTX"),
    ("8", "RTF"),
    ("9", "TXT"),
    ("10", "XLSX"),
)

allowed_extensions=["doc", "docx", "html", "odt", "pdf", "ppt", "pptx", "rtf", "txt", "xlsx"]
validator = FileValidator(max_size=1000, min_size=100, content_types=allowed_extensions)



class FileUploadForm(forms.Form):
    file = forms.FileField(label="", validators=[validator])
    conversion_doctype = forms.ChoiceField(choices=conversion_choices, label="Convert to:")
    # TODO: handle file conversion asynchronously on the page