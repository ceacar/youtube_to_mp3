#!/usr/bin/env python

from __future__ import unicode_literals
import youtube_dl
import sys

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}

def download_link(youtube_link):
    if "youtube" not in youtube_link:
        raise Exception("not a valid youtube link")

    print("processing:",youtube_link)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_link])

def reformat_mobile_link(mobile_youtube_link:'https://youtu.be/YqFHIU4qc-k'):
    strArray = mobile_youtube_link.split('/')
    youtube_hash_code = strArray[-1]
    return "https://www.youtube.com/watch?v={0}".format(youtube_hash_code)

if sys.argv[1] == '-f':
    file_name = sys.argv[2]
    with open(file_name, 'r') as f:
        links = f.readlines()
        for link in links:
            download_link(link)
else:
    youtube_link= sys.argv[1]
    if "youtu.be" in youtube_link:
        #it is a mobile link
        youtube_link = reformat_mobile_link(youtube_link)
    download_link(youtube_link)



