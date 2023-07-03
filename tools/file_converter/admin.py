from django.contrib import admin
from .models import FileConversion

@admin.register(FileConversion)
class FileConversionAdmin(admin.ModelAdmin):
    list_display = ['user', 'input_file', 'uploaded_at']