import instaloader
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()

def download_post(request):
    L = instaloader.Instaloader()
    inputt = request.GET['link']
    url = inputt
    post = instaloader.Post.from_shortcode(
        L.context, url.split("/")[-2])
    username = post.owner_username
    likes = post.likes
    isv = post.is_video


    # Download the post
    a = L.download_post(post, target="downloads")
    print(a)
    return Response({
        'usernmae': username,
        'likes': likes,
        'path': L.download_post(post, target="downloads")
    })