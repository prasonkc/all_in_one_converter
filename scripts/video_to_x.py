from PIL import Image
from moviepy.editor import VideoFileClip
import os
import time, threading
import zipfile
import shutil

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
        threading.Timer(600, delete_converted, args=(output_file,)).start()
        return output_file

    except (FileNotFoundError, TypeError, ValueError, OSError) as e:
        print(f"Error occurred during conversion: {e}")


def convert_video_to_frames(input_file, image_format):
    
    if not os.path.isfile(input_file):
        raise FileNotFoundError('Input file does not exist.')
    
    filename = input_file[7:].split(".")[0]
    try:
        os.makedirs(CONVERTED_DIR, exist_ok=True)
        
        # input path = ./temp/ ie 7 letters
        print(filename)
        
        clip = VideoFileClip(input_file)

        output_folder = f"{CONVERTED_DIR}/frames"

        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        frames = []
        for i, frame in enumerate(clip.iter_frames()):
            output_file = os.path.join(output_folder, f"frame_{i:04d}.{image_format}")
            frame_image = Image.fromarray(frame)
            frame_image.save(output_file)
            frames.append(output_file)
            
        zip_filename = os.path.join(CONVERTED_DIR, 'frames.zip')
        
        with zipfile.ZipFile(zip_filename, 'w') as zipf:
            for frame_file in frames:
                zipf.write(frame_file, os.path.basename(frame_file))
                
        shutil.rmtree(output_folder)

        print("Conversion Complete!")
        threading.Timer(600, delete_converted, args=(zip_filename,)).start()
        return zip_filename

    except (FileNotFoundError, TypeError, ValueError, OSError) as e:
        print(f"Error occurred during conversion: {e}")

        
def delete_converted(path):
    try:
        os.remove(path)
        print(f"Deleted {path}")
    except Exception as e:
        print(f"Error deleting {path}: {e}")
