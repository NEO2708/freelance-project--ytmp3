from django.contrib import admin
from django.urls import path
from home import views
from home import igdownloader
from home import postDownloader

urlpatterns = [
    path('/', views.download_video),
    path('insta',igdownloader.download_post ),
    path('downloadfile',postDownloader.download_file)
]
