from flask import Flask, request, render_template, jsonify
from scripts.video_converter import convert_video_to_video
import base64
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    print("Loaded")
    return render_template("index.html")


@app.route('/video_to_video_converter', methods=["GET", "POST"])
def video_to_video_converter():
    if request.method == "GET":
        print("Get Method loaded")
        return render_template("videos_converter/video_to_video.html")
    else:
        print("Post method loaded")
        video_data = request.files.get("video")  # Access uploaded file using request.files
        selected_format = "." + request.form.get("format")  # Get the selected format from the form
        print(video_data)
        print(format)

        if video_data:
            # create temporary video file
            temp_video_path = "temp_video" + selected_format
            video_data.save(temp_video_path)
            # Convert the video
            print("Now converting....")

            converted_file_path = convert_video_to_video(temp_video_path, selected_format)

            if converted_file_path:
                # Clean up the temporary video file
                os.remove(temp_video_path)

            return jsonify(converted_file_path)
        else:
            return jsonify(error="No File Selected"), 400


if __name__ == '__main__':
    app.run()
