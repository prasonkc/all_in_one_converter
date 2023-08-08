from pytube import YouTube
import os


def show_available_formats_and_resolutions(url):
    try:
        yt = YouTube(url)
        available_formats_and_resolutions = []

        for stream in yt.streams.filter(file_extension="mp4"):
            resolution = stream.resolution
            audio_info = "YES" if stream.includes_audio_track else "NO"
            format_info = stream.mime_type.split('/')[1]
            available_formats_and_resolutions.append((resolution, format_info, audio_info))

        return available_formats_and_resolutions

    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def download_video(video_url, resolution, output_path, video_format):
    try:
        yt = YouTube(video_url)

        stream = yt.streams.filter(file_extension=video_format, resolution=resolution).first()

        if stream:
            print(f"Downloading video '{yt.title}' in {resolution} and {video_format.upper()}...")
            stream.download(output_path=output_path)
            print(f"Download of '{yt.title}' complete.")
        else:
            print(f"Selected resolution '{resolution}' is not available for '{yt.title}'.")
            available_resolutions = []
            print("Available video resolutions and formats:")
            for resolution, format_info, audio_info in show_available_formats_and_resolutions(video_url):
                print(f"{resolution} {format_info.upper()} (Audio: {audio_info})")
                available_resolutions.append(resolution)

            while True:
                new_resolution = input("Please enter a valid resolution from the list above: ").strip()
                new_video_format = input("Please enter a valid file format from the list above: ").strip()
                if new_resolution in available_resolutions:
                    download_video(video_url, new_resolution, output_path, new_video_format)
                    break
                else:
                    print("Invalid resolution. Please enter a valid resolution.")

    except Exception as e:
        print(f"An error occurred while downloading '{video_url}': {e}")


def bulk_download():
    urls = []
    while True:
        url = input("Enter YouTube video URL (or 'download' to start download): ").strip()
        if url.lower() == 'download':
            break
        urls.append(url)

    if not urls:
        print("No video URLs provided.")
        return

    output_path = input("Enter the output directory path (leave blank for current directory): ").strip()
    if not output_path:
        output_path = os.getcwd()

    print("To ensure both audio and video work properly and there are no errors, it is recommended "
          "to download 720p in mp4 format (mp4 automatically selected)")
    selected_resolution = input("Enter desired video resolution for bulk download: ").strip()

    video_format = input("Enter desired video format (e.g., mp4, mkv): ").strip().lower()
    if not video_format:
        video_format = "mp4"

    for url in urls:
        download_video(url, selected_resolution, output_path, video_format)


if __name__ == "__main__":
    bulk_download()
