from pytube import YouTube

# Replace 'video_url' with the URL of the YouTube video you want to download
video_url = 'https://youtu.be/tBy-sJVPErE?si=Dh3DVR-8pDM3UzRx'

# Create a YouTube object
yt = YouTube(video_url)

# Get the highest resolution stream
video_stream = yt.streams.get_highest_resolution()

# Download the video
video_stream.download()

print('Video downloaded successfully!')
