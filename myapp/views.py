from __future__ import unicode_literals

from rest_framework.decorators import api_view
from rest_framework.response import Response
import youtube_dl

# Create your views here.
@api_view(["POST"])
def GetAudio(videoId):
    vidid = videoId.data["video_id"]

    #return Response({'status': 'Successaaa'})

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': '/home/saadaftab/iTube/media/'+vidid+'.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320'
        }],
    }
    mypath = 'https://www.youtube.com/watch?v='+vidid
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([mypath])

    return Response({'status': 'Success'})
