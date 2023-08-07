from pydub import AudioSegment
import os

def convert_audio(input_file, output_file, output_format, bitrate='192k'):
    """
    Convert audio file to a different format.

    Args:
        input_file (str): Path to the input audio file.
        output_file (str): Path to the output audio file.
        output_format (str): Desired output format.
        bitrate (str, optional): Bitrate for the output audio file. Defaults to '192k'.

    Raises:
        FileNotFoundError: If the input file does not exist.
        ValueError: If the output format is not supported.
        TypeError: If any of the input parameters are of incorrect type.

    Returns:
        None
    """
    if not isinstance(input_file, str):
        raise TypeError('input_file must be a string')
    if not isinstance(output_file, str):
        raise TypeError('output_file must be a string')
    if not isinstance(output_format, str):
        raise TypeError('output_format must be a string')
    if not isinstance(bitrate, str):
        raise TypeError('Bitrate must be a string')

    if not os.path.isfile(input_file):
        raise FileNotFoundError('Input file does not exist.')

    try:
        audio = AudioSegment.from_file(input_file)
        converted_audio = audio.export(output_file, format=output_format, bitrate=bitrate)
        converted_audio.close()
        print("Conversion completed!")
    except (FileNotFoundError, TypeError, ValueError, OSError) as e:
        print(f"Error occurred during conversion: {e}")

if __name__ == "__main__":
    input_file = input("Enter the path of the input audio file: ")
    output_format = input("Enter the desired output audio format (e.g., .mp3, .wav, .ogg, etc.): ").replace(".", "")
    output_file = input("Enter the desired path of the output audio file: ")

    # You can adjust the bitrate based on your quality and size preferences.
    # Available options: '192k', '256k', '320k', '128k', etc.
    bitrate = input("Enter the desired bitrate (e.g., 192k, 256k, 320k, etc.): ")

    convert_audio(input_file, output_file, output_format, bitrate)
