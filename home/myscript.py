
from pytube import YouTube
from django.http import FileResponse


def process_data(input_string):

    # yt = YouTube(input_string)
    # value1 = yt.thumbnail_url
    # value2 = yt.title
    # context = {
    #     'value1': value1,
    #     'value2': value2
    # }
    output = FileResponse(
        open(YouTube(input_string).streams.first().download(skip_existing=True), 'rb'))

    return output
