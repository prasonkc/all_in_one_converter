from typing import Union
from PIL import Image
import os


def convert_image(input_file: str, output_file: str, output_format: str) -> Union[str, None]:
    try:
        img = Image.open(input_file)

        # Convert the image to 'RGB' mode to support JPEG format
        img = img.convert('RGB')

        output_file_with_extension = f"{output_file}.{output_format}"
        img.save(output_file_with_extension)
        print(f"Image converted successfully and saved to: {output_file_with_extension}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    input_file = input("Enter the path of the input image: ")
    output_file = input("Enter the path where you want to save the converted image (without extension): ")
    output_format = input("Enter the desired output format (e.g., PNG, JPEG, GIF, BMP): ").lower()

    if output_format not in ('png', 'jpg', 'jpeg', 'gif', 'bmp'):
        print("Invalid output format. Supported formats: PNG, JPEG, GIF, BMP")
    else:
        convert_image(input_file, output_file, output_format)
