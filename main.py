# python version 3.11.3
# Press Ctrl+F8 to toggle the breakpoint.

import sys
from sys import argv
from pytube import YouTube

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)

#If you want to download video with highest resolution
#yd = yt.streams.get_highest_resolution()

#If you want to download with audio only
yd = yt.streams.get_audio_only()

#If you want to convert the video to mp4
#yd = yt.streams.filter(file_extension='mp4')
yd.download('D:\Videos')


print("python version: ", sys.version)


