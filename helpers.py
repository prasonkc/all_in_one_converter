import os

def save_and_convert_video(video_data, selected_format, converter_function):
    video_filename = video_data.filename
    # create temporary video file
    temp_video_path = "./temp/" + video_filename
    video_data.save(temp_video_path)
    # Convert the video
    print("Now converting....")

    converted_file_path = converter_function(temp_video_path, selected_format)

    if converted_file_path:
        # Clean up the temporary video file
        os.remove(temp_video_path)
        
    video_filename = converted_file_path.split("/")[-1]
    return converted_file_path, video_filename



    