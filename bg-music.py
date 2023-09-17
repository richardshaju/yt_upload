from moviepy.editor import VideoFileClip, concatenate_audioclips,AudioFileClip, TextClip, CompositeVideoClip
import random

import os
vid_dirs = []
bgm_dirs = []
for file in os.scandir("cropped"):
    vid_dirs.append(file.path)
for file in os.scandir("BGM"):
    bgm_dirs.append(file.path)

random.shuffle(bgm_dirs)

def add_bgm():

    count = 103
    for video, audio in zip(vid_dirs, bgm_dirs):
        
        video_clip = VideoFileClip(video)

        # Load the background music tracks
        audio_clip = AudioFileClip(audio)
        
        music1 = audio_clip.subclip(0, video_clip.duration)

        # Set the volume level for each background music track
        music1 = music1.volumex(0.5)  # Adjust the volume as needed

        # Set the duration of the text clip to match the video duration

        # Set the audio for the video with text
        clip = video_clip.set_duration(video_clip.duration)
        video_with_bgm = clip.set_audio(music1)

        # Write the final video with text and background music
        video_with_bgm.write_videofile("preprocessed/shorts"+ str(count)+ ".mp4", codec="libx264")
        count += 1

add_bgm()