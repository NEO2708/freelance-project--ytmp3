from django.contrib import admin
from django.urls import path
from home import views
from home import igdownloader

urlpatterns = [
    path('', views.download_video),
    path('insta',igdownloader.download_post )
]
