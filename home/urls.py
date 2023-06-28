from django.contrib import admin
from django.urls import path
from home import views
from home import igdownloader
from home import postDownloader
from home import ytdownloader
from home import home

urlpatterns = [
    path('', views.download_video),
    path('insta',igdownloader.InstaDownloader ),
    path('downloadfile',postDownloader.download_file),
    path('ytdownload',ytdownloader.ytdownload),
    path('homepage',home.homepage)

]
