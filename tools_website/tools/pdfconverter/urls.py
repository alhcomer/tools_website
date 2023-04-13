from . import views
from django.urls import path, include


app_name = 'pdfconverter'

urlpatterns = [
    path('', views.about, name='about')
]
