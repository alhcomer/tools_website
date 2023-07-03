from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'tools/index.html')

def about(request):
    return render(request, 'tools/about-us.html')

@login_required
def tools(request):
    return render(request, 'tools/tools.html')

#TODO:  create general about page for website
#TODO: create market section (selling whatever) to demonstrate e-commerce platform capabilities
#TODO: if user not logged in, making clicking on tools link show alert saying you need to create an account. Until then, make Tools link bootstrap disabled and hide Tools drop down
#TODO: implement the following tools

"""
Image converters: Similar to PDF converters, image converters allow users to convert image files between different formats. This could include tools for converting between JPEG, PNG, GIF, and other image file types.

File compression tools: These tools allow users to compress files into a smaller size, making it easier to transfer them over the internet or store them on a device with limited storage space.

Unit converters: Unit converters can be useful for converting between different units of measurement, such as length, weight, temperature, and more.

Encryption/decryption tools: These tools can be used to encrypt sensitive files or messages to protect them from unauthorized access. Similarly, decryption tools can be used to reverse the encryption process and access the original data.

Audio/Video converters: These tools allow users to convert audio and video files between different formats. This could include tools for converting between MP3, WAV, AVI, MP4, and other formats.

OCR (Optical Character Recognition) tools: These tools can be used to extract text from images or scanned documents. Users can upload an image file and the tool will extract the text and convert it into an editable format.

Code converters: These tools can be useful for developers who need to convert code between different programming languages. For example, a tool that converts Python code to Java code.

"""