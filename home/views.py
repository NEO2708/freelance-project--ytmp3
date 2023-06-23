from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import youtube_dl
from pytube import YouTube
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view()


def download_video(request):

    link=request.GET['link']
    if 'm.' in link:
            link = link.replace(u'm.', u'')

    elif 'youtu.be' in link:
            video_id = link.split('/')[-1]
            link = 'https://www.youtube.com/watch?v=' + video_id
    inputt = link
    yt=YouTube(inputt)
    


    if(inputt != ""):
        video_url = inputt
       
        print(video_url)

        ydl_opts = { 'verbose': True, }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(
                video_url, download=False)
        video_audio_streams = []
        for m in meta['formats']:
            file_size = m['filesize']
            if file_size is not None:
                file_size = f'{round(int(file_size) / 1000000,2)} mb'

            resolution = 'Audio'
            if m['height'] is not None:
                resolution = f"{m['height']}x{m['width']}"
            video_audio_streams.append({
                'resolution': resolution,
                'extension': m['ext'],
                'file_size': file_size,
                'video_url': m['url']
            })
  
    context = {
        'title': meta['title'],
        'description': meta['description'], 'likes': meta['like_count'],
        'dislikes': meta['dislike_count'], 'thumb': meta['thumbnails'][3]['url'],
        'duration': round(int(meta['duration'])/60, 2), 'views': f'{int(meta["view_count"]):,}'
    }


    return Response(context)

