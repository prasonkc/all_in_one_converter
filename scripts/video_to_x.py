from PIL import Image
from moviepy.editor import VideoFileClip
import os


def convert_to_gif(input_file, output_file):
    print("Converting...")
    clip = VideoFileClip(input_file)
    clip.write_gif(output_file, fps=10)


def extract_audio(input_file, output_file, audio_format):
    print("Converting...")
    clip = VideoFileClip(input_file)
    audio = clip.audio
    audio.write_audiofile(output_file, codec=audio_format)


def convert_to_frames(input_file, output_folder, image_format):
    print("Converting...")
    clip = VideoFileClip(input_file)

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, frame in enumerate(clip.iter_frames()):
        output_file = os.path.join(output_folder, f"frame_{i:04d}.{image_format}")
        frame_image = Image.fromarray(frame)  # Assuming you have PIL (Python Imaging Library) installed
        frame_image.save(output_file)


if __name__ == "__main__":
    print("1. Convert video to GIF")
    print("2. Extract audio from video")
    print("3. Convert video to frames (pictures)")

    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
        input_file = input("Enter the path of the input video file: ")
        output_file = input("Enter the path for the output GIF file: ")
        convert_to_gif(input_file, output_file)
        print("Conversion to GIF complete.")

    elif choice == "2":
        input_file = input("Enter the path of the input video file: ")
        output_file = input("Enter the path for the output audio file: ")
        audio_format = input("Enter the desired audio format (e.g., mp3, wav): ")
        extract_audio(input_file, output_file, audio_format)
        print("Audio extraction complete.")

    elif choice == "3":
        input_file = input("Enter the path of the input video file: ")
        output_folder = input("Enter the folder path to save frames (pictures): ")
        image_format = input("Enter the desired image format (e.g., png, jpg): ")
        convert_to_frames(input_file, output_folder, image_format)
        print("Conversion to frames complete.")

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
