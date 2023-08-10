from moviepy.editor import VideoFileClip
from moviepy.editor import *
import os
import time
import threading

CONVERTED_DIR = "../converted"


def convert_video_to_video(input_file, output_format):
    valid_codecs = {
        ".mp4": ("libx264", "aac"),
        ".avi": ("libx264", "aac"),
        ".webm": ("libvpx", "libvorbis"),
        ".mkv": ("libx264", "aac"),
        ".mov": ("libx264", "aac"),
        ".flv": ("libx264", "aac"),
        ".wmv": ("wmv2", "wmav2"),
        ".m4v": ("libx264", "aac"),
        ".3gp": ("libx264", "aac"),
        ".ogv": ("libtheora", "libvorbis"),
        ".webp": ("libwebp", "libvorbis"),
        ".divx": ("mpeg4", "mp3"),
        ".ts": ("mpeg2video", "mp2"),
        ".vob": ("mpeg2video", "mp2"),
        # Add more formats and codecs as needed
    }

    try:
        if output_format not in valid_codecs:
            raise ValueError(
                f"Unsupported output format: {output_format}. Valid formats are: {list(valid_codecs.keys())}")

        if not os.path.isfile(input_file):
            raise FileNotFoundError(f"Input file {input_file} does not exist.")

        video = VideoFileClip(input_file)
        video_codec, audio_codec = valid_codecs[output_format]

        os.makedirs(CONVERTED_DIR, exist_ok=True)

        filename = input_file.split(".")[0]

        timestamp = int(time.time())
        output_filename = f"{filename}_converted_{timestamp}{output_format}"
        output_file = os.path.join(CONVERTED_DIR, output_filename)

        video.write_videofile(output_file, codec=video_codec, audio_codec=audio_codec, preset='ultrafast')

        # threading.Timer(3600, delete_converted_video, args=(output_file,)).start()

    except ValueError as ve:
        print(f"ValueError during conversion: {ve}")
        return False
    except FileNotFoundError as fnfe:
        print(f"FileNotFoundError during conversion: {fnfe}")
        return False
    except Exception as e:
        print(f"Error during conversion: {e}")
        return False
    finally:
        video.close()

    print("Conversion completed!")
    return output_file


# def delete_converted_video(path):
#     try:
#         os.remove(path)
#         print(f"Deleted {path}")
#     except Exception as e:
#         print(f"Error deleting {path}: {e}")
