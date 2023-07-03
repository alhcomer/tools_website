from . import views
from django.urls import path, include

app_name = 'tools'

urlpatterns = [
    path('', views.index, name='index'),
    path('tools/', views.tools, name='tools'),
    path('tools/file_converter/', include('tools.file_converter.urls')),
]