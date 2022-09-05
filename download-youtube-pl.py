import sys
from pytube import YouTube
from pytube import Playlist
url = sys.argv[1]
print('Playlist URL: ' + url)

p = Playlist(url)
print('Playlist Title: ' + p.title)

for video in Playlist(url).videos:
    print('URL: ' + video.watch_url)
    video.streams.filter(progressive=True).order_by('resolution').desc().first().download('.')