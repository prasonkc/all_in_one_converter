from PIL import Image
from moviepy.editor import VideoFileClip
import os
import time, threading

CONVERTED_DIR = "./converted"
def convert_video_to_gif(input_file, format):
    
    if not os.path.isfile(input_file):
        raise FileNotFoundError('Input file does not exist.')
    
    filename = input_file[7:].split(".")[0]
    try:
        os.makedirs(CONVERTED_DIR, exist_ok=True)
        
        # input path = ./temp/ ie 7 letters
        print(filename)

        timestamp = int(time.time())
        output_filename = f"{filename}_converted_{timestamp}.{format}"
        output_file = os.path.join(CONVERTED_DIR, output_filename)
        
        clip = VideoFileClip(input_file)
        clip.write_gif(output_file, fps=10)
        
        print("Conversion completed!")
        threading.Timer(600, delete_converted_video, args=(output_file,)).start()
        return output_file

    except (FileNotFoundError, TypeError, ValueError, OSError) as e:
        print(f"Error occurred during conversion: {e}")


def convert_video_to_frames(input_file, output_folder, image_format):
    print("Converting...")
    clip = VideoFileClip(input_file)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, frame in enumerate(clip.iter_frames()):
        output_file = os.path.join(output_folder, f"frame_{i:04d}.{image_format}")
        frame_image = Image.fromarray(frame)  
        frame_image.save(output_file)
        
        
def delete_converted_video(path):
    try:
        os.remove(path)
        print(f"Deleted {path}")
    except Exception as e:
        print(f"Error deleting {path}: {e}")
