import sys
import os
from pytube import YouTube

class Media(object):
    def download(self, url):
        try:
            yt = YouTube(url)
        except Exception as e:
            print(e)
            raise SystemExit

        filename = os.getcwd() + "\\" + yt.filename.replace("!", "").replace("&","").replace(" ", "-") + ".mp4"

        # Finds best quality for the video
        resolutions = ["1080p", "720p", "480p", "360p", "240p"]
        video_info = yt.filter("mp4")
        for resolution in resolutions:
            if resolution in str(video_info):
                res = resolution
                break

        # Downloads the video
        try:
            video = yt.get("mp4", res)
            video.download(filename)
        except Exception as e:
            print(e)
            raise SystemExit

        return filename

    def convert(self, filename):
        mp3 = filename.replace("mp4", "mp3") 
        try:
            os.system("ffmpeg -i {} {}".format(filename, mp3))
            os.remove(filename)
        except Exception as e:
            print(e)
            raise SystemExit
        

if __name__ == '__main__':
    m = Media()
    try:
        video_id = sys.argv[1]
    except:
        print("""You need to provide a YouTube URL in order for this to work...
Syntax: 'mp3 VIDEOID'
Ex. http://youtube.com/watch?v=VIDEOID""")
        raise SystemExit
    url = "http://youtube.com/watch?v={}".format(video_id)
    filename = m.download(url) 
    m.convert(filename)
