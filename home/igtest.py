import instaloader
import datetime
import firebase_admin
import urllib.request
from firebase_admin import storage
from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime
from apify_client import ApifyClient


@api_view()


def InstaDownloader(request):
    inputt =request.GET['link']
    stream=[]
    client = ApifyClient("apify_api_fm36Y2p2MK3N2YBIIj7Yir32u7nQ7m0eV4rH")

    # Prepare the Actor input
    run_input = {
        "directUrls": [inputt],
        "resultsType": "details",
        "resultsLimit": 200,
        "searchType": "hashtag",
        "searchLimit": 1,
        "proxy": {
            "useApifyProxy": True,
            "apifyProxyGroups": ["RESIDENTIAL"],
        },
        "maxRequestRetries": 11,
        "extendOutputFunction": """async ({ data, item, helpers, page, customData, label }) => {
      return item;
    }""",
        "extendScraperFunction": """async ({ page, request, label, response, helpers, requestQueue, logins, addProfile, addPost, addLocation, addHashtag, doRequest, customData, Apify }) => {
        
    }""",
        "customData": {},
    }

    # Run the Actor and wait for it to finish
    run = client.actor("apify/instagram-scraper").call(run_input=run_input)

    # Fetch and print Actor results from the run's dataset (if there are any)
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(item)
        stream.append(item)
    return Response({"stream":stream})
    