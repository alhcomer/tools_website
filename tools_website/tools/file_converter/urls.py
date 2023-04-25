from . import views
from django.urls import path, include


app_name = 'file_converter'

urlpatterns = [
    path('', views.about, name='about'),
    path('file_converter', views.file_converter, name="file_converter"),
    path('<int:files_id>/download', views.download, name="download"),
]
