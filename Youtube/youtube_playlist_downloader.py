from pytube import Playlist, YouTube
import os


def download_playlist(playlist_url, download_audio):
    try:
        playlist = Playlist(playlist_url)
        output_path = input("Enter the output directory path (leave blank for current directory): ").strip()
        if not output_path:
            output_path = os.getcwd()

        for video_url in playlist.video_urls:
            if download_audio:
                download_audio_from_video(video_url, output_path)
            else:
                download_video(video_url, output_path)

    except Exception as e:
        print(f"An error occurred: {e}")


def download_audio_from_video(video_url, output_path):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(only_audio=True).first()

        if stream:
            print(f"Downloading audio from video '{yt.title}'...")
            stream.download(output_path=output_path, filename=f"{yt.title}.mp3")
            print(f"Download of audio from '{yt.title}' complete.")
        else:
            print(f"No audio available for '{yt.title}'.")

    except Exception as e:
        print(f"An error occurred while downloading audio from '{video_url}': {e}")


def download_video(video_url, output_path):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc().first()

        if stream:
            print(f"Downloading video '{yt.title}'...")
            stream.download(output_path=output_path)
            print(f"Download of video '{yt.title}' complete.")
        else:
            print(f"No video available for '{yt.title}'.")

    except Exception as e:
        print(f"An error occurred while downloading video '{video_url}': {e}")


if __name__ == "__main__":
    playlist_url = input("Enter YouTube playlist URL: ").strip()
    download_audio = input("Do you want to download audio only? (y/n): ").strip().lower()

    if download_audio == 'y':
        download_audio = True
    else:
        download_audio = False

    download_playlist(playlist_url, download_audio)
