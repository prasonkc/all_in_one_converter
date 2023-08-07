from pytube import YouTube
import os

# Function to dynamically show available video resolutions for a given video URL
def show_available_resolutions(url):
    try:
        yt = YouTube(url)
        available_resolutions = [stream.resolution for stream in yt.streams.filter(file_extension="mp4")]
        print("Available video resolutions:")
        for resolution in available_resolutions:
            print(resolution)
        return available_resolutions
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


# Function for downloading a single video
def download_single_video(url):
    available_resolutions = show_available_resolutions(url)
    if not available_resolutions:
        return

    resolution = input("Enter desired video resolution: ").strip()

    if resolution not in available_resolutions:
        print("Selected resolution is not available.")
        return

    if resolution == "1080p":
        confirm = input("Audio cannot be guaranteed to preserve in 1080p. Please use 720p to ensure both audio and video are preserved. Do you still wish to continue? (y/n): ").strip().lower()
        if confirm != "y":
            print("Download cancelled.")
            return

    output_path = input("Enter the output directory path (leave blank for current directory): ").strip()
    if not output_path:
        output_path = os.getcwd()

    try:
        yt = YouTube(url)
        if yt.age_restricted:
            print("Sorry, we do not support age-restricted downloads.")
            return
        stream = yt.streams.filter(file_extension="mp4", resolution=resolution).first()
        if stream:
            print(f"Downloading video '{yt.title}' in {resolution}...")
            stream.download(output_path=output_path)
            print(f"Download of '{yt.title}' complete.")
        else:
            print(f"No video available in {resolution} for '{yt.title}'.")
    except Exception as e:
        print(f"An error occurred while downloading '{url}': {e}")


if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ").strip()
    download_single_video(video_url)
