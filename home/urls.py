from django.contrib import admin
from django.urls import path
from home import views
from home import igdownloader
from home import postDownloader
from home import ytdownloader

urlpatterns = [
    path('', views.download_video),
    path('insta',igdownloader.InstaDownloader ),
    path('downloadfile',postDownloader.download_file),
    path('ytdownload',ytdownloader.ytdownload),
]
