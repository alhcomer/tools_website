from . import views
from django.urls import path


app_name = 'tools'

urlpatterns = [
    path('', views.index, name='index')
]
