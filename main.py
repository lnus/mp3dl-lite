import sys
import os
import string
import pytube
# Failsafe incase of the PyTube version being wrong, seems to be a glitch with version above this one(?)
if pytube.__version__ != "6.2.2":
    os.system("pip install pytube==6.2.2")
    from pytube import YouTube
else:
    from pytube import YouTube

class Media(object):
    def download(self, url):
        try:
            yt = YouTube(url)
        except Exception as e:
            print(e)
            raise SystemExit

        filename = "{}\\{}.mp4".format(os.getcwd(), yt.filename)

        # Makes handling the file with ffmpeg a little bit easier :^) 
        filename = filename.replace(" ", "-")

        # Remove non-ascii characters so that the filename works!!!
        filename = u"{}".format(filename)
        filename = "".join(i for i in filename if i in string.printable)

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
