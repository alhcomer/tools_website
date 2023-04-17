from django.shortcuts import render
from .models import FileConverter
from .forms import FileUploadForm

def about(request):
    return render(request, 'tools/file-converter/about.html')

def file_converter(request):
    if request.method == "POST":
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            file_to_convert = FileConverter.objects.get(file_field=form)
            #TODO: finish this
        #TODO: get object from Form, convert file here and save. Then render page again with updates user files
    else: 
        user_files = FileConverter.objects.filter(user=request.user.id)
        context = {}
        context["user_files"] = user_files
        context["form"] = FileUploadForm
        return render(request, 'tools/file-converter/file-converter.html', context=context)