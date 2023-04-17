from django import forms

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

class FileUploadForm(forms.Form):
    file_field = forms.FileField()
    conversion_doctype = forms.ChoiceField(choices=conversion_choices)
    # TODO: handle file conversion asynchronously on the page