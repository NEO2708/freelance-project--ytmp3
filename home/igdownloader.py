import instaloader
import datetime
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import urllib.request
from firebase_admin import storage
from rest_framework.response import Response
from rest_framework.decorators import api_view
import datetime


@api_view()

def InstaDownloader(request):
    inputt =request.GET['link']

    cred = credentials.Certificate('/Users/rangolivision/freelance-project--ytmp3/static/khudkibook-firebase-adminsdk-vegxe-be3361f282.json')
    firebase_admin.initialize_app(cred, {
    "storageBucket": "khudkibook.appspot.com"
    })
    
    db = firestore.client()

    def upload_file(url, filename):
        # Fetch the file from the URL
        file_data = urllib.request.urlopen(url).read()

        # Upload the file to Firebase Storage
        bucket = storage.bucket()
        blob = bucket.blob(filename)
        blob.upload_from_string(file_data, content_type='application/octet-stream')

        # Create a Firestore document to store the file details
        file_ref = db.collection('files').document()
        file_ref.set({
            'filename': filename,
            'download_url': blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET'),
        })

        # Return the downloadable link
        return blob.generate_signed_url(datetime.timedelta(seconds=300), method='GET')

    L = instaloader.Instaloader()
    url = inputt
    post = instaloader.Post.from_shortcode(
        L.context, url.split("/")[-2])
    media= post._full_metadata_dict
    # print(media)
    owner=media.get("owner")
    profile_pic=owner.get("profile_pic_url")
    isprivate=owner.get("is_private")
    
        # Checking if the post is private
    if(isprivate== True):
        return Response("Requested POST is PRIVATE")
    else:
        username = post.owner_username
        likes = post.likes
        mediacount=post.mediacount
        print(mediacount)
        imagepost=[]
        videocover=[]
        imgcover=[]
        videopost=[]
        if(mediacount > 1):
            sidecar=media.get("edge_sidecar_to_children")
            edge=sidecar.get("edges")

            for i in range(mediacount):
                if(i==0):
                    filename=f'{"VIG001"+username+".png"}'
                    filenamev=f'{"VIG001"+username+".mp4"}'
                if(i==1):
                    filename=f'{"VIG002"+username+".png"}'
                    filenamev=f'{"VIG002"+username+".mp4"}'
                if(i==2):
                    filename=f'{"VIG003"+username+".png"}'
                    filenamev=f'{"VIG003"+username+".mp4"}'
                if(i==3):
                    filename=f'{"VIG004"+username+".png"}'
                    filenamev=f'{"VIG004"+username+".mp4"}'
                if(i==4):
                    filename=f'{"VIG005"+username+".png"}'
                    filenamev=f'{"VIG005"+username+".mp4"}'
                if(i==5):
                    filename=f'{"VIG006"+username+".png"}'
                    filenamev=f'{"VIG006"+username+".mp4"}'
                if(i==6):
                    filename=f'{"VIG007"+username+".png"}'
                    filenamev=f'{"VIG007"+username+".mp4"}'
                if(i==7):
                    filename=f'{"VIG008"+username+".png"}'
                    filenamev=f'{"VIG008"+username+".mp4"}'
                if(i==8):
                    filename=f'{"VIG009"+username+".png"}'
                    filenamev=f'{"VIG009"+username+".mp4"}'
                if(i==9):
                    filename=f'{"VIG010"+username+".png"}'
                    filenamev=f'{"VIG010"+username+".mp4"}'
                node=edge[i]
                nodes=node.get("node")
                resource=nodes.get("display_resources")
                videourl=nodes.get("video_url")
                isposttype=nodes.get("is_video")


                src1080=resource[2]
                if(isposttype == True):
                    video=videourl
                    file_url = video
                    file_name = filenamev
                    video=upload_file(file_url, file_name)
                    # videocover.append(video)
                    videopost.append(video)
                else:
                    file_url = src1080.get("src")
                    file_name = filename
                    image=upload_file(file_url, file_name)
                    # imgcover.append(image)
                    imagepost.append(image)         
            return Response({"videourls":videopost,"imageurls":imagepost,"username":username,"likes":likes,"profilepic":profile_pic,"type":"video"})
        else:
            istype=post.is_video
            if(istype==True):
                video=post.video_url
                file_url = video
                file_name = "VID"+username+".mp4"
                video=upload_file(file_url, file_name)
                return Response({"video_url":video,"username":username,"likes":likes,"profilepic":profile_pic,"type":"video"})
            else:
                image=post.url
                file_url = image
                file_name = "VID"+username+".png"
                image=upload_file(file_url, file_name)
                return Response({"image_url":image,"username":username,"likes":likes,"profilepic":profile_pic,"type":"image"})









