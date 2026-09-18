import os
from moviepy import VideoFileClip
from tkinter import *
from tkinter import filedialog

def openFile():
    path = filedialog.askopenfilename()
    return path

def OpenWindow():
    Window = Tk()
    button = Button(text="Click me to open the Explorer!", command=openFile)
    button.pack()
    Window.mainloop()

print("Welcome to Shut Up Mp4! Enter GUI to open the file browser! ")
video_path = input("Enter the path to the video file: ").strip().strip('"')
output_name = input("Enter the name of the output video file (without extension): ").strip()

if video_path == "GUI":
    video_path = openFile()


if not video_path:
    raise ValueError("you didnt even enter anything or closed the window")

if not os.path.exists(video_path):
    raise FileNotFoundError(f"Video file not found: {video_path}")

if not output_name:
    output_name = "output_video"

input_video = VideoFileClip(video_path)
try:
    muted_video = input_video.without_audio()
    output_path = os.path.splitext(output_name)[0] + ".mp4"
    muted_video.write_videofile(output_path)
    print(f"Video saved as: {output_path}")
finally:
    input_video.close()
    if 'muted_video' in locals():
        muted_video.close()

        print("Congratulations! The video has been muted and is saved in the folder where you saved the script!")
        print("Thanks for using my programm :) This was made by gubbygui")
