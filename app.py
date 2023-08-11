from flask import Flask, request, render_template, jsonify
from scripts.video_converter import convert_video_to_video
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
        video_data = request.files.get("video") 
        selected_format = "." + request.form.get("format")
        video_filename = video_data.filename


        if video_data:
            # create temporary video file
            temp_video_path = "./temp/" + video_filename
            video_data.save(temp_video_path)
            # Convert the video
            print("Now converting....")

            converted_file_path = convert_video_to_video(temp_video_path, selected_format)

            if converted_file_path:
                # Clean up the temporary video file
                os.remove(temp_video_path)
                
            video_filename = converted_file_path.split("/")[-1]
            return jsonify(video_filename = video_filename, converted_file_path = converted_file_path)
        
        else:
            return jsonify(error="No File Selected"), 400


if __name__ == '__main__':
    app.run()
