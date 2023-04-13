from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'tools/index.html')

@login_required
def tools(request):
    tools = 'tools'
    return render(request, 'tools/tools.html', {'tools': tools})

#TODO:  create about page
#TODO: create market section (selling whatever) to demonstrate e-commerce platform capabilities

