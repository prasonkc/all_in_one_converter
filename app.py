from flask import Flask, request, render_template, jsonify, send_from_directory
from scripts.video_converter import convert_video_to_video
from scripts.audio_converter import convert_video_to_audio
from scripts.video_to_x import convert_video_to_frames, convert_video_to_gif
from helpers import save_and_convert_video
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    print("Loaded")
    return render_template("index.html")


@app.route('/video_to_video_converter', methods=["GET", "POST"])
def video_to_video_converter():
    if request.method == "GET":
        return render_template("videos_converter/video_to_video.html")
    else:
        video_data = request.files.get("video") 
        selected_format = "." + request.form.get("format")

        if video_data:
            converted_file_path, filename = save_and_convert_video(video_data, selected_format, convert_video_to_video)
            return jsonify(filename = filename, converted_file_path = converted_file_path)
        
        else:
            return jsonify(error="No File Selected"), 400
        
        
@app.route('/video_to_audio_converter',methods=["GET", "POST"])
def video_to_audio_converter():
    if request.method == "GET":
        return render_template("videos_converter/video_to_audio.html")
    else:
        video_data = request.files.get("video")
        selected_format = request.form.get("format")
       
        if video_data:
            converted_file_path, filename = save_and_convert_video(video_data, selected_format, convert_video_to_audio)
            return jsonify(filename = filename, converted_file_path = converted_file_path)
        
        else:
            return jsonify(error="No File Selected"), 400

        
@app.route('/video_to_gif_converter', methods = ["GET", "POST"])
def video_to_gif_converter():
    if request.method == "GET":
        return render_template("videos_converter/video_to_gif.html")
    else:
        video_data = request.files.get("video")
        format = request.form.get("format")
        
        if video_data:
            converted_file_path, filename = save_and_convert_video(video_data, format, convert_video_to_gif)
            
            return jsonify(converted_file_path = converted_file_path, filename = filename)
        
@app.route('/video_to_frames_converter', methods = ["GET", "POST"])
def video_to_frames_converter():
    if request.method == "GET":
        return render_template("videos_converter/video_to_frames.html")
    else:
        video_data = request.files.get("video")
        format = request.form.get("format")
        
        if video_data:
            converted_file_path, filename = save_and_convert_video(video_data, format, convert_video_to_frames)
            
            return jsonify(converted_file_path = converted_file_path, filename = filename)
        
    
@app.route('/converted/<path:filename>')
def download_converted_video(filename):
    converted_dir = os.path.join(os.getcwd(), 'converted')
    file_path = os.path.join(converted_dir, filename) 
    response = send_from_directory(converted_dir, filename)

    os.remove(file_path)
    return response

if __name__ == '__main__':
    app.run()
