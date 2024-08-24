from argparse import ArgumentParser
from pytube import YouTube

## Banner displayed when the code runs
BANNER = """
***************************************
**       YouTube Video Downloader     **
***************************************
"""

# Message displayed every time the code runs
MESSAGE = "Thank you for using the YouTube Video Downloader!\n"

def get_url():
    ## Create an ArgumentParser object to handle command-line arguments
    parser = ArgumentParser()
    ## Add arguments for YouTube URL, resolution, and custom filename
    parser.add_argument("-u", "--url", dest="url", help="Enter The Url For The Youtube Video To Download")
    parser.add_argument("-r", "--resolution", dest="res", default="1080p", help="Enter The Resolution For The Video (default: 720p)")
    parser.add_argument("-n", "--filename", dest="filename", help="Enter Custom Filename (optional)")
    ## Parse the command-line arguments and return the URL, resolution, and filename
    args = parser.parse_args()
    return args.url, args.res, args.filename

def download_video(url, res, filename=None):
    try:
        ## Create a YouTube object for the given video URL
        yt = YouTube(url)
        ## Filter and select the appropriate video stream based on resolution
        video_stream = yt.streams.filter(progressive=True, file_extension="mp4", resolution=res).first()
        ## Download the video using the specified filename if provided, otherwise use the original filename
        if video_stream:
            if filename:
                video_stream.download(filename=filename)
            else:
                video_stream.download()
            print("Video Downloaded Successfully\n")
        else:
            print(f"No {res} resolution available for the provided video. Use -h for help.\n")
    except Exception as e:
        print(f"An error occurred: {e}\n")

if __name__ == "__main__":
    print(BANNER)
    ## Get YouTube URL, resolution, and custom filename from command-line arguments
    video_url, resolution, custom_filename = get_url()
    ## If the URL is provided, download the video with the specified resolution and filename
    if video_url:
        download_video(video_url, resolution, custom_filename)
    print(MESSAGE)
