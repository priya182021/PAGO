import inference
import extract_audio_from_video
import audio_translation
import automated_transcription_script
import os
import inference

CHECKPOINT_PATH = "D:/PAGO/Wav2Lip/checkpoints/wav2lip_gan.pth"
FINAL_OUTPUT_DIRECTOR = "D:/PAGO/converted_videos/output.mp4"
OUTPUT_TRANSLATED_AUDIO_LOCATION = "D:/PAGO/translated_audio/translated.wav"
OUTPUT_AUDIO_FILE_LOCATION="D:/PAGO/extracted_audio"
DEFAULT_VIDEO_FILE ="D:/PAGO/sample_data/uploaded.mp4"
DEFAULT_VIDEO_FILE_NAME ="video"
DEFAULT_LANGAUGE = "English"
DEFAULT_IMAGE_FILE= "D:/PAGO/sample_data/uploaded.jpg"

def get_conversions(audio_file, video_file, file_name, final_output_directory):
    try:
            checkpoint_path = CHECKPOINT_PATH
            print("checkpooint")
            inference.get_conversion(audio_file, video_file,  file_name,  checkpoint_path, final_output_directory)
    except Exception as e:
        print("Exception has occured.. get_conversion")
        print(e)
        return False
    return True

def find_language_code(language):
    langcode_audio = {
                      'en': 'en-EN',
                      'hi': 'hi-IN',
                      'hi_female': 'hi-IN'
                      }
    voice_name = {

        'hi': 'hi-IN-Standard-B',
        'hi_female': 'hi-IN-Standard-A'
    }
    return langcode_audio[language], voice_name[language]

def convert_video(language,video_file=DEFAULT_VIDEO_FILE, output_audio_file_location=OUTPUT_AUDIO_FILE_LOCATION, output_translated_audio_location=OUTPUT_TRANSLATED_AUDIO_LOCATION, video_file_name=DEFAULT_VIDEO_FILE_NAME , final_output_directory=FINAL_OUTPUT_DIRECTOR):
    try:
        print("started converting")
        #language_code, voice_name = find_language_code(language)
        print(language)
        video_file_name = video_file_name + "_" +language
        print(video_file_name)
        audio_file_id = "/" + video_file_name +".wav"
        output_audio_file_location = output_audio_file_location + audio_file_id
        print(output_audio_file_location)
        extract_audio_from_video.extract_audio(video_file, output_audio_file_location)
        print("audio extracted")
        transation_completed =audio_translation.translate_audio(output_audio_file_location,
                                                                              output_translated_audio_location,
                                                                              language
                                                                              )
        print("translation completed")

        if transation_completed:
            get_conversions(output_translated_audio_location, video_file, video_file_name, final_output_directory)
        return True
    except Exception as e:
        print("Exception has occured ...  convert_video() ")
        print(e)
        return False

def convert_image(video_file=DEFAULT_IMAGE_FILE, output_audio_file_location=OUTPUT_AUDIO_FILE_LOCATION, output_translated_audio_location=OUTPUT_TRANSLATED_AUDIO_LOCATION, video_file_name=DEFAULT_VIDEO_FILE_NAME , language=DEFAULT_LANGAUGE, final_output_directory=FINAL_OUTPUT_DIRECTOR, text_input='Hello'):
    try:
        print("Using convert image...")
        print(text_input)
        language_code, voice_name = find_language_code(language)
        print("fetched langauge code ...")
        video_file_name = video_file_name + "_" +language
        audio_file_id = "/" + video_file_name +".wav"
        output_audio_file_location = output_audio_file_location + audio_file_id
#         extract_audio_from_video.extract_audio(video_file, output_audio_location=output_audio_file_location)
        transation_completed = automated_transcription_script.translate_text_only(text_input,
                                                                              output_translated_audio_location,
                                                                              language_code=language_code,
                                                                              voice_name = voice_name
                                                                              )
        if transation_completed:
            get_conversions(output_translated_audio_location, video_file, video_file_name, final_output_directory)
        return True
    except Exception as e:
        print("Exception has occured ...  convert_image() ")
        print(e)
        return False
