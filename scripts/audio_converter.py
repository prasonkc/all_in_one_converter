from pydub import AudioSegment
import os
import threading
import time

CONVERTED_DIR = "./converted"

def convert_video_to_audio(input_file, output_format):

    if not os.path.isfile(input_file):
        raise FileNotFoundError('Input file does not exist.')

    try:

        os.makedirs(CONVERTED_DIR, exist_ok=True)
        
        filename = input_file[7:].split(".")[0]
        # input path = ./temp/ ie 7 letters
        print(filename)

        timestamp = int(time.time())
        output_filename = f"{filename}_converted_{timestamp}.{output_format}"
        output_file = os.path.join(CONVERTED_DIR, output_filename)
        
        audio = AudioSegment.from_file(input_file)
        converted_audio = audio.export(output_file, format=output_format)
        converted_audio.close()
        
        print("Conversion completed!")
        threading.Timer(600, delete_converted_audio, args=(output_file,)).start()
        return output_file

    except (FileNotFoundError, TypeError, ValueError, OSError) as e:
        print(f"Error occurred during conversion: {e}")

def delete_converted_audio(path):
    try:
        os.remove(path)
        print(f"Deleted {path}")
    except Exception as e:
        print(f"Error deleting {path}: {e}")
