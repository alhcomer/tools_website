from django.shortcuts import render

def about(request):
    return render(request, 'tools/pdfconverter/about.html')