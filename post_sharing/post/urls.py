from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('upload/', views.upload.as_view(), name='upload'),
    path('uploadedSuccess/', views.uploadedSuccess.as_view(), name='uploadedSuccess'),
    path('list/', views.postList.as_view(), name='postList')
]

