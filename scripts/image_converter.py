from typing import Union
from PIL import Image
import os
import threading
import time

CONVERTED_DIR = "./converted"

def convert_image_to_image(input_file: str, output_format: str) -> Union[str, None]:
    try:
        img = Image.open(input_file)

        # Convert the image to 'RGB' mode to support JPEG format
        img = img.convert('RGB')

        filename = input_file[7:].split(".")[0] 
        # input path = ./temp/ ie 7 letters

        timestamp = int(time.time())
        output_filename = f"{filename}_converted_{timestamp}{output_format}"
        output_file = os.path.join(CONVERTED_DIR, output_filename)

        img.save(output_file)
        print(f"Image converted successfully and saved to: {output_file}")
        threading.Timer(6, delete_converted_image, args=(output_file,)).start()
        return output_file

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

def delete_converted_image(path):
    try:
        os.remove(path)
        print(f"Deleted {path}")
    except Exception as e:
        print(f"Error deleting {path}: {e}")
