from . import views
from django.urls import path

app_name = 'converter'

urlpatterns = [
    path('', views.file_converter, name='file_converter'),
    path('<int:files_id>/download', views.download, name='download'),
]