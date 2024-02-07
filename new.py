import os
import subprocess
from base64 import b64encode
import moviepy.editor as mp
import cv2

def get_video_resolution(video_path):
    """Function to get the resolution of a video"""
    
    video = cv2.VideoCapture(video_path)
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    return (width, height)

def resize_video(video_path, new_resolution):
    """Function to resize a video"""
   
    video = cv2.VideoCapture(video_path)
    fourcc = int(video.get(cv2.CAP_PROP_FOURCC))
    fps = video.get(cv2.CAP_PROP_FPS)
    width, height = new_resolution
    output_path = os.path.splitext(video_path)[0] + '_720p.mp4'
    writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    while True:
        success, frame = video.read()
        if not success:
            break
        resized_frame = cv2.resize(frame, new_resolution)
        writer.write(resized_frame)
    video.release()
    writer.release()

def convert(PATH_TO_YOUR_VIDEO):
    video_duration = mp.VideoFileClip(PATH_TO_YOUR_VIDEO).duration
    if video_duration > 360:
        print("WARNING: Video duration exceeds 60 seconds. Please upload a shorter video.")
        raise SystemExit(0)

    output_file_path =  "D:/PAGO/converted_videos/output.mp4"
    video_resolution = get_video_resolution(PATH_TO_YOUR_VIDEO)
    print(f"Video resolution: {video_resolution}")
    if video_resolution[0] >= 1920 or video_resolution[1] >= 1080:
        print("Resizing video to 720p...")
        subprocess.run(['ffmpeg', '-i', PATH_TO_YOUR_VIDEO, '-vf', 'scale=1280:360', output_file_path])
        print("Video resized to 720p")
    else:
        print("No resizing needed")

    #     os.system(f"ffmpeg -i {PATH_TO_YOUR_VIDEO} -vf scale=1280:360 D:/PAGO/sample_data/uploaded.mp4")
    #     PATH_TO_YOUR_VIDEO = "D:/PAGO/sample_data/uploaded.mp4"
    #     print("Video resized to 720p")
    # else:
    #     print("No resizing needed")
    
    
    
    pad_top =  0
    pad_bottom =  10
    pad_left =  0
    pad_right =  0
    rescaleFactor =  1
    nosmooth = True 

    use_hd_model = False 
    checkpoint_path = 'checkpoints/wav2lip.pth' if not use_hd_model else 'checkpoints/wav2lip_gan.pth'

    if nosmooth == False:
        command = f"python inference.py --checkpoint_path {checkpoint_path} --face '..D:/PAGO/sample_data/uploaded.mp4' --audio '..D:/PAGO/translated_audio/translated.wav' --pads {pad_top} {pad_bottom} {pad_left} {pad_right} --resize_factor {rescaleFactor}"
    else:
        command = f"python inference.py --checkpoint_path {checkpoint_path} --face '..D:/PAGO/sample_data/uploaded.mp4' --audio '..D:/PAGO/translated_audio/translated.wav' --pads {pad_top} {pad_bottom} {pad_left} {pad_right} --resize_factor {rescaleFactor} --nosmooth"

    subprocess.run(command, shell=True)
   
    #Preview output video
    if os.path.exists(output_file_path):
        print("Final Video Preview")
        print("Download this video from", output_file_path)
    else:
        print("Processing failed. Output video not found.")