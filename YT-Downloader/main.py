from pytube import YouTube 
while 1:
    def download(link):
        youtube_object = YouTube(link)
        youtube_object = youtube_object.streams.get_highest_resolution()
        try:
            youtube_object.download()
        except:
            print("Error happens while downloading your video")
            print("Try again!")
        print("Your download is completed")
    link = input("Enter your link here to download: ")
    download(link)