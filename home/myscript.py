
from pytube import YouTube
from django.http import FileResponse


def process_data(input_string):
    output = FileResponse(
        open(YouTube(input_string).streams.first().download(skip_existing=True), 'rb'))

    return output
