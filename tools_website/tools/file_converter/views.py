from django.shortcuts import render
from .models import FileConverter

def about(request):
    return render(request, 'tools/pdfconverter/about.html')

def file_converter(request):
    if request.method == "POST":
        pass
        #TODO: get object from Form, convert file here and save. Then render page again with updates user files
    else: 
        user_files = FileConverter.objects.filter(user=request.user)
        return render(request, 'tools/file-converter/file-converter.html', context={'user_files': user_files})