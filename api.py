import os
from flask import Flask, request, session, send_file, render_template
from werkzeug.utils import secure_filename
import audio_video_handler
import pathlib
from pathlib import Path

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY']="abcdefg"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/language', methods=['POST'])
def translate_text():
    try:
        selected_language = request.form.get('language')
        if selected_language in ['en', 'hi']:  # Add more languages as needed
            session['selected_language'] = selected_language
            return "Language selected successfully"
        else:
            return "Invalid language selected", 400
    except KeyError:
        return "No language selected", 400

@app.route('/upload_video', methods=['POST'])
def upload_video():
    try:
        media_folder = "PAGO/sample_data"
        if not os.path.exists(media_folder):
            os.makedirs(media_folder)
        file = request.files['videoFile']
        filename = secure_filename(file.filename)
        extension = pathlib.Path(filename).suffix
        filename = 'uploaded' + extension
        destination = "/".join([media_folder, filename])
        file.save(destination)
        return 'Video uploaded successfully'
    except Exception as e:
        return f'Error occurred: {e}', 500


@app.route('/generate', methods=['POST'])
def generate_result():
    try:
        print("covnerting video .. ")
        selected_language = session.get('selected_language')  # Get selected language from session
        if not selected_language:
            return "Language not selected. Please select a language first.", 400
        else:
            print( "Language selected")
        # Assuming convert_video accepts the language as an argument
        audio_video_handler.convert_video(language=selected_language)
        print("conversion .. completed .. ")
        return render_template('index.html', show_download=True)
    except Exception as e:
        return f'Error occurred: {e}', 500

@app.route('/download_generated_video', methods=['GET'])
def get_generated_video():
    output_video_path ="PAGO/converted_videos/output.mp4" # Replace this with the actual path of the generated video
    try:
        return send_file(output_video_path, as_attachment=True)
    except:
        return "Generated video file not found!", 404

if __name__ == '__main__':
    app.run(debug=True, port=500)





