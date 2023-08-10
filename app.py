from flask import Flask,request, render_template, jsonify
from scripts.video_converter import convert_video_to_video

app = Flask(__name__)


@app.route('/')
def hello_world():
    print("Loaded")
    return render_template("index.html")

@app.route('/video_to_video_converter', methods = ["GET", "POST"])
def video_to_video_converter():
    if request.method == "GET":
        print("Get Method loaded")
        return render_template("videos_converter/video_to_video.html")
    else:
        print("Post method loaded")
        video_data = request.data
        format = "." + request.headers.get("X-File-Name", "mp4") 
        print(video_data)
        
        if video_data:
            if video_data.filename:
                # Convert the video
                print("Now converting....")
                converted_video = convert_video_to_video(video_data, format)
                print("conversion complete...")
                return jsonify(message="Video converted successfully")
        else:
            print("Not Ok")
            return jsonify(error="No File Selected"), 400
        
if __name__ == '__main__':
    app.run()
