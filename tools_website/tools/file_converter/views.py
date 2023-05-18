from django.shortcuts import render
from .models import FileConversion
from .forms import FileUploadForm
from .converter import FileConverter
from django.conf import settings
from .models import user_directory_path

def about(request):
    return render(request, 'tools/file-converter/about.html')

def file_converter(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)

        if form.is_valid():
            file_to_convert_base = form.save(commit=False)
            file_to_convert_base.user = request.user

            file_converter = FileConverter(request.FILES['input_file'], request)
            file_to_convert_base.output_file.name = file_converter.output_file

            file_to_convert_base.save()
            form.save_m2m()

    user_files = FileConversion.objects.filter(user=request.user.id)
    context = {
        'user_files': user_files,
        'form': FileUploadForm(),
    }
    return render(request, 'tools/file-converter/file-converter.html', context=context)

def download(request, files_id):
    files_to_download = FileConversion.objects.get(id=files_id)
    if request.user.id == files_to_download.user.id:
        return render(request, 'tools/file_converter/<int:user_id>/<int:file_id>/download')