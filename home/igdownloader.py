import instaloader
from rest_framework.decorators import api_view
from rest_framework.response import Response
import urllib.request

@api_view()

def download_post(request):
    L = instaloader.Instaloader()
    inputt = request.GET['link']
    url = inputt
    post = instaloader.Post.from_shortcode(
        L.context, url.split("/")[-2])
    username = post.owner_username
    likes = post.likes
    path = post.url
    isv = post.is_video
    imgURL = path

    urllib.request.urlretrieve(imgURL, "/Users/rangolivision/freelance-project--ytmp3/igdownload/ig01.png")


    # Download the post
    # a = L.download_post(post, target="downloads")

    return Response({
        'usernmae': username,
        'likes': likes,
        'path': path,
    })