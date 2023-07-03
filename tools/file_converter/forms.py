from django import forms
from django.core.validators import FileExtensionValidator
import mimetypes
from .models import FileConversion

conversion_choices = (
    (".doc", "DOC"),
    (".docx", "DOCX"),
    (".html", "HTML"),
    (".odt", "ODT"),
    (".pdf", "PDF"),
    (".rtf", "RTF"),
    (".txt", "TXT"),
)


class FileUploadForm(forms.ModelForm):
    conversion_doctype = forms.ChoiceField(choices=conversion_choices, label="Convert to:")

    class Meta:
        model=FileConversion
        fields = ["input_file"]