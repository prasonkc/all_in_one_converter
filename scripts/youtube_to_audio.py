import os
from pytube import YouTube
from pydub import AudioSegment
import threading

output_dir = "./downloads"


def download_ytAudio(video_url, bitrate='192k'):
    try:
        yt = YouTube(video_url)
        audio_streams = yt.streams.filter(only_audio=True)
        filename = f"{yt.title}.mp3"

        if not audio_streams:
            print(f"No audio streams available for '{yt.title}'.")
            return

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        print(f"Downloading audio from '{yt.title}'...")
        audio_stream = audio_streams.first()
        audio_file_path = os.path.join(output_dir, filename)
        audio_stream.download(output_path=output_dir, filename=filename)

        # Convert to desired audio format and bitrate using pydub
        audio = AudioSegment.from_file(audio_file_path)
        audio.export(audio_file_path, bitrate=bitrate)

        print(f"Download and conversion of '{yt.title}' complete.")
        threading.Timer(600, delete_file, args=(audio_file_path,)).start()
        return output_dir, filename
    except Exception as e:
        print(f"An error occurred while downloading audio: {e}")


def delete_file(path):
    try:
        os.remove(path)
        print(f"Deleted {path}")
    except Exception as e:
        print(f"Error deleting {path}: {e}")