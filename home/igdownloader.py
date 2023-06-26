import instaloader
from rest_framework.decorators import api_view
from rest_framework.response import Response
import urllib.request
from django.http import HttpResponse

@api_view()

def download_post(request):
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
        file_url = video 
        file_name = username+"001.mp4"
        if file_url and file_name:
            try:
                file_data = urllib.request.urlopen(file_url).read()
                content_type = 'application/octet-stream'
                response = HttpResponse(file_data, content_type=content_type)
                response['Content-Disposition'] = f'attachment; filename="{file_name}"'
                return response
                
            except Exception as e:
                return HttpResponse(f'Error downloading file: {str(e)}', status=500)
        else:
            return HttpResponse('File URL or desired file name is missing.', status=400)
   
    else:
        path = post.url
        imgURL = path
        file_url = imgURL 
        file_name = username+"001.jpg"  
        if file_url and file_name:
            try:
                file_data = urllib.request.urlopen(file_url).read()
                content_type = 'application/octet-stream'
                response = HttpResponse(file_data, content_type=content_type)
                response['Content-Disposition'] = f'attachment; filename="{file_name}"'
                return response                
            except Exception as e:
                return HttpResponse(f'Error downloading file: {str(e)}', status=500)

        else:
            return Response({'error': 'File URL or desired file name is missing.'}, status=400)


    