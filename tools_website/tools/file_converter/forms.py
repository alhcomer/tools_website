from django import forms
from django.core.validators import FileExtensionValidator
import mimetypes
from .models import FileConversion

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


class FileUploadForm(forms.ModelForm):
    conversion_doctype = forms.ChoiceField(choices=conversion_choices, label="Convert to:")

    class Meta:
        model=FileConversion
        fields = ["input_file"]