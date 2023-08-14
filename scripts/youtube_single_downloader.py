import os
from pytube import YouTube
import threading

output_dir = "./downloads"


def download_ytVideo(url, resolution):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the stream for the specified resolution
        stream = yt.streams.filter(res=resolution, file_extension="mp4").first()
        filename = f"{yt.title}.mp4"
        output_file = os.path.join(output_dir, filename)

        if stream:
            # Download the video
            print(f"Downloading '{yt.title}' in {resolution}...")
            stream.download(output_path=output_dir)

            print(f"Download of '{yt.title}' in {resolution} complete. Saved as '{output_file}'")
            threading.Timer(600, delete_file, args=(output_file,)).start()
        else:
            print(f"No {resolution} video available for '{yt.title}'.")
            return None, None

        return output_dir, filename
    except Exception as e:
        print(f"An error occurred while downloading '{url}': {e}")
        return None, None


def delete_file(path):
    try:
        os.remove(path)
        print(f"Deleted {path}")
    except Exception as e:
        print(f"Error deleting {path}: {e}")
