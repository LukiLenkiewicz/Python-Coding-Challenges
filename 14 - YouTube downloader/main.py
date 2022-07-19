from pytube import YouTube
import tkinter

def display_videos(url):
    yt = YouTube(url)
    streams = yt.streams.all()
    # streams = yt.streams.filter(only_video=True)
    # streams = yt.streams.filter(only_audio=True)
    res_list = list(enumerate(streams))
    for i in res_list:
        print(i)


def download_highest_resolution(url):
    yt = YouTube(str(url.get()))
    video = yt.streams.get_highest_resolution()
    video.download()


def display_interface():
    root = tkinter.Tk()
    root.geometry("500x300")
    root.resizable(0, 0)
    root.title("You Tube video downloader")
    tkinter.Label(root,text = 'Youtube Video Downloader', font=("Arial", 20)).pack()
    tkinter.Label(root, text = 'Paste Link Here:', font=("Arial", 15)).place(x= 160 , y = 60)
    link = tkinter.StringVar()
    link_enter = tkinter.Entry(root, width = 70, textvariable = link).place(x = 32, y = 90)
    tkinter.Button(root,text = 'DOWNLOAD', font=("Arial", 15), padx = 2, command = lambda: download_highest_resolution(link)).place(x=180, y = 180)
    root.mainloop()


display_interface()