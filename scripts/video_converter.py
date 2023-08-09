from moviepy.editor import VideoFileClip
from moviepy.editor import *
import os


def convert_video(input_file, output_file, output_format):
    """
    Args:
        input_file: The file path of the video to be converted.
        output_file: The file path of the converted video.
        output_format: The format of the output video file.

    Returns:
        True if the conversion was successful, False otherwise.
    """

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
        ".mov": ("prores", "pcm_s16le"),
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

        output_dir = os.path.dirname(output_file)
        os.makedirs(output_dir, exist_ok=True)

        video.write_videofile(output_file, codec=video_codec, audio_codec=audio_codec, preset='ultrafast')
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
    return True


if __name__ == "__main__":
    input_file = input("Enter the path of the input video file: ")
    output_format = input("Enter the desired output video format (e.g., .mp4, .avi, .webm, etc.): ")
    output_file = input("Enter the desired path of the output video file: ")

    convert_video(input_file, output_file, output_format)
