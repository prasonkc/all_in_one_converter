import os
from pytube import YouTube
from pydub import AudioSegment


def download_ytAudio(video_url, output_path, audio_format='mp3', bitrate='192k'):
    try:
        yt = YouTube(video_url)
        audio_streams = yt.streams.filter(only_audio=True)

        if not audio_streams:
            print(f"No audio streams available for '{yt.title}'.")
            return

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        print(f"Downloading audio from '{yt.title}'...")
        audio_stream = audio_streams.first()
        audio_file_path = os.path.join(output_path, f"{yt.title}.{audio_format}")
        audio_stream.download(output_path=output_path, filename=f"{yt.title}.{audio_format}")

        # Convert to desired audio format and bitrate using pydub
        audio = AudioSegment.from_file(audio_file_path)
        audio.export(audio_file_path, format=audio_format, bitrate=bitrate)

        print(f"Download and conversion of '{yt.title}' complete.")
    except Exception as e:
        print(f"An error occurred while downloading audio: {e}")


def main():
    video_urls = []
    while True:
        url = input("Enter YouTube video URL (or 'download' to start download): ").strip()
        if url.lower() == 'download':
            break
        video_urls.append(url)

    if not video_urls:
        print("No video URLs provided.")
        return

    output_path = input("Enter the output directory path (leave blank for current directory): ").strip()
    if not output_path:
        output_path = os.getcwd()

    audio_format = input("Enter desired audio format (e.g., mp3, m4a): ").strip().lower()
    if not audio_format:
        audio_format = 'mp3'

    bitrate = input("Enter desired bitrate (e.g., 192k): ").strip().lower()
    if not bitrate:
        bitrate = '192k'

    for url in video_urls:
        download_audio(url, output_path, audio_format, bitrate)


if __name__ == "__main__":
    main()

