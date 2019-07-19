from django.urls import path

from . import views


urlpatterns = [
    path('upload/', views.upload.as_view(), name='upload'),
]