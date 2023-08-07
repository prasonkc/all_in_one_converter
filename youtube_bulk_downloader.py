from pytube import YouTube
import os

# audio might not work with 1080p. Use 720p to preserve both video and audio
def show_available_resolutions(video_url):
    try:
        yt = YouTube(video_url)
        available_resolutions = [stream.resolution for stream in yt.streams.filter(file_extension="mp4")]
        print(f"Available video resolutions for '{yt.title}':")
        for resolution in available_resolutions:
            print(resolution)
        return available_resolutions
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def download_video(video_url, resolution, output_path):
    try:
        yt = YouTube(video_url)
        if yt.age_restricted:
            print("Sorry, age-restricted videos not available.")
            return

        stream = yt.streams.filter(file_extension="mp4", resolution=resolution).first()

        if stream:
            print(f"Downloading video '{yt.title}' in {resolution}...")
            stream.download(output_path=output_path)
            print(f"Download of '{yt.title}' complete.")
        else:
            print(f"Selected resolution '{resolution}' is not available for '{yt.title}'.")
            available_resolutions = show_available_resolutions(video_url)
            while True:
                new_resolution = input("Please enter a valid resolution from the list above: ").strip()
                if new_resolution in available_resolutions:
                    download_video(video_url, new_resolution, output_path)
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

    selected_resolution = input("Enter desired video resolution for bulk download: ").strip()
    for url in urls:
        download_video(url, selected_resolution, output_path)


if __name__ == "__main__":
    bulk_download()
