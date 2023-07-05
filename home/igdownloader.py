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
    if not firebase_admin._apps:
    # Initialize the Firebase app
        cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "khudkibook",
  "private_key_id": "be3361f282e441a2265d7da26605cf9d6943b401",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDK24YUVWB9XwM7\nd6ZCo4lYD2eeXai8CcsxosSYSkCG8v41hdfLw9AOWuM7HkMfnbiASnSga7q7oDIQ\nSD9jke9VsKoaITxCVsXQ+7zAXZlhFQj7WKNkIkWCUBSxfQ4HspCmYYZ5VtQCPEc7\n+ZtogQk2TBYRjosAWnQRuswGq5Xz0Yd64ul8a3/Y+b4BuxQPrLbMMVVkyTKwNEWX\nXQKyfX0QdM+T8+u1o6iLNoiThmiO55D8V8toM1TKvvhT45SEexAqVZftNl+B3Mk3\n2J3Tcs2WG+ETcZf7E5lPDfnIq72vN296+AM/l+deJY5v1B4g5AXHsiXmL8ozn/cB\nz7KiYJLxAgMBAAECggEAC7B/tu8+iqrtdEFOTtu+n9jvZyRNg1xrHZacDoyE0GHz\nPSFT0JWdiR46pt71Dj7X8WiY9N+QWJyAFgkbwgCYUo9GFhBhOQ9oAcVn2IvsOTht\nlpJChBQnfj1gG+QxaUckZ7oJ9jcHK4POtQmKp4h7/+l9ghB9OQ19T8I8XIwJrY2E\npToS6kvTM/AEU6eIEL+VFYWQ+gcVsGWXY1PshoX0Ltr5bUyKFlBLHWW7UjefyVzG\nkCtU3o2rUhJitBTjax+HGvLd5auAs/e6dH8VKgW8N8P0XHCHAjh1c9WT0wBafhln\nBj0ThSHkg9Nd1f/aN3bvlH2K4yjUnN60vsfofUnBAQKBgQDnjKGTO5FLI+STXNZC\n9QGOxX0/P5REBiFeagyXxVMMQVo4UDrKo6vpwVvRlbPJz1KH+DDw4S/eVIy0q6IO\n+ZG+job/hjDfvbnJ8um9ozg6dGsmnRCoVz/5fUSReJJlYbKIk/p+NSGqQ/B8bKAW\nToI5rObJQ8/FVTvCzLQhzUsvoQKBgQDgR0eHpTrE+byViJoiQsnxe+XpGBXwSuGI\nycfek2HpLcrjKwz9fdwgbHQRy+aeAOzb8PDtCo2FUyLbmv9LCoZ4C7nuOBXYMnc6\ngBvxkZzRDjk+fGtYUjZpvS1iLDowPleCf8+KyeZqz3IRerM4KrLvoWDgMkYBBm6r\nWFjLJnrhUQKBgDYIJggSZWQwWv1cM49qVtO3F/PzZSi+eXjrrEaaQDfi5Cex6RYy\nPUKN4Vw1379fBrY930XGdoIeHrtmNani6PSbk7r62FrNjhYm/g5HkS5qzjozepid\ny4rvhVmg1iCcPKoMRe6/fTybH/oY6v5pkY/d3fjnPwugSRK66+nbWwkhAoGAJiL4\nvtAR1jzBHIxF6V2CCVYQGjrGQD37a88j9W0KUSRAQ7CmXNRyAfFvKzeI14VAwYWO\n8j/BINKqMr2Ae7omc3NLAn729/Rc4c228rTX/ZR1l3KArlwMdJ5+gRsUKe/v4Xjq\nSadbTv5HX0GGCB76nlTKrFTgInx9hRVYw/KfIoECgYBq0CAooEw6pdwGRKHEFZbV\n4tf5tpP50wJ61sab1AmsNoCoUrQUCzsqncFfYCcvwXE+eI4nk3ens5X6Q4zHrCZe\nWnzDEXbfERpXlvW9IcnUs7WHODqiADBiY/W5tnayGc4Ozx34B4f6Bh9/R9eW63dr\nmbp3GRtAbvwv8zfvNuD8ZA==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-vegxe@khudkibook.iam.gserviceaccount.com",
  "client_id": "106681282986463050082",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-vegxe%40khudkibook.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
)
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
        return Response({"account_type":True})
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
            return Response({"account_type":True,"videourls":videopost,"imageurls":imagepost,"username":username,"likes":likes,"profilepic":profile_pic,"type":"video"})
        else:
            istype=post.is_video
            if(istype==True):
                video=post.video_url
                file_url = video
                file_name = "VID"+username+".mp4"
                video=upload_file(file_url, file_name)
                videopost.append(video)
                return Response({"account_type":False,"videourls":videopost, "imageurls": imagepost, "username":username,"likes":likes,"profilepic":profile_pic,"type":"video"})
            else:
                image=post.url
                file_url = image
                file_name = "VID"+username+".png"
                image=upload_file(file_url, file_name)
                imagepost.append(image)
                return Response({"stream":media,"account_type":False,"imageurls":imagepost,"videourls": videopost,"username":username,"likes":likes,"profilepic":profile_pic,"type":"image"})









