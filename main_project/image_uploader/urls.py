from django.urls import path
from . import views

urlpatterns = [
    path('', views.uploader, name='upload'),
    path('upload-success/', views.uploaded, name='upload_success')
]
