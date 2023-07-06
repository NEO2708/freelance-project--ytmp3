
from django.urls import path
from home import igdownloader
from home import home


urlpatterns = [
    path('insta',igdownloader.InstaDownloader ),
    path('homepage',home.homepage),

]
