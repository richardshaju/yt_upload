import os

vid_dirs = []
for file in os.scandir("./raw_videos"):
    vid_dirs.append(file.path)
    
import cv2

for file in vid_dirs:
    file_path = file  # change to your own video path
    vid = cv2.VideoCapture(file_path)
    height = vid.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width = vid.get(cv2.CAP_PROP_FRAME_WIDTH)
     
    print(height,width)