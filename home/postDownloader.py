import instaloader
from rest_framework.decorators import api_view
from rest_framework.response import Response
import urllib.request
from django.http import HttpResponse

@api_view()

def download_file(request):
    L = instaloader.Instaloader()
    inputt = request.GET['link']
    url = inputt
    post = instaloader.Post.from_shortcode(
        L.context, url.split("/")[-2])
    istype=post.is_video
    username = post.owner_username
    likes = post.likes

    if(istype == True):
        video=post.video_url

        
        return Response({
        "type":"video",
        'username': username,
        'likes': likes,
        'video_url':video,
    })
        
    else:
        path = post.url
        imgURL = path
        return Response({
        "type":"image",
        'username': username,
        'likes': likes,
        'img_url':imgURL,
    })
