from moviepy.editor import (
    VideoFileClip,
    concatenate_audioclips,
    AudioFileClip,
    TextClip,
    CompositeVideoClip,
)
import moviepy.editor as mpe
import random
import os
import re
import pandas as pd

contents = []
vid_dirs = []



df = pd.read_csv('./contents.csv')
for index, row in df.iterrows():
    contents.append(row['Data'])
    
for file in os.scandir("preprocessed"):
    vid_dirs.append(file.path)
    

def video_with_text(value, path):
    
    print("Value : ",value)
    words = value.split()
    first_three_words = ' '.join(words[:4])
    new_path = first_three_words.replace('"','')
    value = value.replace('"','')
    value = value.replace("\\n", "\n")

    headings = ['motivational fact', 'inspiring truth', 'encouraging reality','Positive revelation','Galvanizing reality']
    heading_data = random.choice(headings)

    # Load the video clip
    video_clip = VideoFileClip(path)

    # Create a text clip with the desired text and styling
    font_path = "fonts\BebasNeue-Regular.ttf"

    heading = TextClip("\t" + heading_data + "\t", font=font_path, fontsize=65,   color="white", bg_color="black")
    heading = heading.set_duration(video_clip.duration)
    heading = heading.set_position(("center",500))
    print(value)
    txt_clip = TextClip(
        value,
        font=font_path,
        fontsize=70,
        color="white",
    )
    txt_clip = txt_clip.set_duration(video_clip.duration)
    txt_clip = txt_clip.set_position(("center", "center"))

    tag = TextClip("@dailyquotes24x7", fontsize=30,   color="white")
    tag = tag.set_duration(video_clip.duration)
    tag = tag.set_position(("center",1800))  


    # Overlay the text on the video using CompositeVideoClip
    video_with_text = CompositeVideoClip([video_clip, heading,txt_clip,tag])



    # Write the final video with text and background music
    video_with_text.write_videofile("final_output/"+new_path +"......mp4",codec="libx264")


for value, path in zip(contents, vid_dirs):
    video_with_text(value, path)
    
