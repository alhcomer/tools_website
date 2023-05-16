from django.shortcuts import render
from .models import FileConversion
from .forms import FileUploadForm
from .converter import FileConverter
from django.conf import settings
from .models import user_directory_path

def about(request):
    return render(request, 'tools/file-converter/about.html')

def file_converter(request):

    # TODO: make it so that if file is already in db, ask whether to overwrite or not

    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        for field in form:
            for error in field.errors:
                print(error)

        print(request.FILES['input_file'])

        if form.is_valid():
            # TODO: grab file from request.FILES, convert file and save to db
            file_to_convert_base = form.save(commit=False)
            file_to_convert_base.user = request.user
            file_to_convert_base.output_file = FileConverter(request.FILES['input_file'], request).output_file
            file_to_convert_base.save()
            form.save_m2m()
            context = {}
            context["user_files"] = user_files
            context["form"] = FileUploadForm()
            return render(request, 'tools/file-converter/file-converter.html', context=context)
        #TODO: get object from Form, convert file here and save. Then render page again with updates user files
    else: 
        user_files = FileConversion.objects.filter(user=request.user.id)
        context = {}
        context["user_files"] = user_files
        context["form"] = FileUploadForm()
        return render(request, 'tools/file-converter/file-converter.html', context=context)

def download(request, files_id):
    #TODO: Fix so that user can only view if file id matches request.user id
    files_to_download = FileConversion.objects.get(id=files_id)
    if request.user.id == files_to_download.user.id:
        return render(request, 'tools/file_converter/<int:user_id>/<int:file_id>/download')