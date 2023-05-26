from django.shortcuts import render
from .models import FileConversion
from .forms import FileUploadForm
from .converter import FileConverter
from django.conf import settings
from .models import user_directory_path
import uuid
from django.contrib.auth.decorators import login_required
import os

def about(request):
    return render(request, 'tools/file-converter/about.html')

# TODO: must specify login_required redirect url
# TODO: delete redundant code, e.g. potentially the code below
# TODO: make input file and output file have same name excluding file extension
@login_required
def file_converter(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            conversion_choice = form.cleaned_data['conversion_doctype']
            print(conversion_choice)
            input_file = request.FILES['input_file']
            file_to_convert_base = form.save(commit=False)
            file_to_convert_base.user = request.user

            # if FileConversion.objects.filter(user=request.user, input_file=input_file).exists():
            #     print("This is the if")
            #     unique_filename = str(uuid.uuid4()) + '_' + input_file.name
            #     file_converter = FileConverter(input_file, request)
            #     file_to_convert_base.output_file.name = os.path.join('uploads', unique_filename)

            # else:
            #     print("This is the else")
            #     print(input_file.name)
            file_converter = FileConverter(input_file, request)
            file_converter.input_file.name = input_file.name
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