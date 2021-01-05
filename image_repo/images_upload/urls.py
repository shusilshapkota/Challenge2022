from django.urls import path
from .views import postImage

urlpatterns = [
    path('upload_img/', postImage.as_view(), name='postImage'),
]
