from pytube import YouTube
import os


# Function to dynamically show available video formats and resolutions for a given video URL
def show_available_formats_and_resolutions(url):
    try:
        yt = YouTube(url)
        available_formats_and_resolutions = []

        for stream in yt.streams.filter(file_extension="mp4"):
            resolution = stream.resolution
            audio_info = "YES" if stream.includes_audio_track else "NO"
            format_info = stream.mime_type.split('/')[1]
            available_formats_and_resolutions.append((resolution, format_info, audio_info))

        print("Available video resolutions and formats:")
        for resolution, format_info, audio_info in available_formats_and_resolutions:
            print(f"{resolution} {format_info.upper()} (Audio: {audio_info})")

        return available_formats_and_resolutions

    except Exception as e:
        print(f"An error occurred: {e}")
        return []


# Function for downloading a single video
def download_single_video(url):
    available_formats_and_resolutions = show_available_formats_and_resolutions(url)
    if not available_formats_and_resolutions:
        return

    print("To Ensure both audio and video works properly and there are no errors, it is recommended "
          "to download 720p in mp4 format")
    resolution = input("Enter desired video resolution: ").strip()

    if resolution not in [res for res, _, _ in available_formats_and_resolutions]:
        print("Selected resolution is not available.")
        return

    video_format = input("Enter desired video format (e.g., mp4, mkv): ").strip().lower()
    if not video_format:
        video_format = "mp4"
    else:
        video_format = video_format.lower()

    output_path = input("Enter the output directory path (leave blank for current directory): ").strip()
    if not output_path:
        output_path = os.getcwd()

    try:
        yt = YouTube(url)
        if yt.age_restricted:
            print("Sorry, we do not support age-restricted downloads.")
            return

        stream = yt.streams.filter(res=resolution, file_extension=video_format).first()
        if stream:
            print(f"Downloading video '{yt.title}' in {resolution} and {video_format.upper()}...")
            stream.download(output_path=output_path)
            print(f"Download of '{yt.title}' complete.")
        else:
            print(f"No video available in {resolution} and {video_format.upper()} for '{yt.title}'.")
    except Exception as e:
        print(f"An error occurred while downloading '{url}': {e}")


if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ").strip()
    download_single_video(video_url)
