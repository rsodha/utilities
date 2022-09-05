import sys
from pytube import YouTube
url = sys.argv[1]
YouTube(url).streams.filter(progressive=True).order_by('resolution').desc().first().download('.')