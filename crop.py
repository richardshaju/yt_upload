import cv2
from moviepy.video.fx import colorx
# Set the input video file path

import os
img_dirs = []
for file in os.scandir("raw_videos"):
        img_dirs.append(file.path)
print(img_dirs)

def crop_video(path):

    input_video_path = path

    # Define the aspect ratio for YouTube Shorts (9:16)
    aspect_ratio_width = 9
    aspect_ratio_height = 16

    # Function to apply a dark filter to a frame
    def apply_dark_filter(frame, brightness_factor=0.7, contrast_factor=0.7):
        # Adjust brightness and contrast
        adjusted_frame = cv2.convertScaleAbs(frame, alpha=brightness_factor, beta=0)
        adjusted_frame = cv2.convertScaleAbs(adjusted_frame, alpha=contrast_factor, beta=0)

        return adjusted_frame

    # Calculate the cropping dimensions to maintain the aspect ratio
    cap = cv2.VideoCapture(input_video_path)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    if frame_width / aspect_ratio_width > frame_height / aspect_ratio_height:
        # Crop the width to maintain the aspect ratio
        crop_width = int(frame_height * aspect_ratio_width / aspect_ratio_height)
        crop_height = frame_height
        crop_x = int((frame_width - crop_width) / 2)
        crop_y = 0
    else:
        # Crop the height to maintain the aspect ratio
        crop_width = frame_width
        crop_height = int(frame_width * aspect_ratio_height / aspect_ratio_width)
        crop_x = 0
        crop_y = int((frame_height - crop_height) / 2)

    # Set the output video file path
    new_path = path.split('\\')[1]
    output_video_path = './cropped/'+ new_path

    # Open the input video file
    cap = cv2.VideoCapture(input_video_path)

    # Create a VideoWriter object to write the cropped video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, 30.0, (crop_width, crop_height))

    # Loop through the frames, crop, and write to the output video
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Crop the frame
        cropped_frame = frame[crop_y:crop_y + crop_height, crop_x:crop_x + crop_width]
        dark_frame = apply_dark_filter(cropped_frame)
        # Write the cropped frame to the output video
        out.write(dark_frame)

    # Release the video objects
    cap.release()
    out.release()

    print(f"Video cropped for YouTube Shorts and saved as '{output_video_path}'")

for img_dir in img_dirs:
        print(img_dir)
        crop_video(img_dir)



