import os
from moviepy import VideoFileClip

video_path = input("Enter the path to the video file: ").strip().strip('"')
output_name = input("Enter the name of the output video file (without extension): ").strip()

if not video_path:
    raise ValueError("No video path entered.")

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
        print("Thanks for using my programm :)")
