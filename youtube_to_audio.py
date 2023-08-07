from pytube import YouTube
import os


def download_audio(url, audio_format):
    try:
        yt = YouTube(url)

        if yt.age_restricted:
            print("Sorry, we do not support age-restricted video downloads.")
            return

        audio_stream = yt.streams.filter(only_audio=True, file_extension=audio_format).first()
        if not audio_stream:
            print(f"No audio available in {audio_format.upper()} format for '{yt.title}'.")
            return

        output_path = input("Enter the output directory path (leave blank for current directory): ").strip()
        if not output_path:
            output_path = os.getcwd()

        print(f"Downloading audio from '{yt.title}' in the best available quality...")
        audio_stream.download(output_path=output_path)
        downloaded_file_path = os.path.join(output_path, audio_stream.default_filename)

        print("Audio download complete.")

        convert_audio_bitrate(downloaded_file_path, audio_format)

    except Exception as e:
        print(f"An error occurred while downloading audio from '{url}': {e}")


def convert_audio_bitrate(input_file, audio_format):
    try:
        desired_bitrate = input("Enter desired audio bitrate (e.g., 64k, 128k, 192k, 256k, 320k): ").strip().lower()
        if not desired_bitrate:
            print("No bitrate entered. Audio will not be converted.")
            return

        output_file_path = os.path.splitext(input_file)[0] + f"_{desired_bitrate}.{audio_format}"
        command = f"ffmpeg -i {input_file} -b:a {desired_bitrate} {output_file_path}"

        os.system(command)

        print(f"Audio bitrate conversion complete. Saved as: {output_file_path}")

    except Exception as e:
        print(f"An error occurred while converting audio: {e}")


if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ").strip()
    audio_format = input("Enter desired audio format (e.g., mp3, m4a, webm): ").strip().lower()

    if not audio_format:
        audio_format = "mp3"

    download_audio(video_url, audio_format)
