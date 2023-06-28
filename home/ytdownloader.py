import instaloader
from rest_framework.decorators import api_view
from rest_framework.response import Response
import urllib.request
import requests
from django.http import HttpResponse
from django.core.files.base import ContentFile
from .models import Igdatabse


@api_view()

def ytdownload(request):
    file_url = request.GET['link']  # Get the file URL from the query parameters

    if file_url:
        try:
            # Fetch the file from the URL
            response = requests.get(file_url)
            file_data = response.content
            
            # Create a new instance of the Igdatabse
            file_model = Igdatabse()
            
            # Assign the fetched file to the file field
            file_model.file.save(file_url.split('/')[-1], ContentFile(file_data))
            
            # Save the model instance to the database
            file_model.save()
            
            return HttpResponse('File uploaded successfully.')

        except Exception as e:
            # Handle any errors that occur during the file upload
            return HttpResponse(f'Error uploading file: {str(e)}', status=500)

    else:
        return HttpResponse('File URL is missing.', status=400)
