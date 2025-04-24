from django.urls import path
from .views import UploadVideo, UploadImage

urlpatterns = [
    path('upload-video/', UploadVideo.as_view(), name='upload_video'),
    path('upload-image/', UploadImage.as_view(), name='upload_image'),
]