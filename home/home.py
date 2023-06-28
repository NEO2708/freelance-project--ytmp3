from django.shortcuts import render

def homepage(request):
      
    # render function takes argument  - request
    # and return HTML as response
    return render(request, "index.html")