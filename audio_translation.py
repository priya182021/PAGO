import whisper
import os
#from googletrans import Translator
from gtts import gTTS
import speech_recognition as sr
from translate import Translator
# INDIC_NLP_LIB_HOME=r"C:\Users\D priyanka\indic_nlp_library"
# # The path to the local git repo for Indic NLP Resources
# INDIC_NLP_RESOURCES=r"C:\Users\D priyanka\indic_nlp_resources"
# import sys
# sys.path.append('{}'.format(INDIC_NLP_LIB_HOME))
# import re
# import os
# from tqdm import tqdm
# import shutil

# from indicnlp import common
# from indicnlp import loader
# common.set_resources_path(INDIC_NLP_RESOURCES)
# from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator as script_conv

model = whisper.load_model("base")
target_languages = ['te', 'fr', 'hi', 'de']  # Add more languages as needed

def translate_audio(audio_file,output_audio_file_location,langauge):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        transcript = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
        return False
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return False

    translator = Translator(to_lang="hi")
    translation = translator.translate(transcript)
    print(translation)
    try:
        voice = gTTS(translation, lang=langauge)
        voice.save(output_audio_file_location)
    except:
        print("error")
    # loader.load()
    # infname=transcript
    
    # if len(sys.argv) < 5:
    #     print("Usage: python indic_scriptmap.py <input_file> <output_file> <source_language> <target_language>")
    #     print("where <input_file> is the input file containing lines with the original script, and <output_file> is where the file with the script mapped content into the target language will be written.")
    #     print("<source_language> is the language of the original script, and <target_language> is the language of the script to be mapped into.")
    #     print("Example: python indic_scriptmap.py input.txt output.txt ta hi")
    #     print("This will map the script in the input.txt file from Tamil to Hindi.")
    #     exit()

    # print()
    # print(infname)
    # print(outfname)
    # print(inlang)
    # print(outlang)

    # with open(outfname,'w',encoding='utf-8') as outfile, \
    #     open(infname,'r',encoding='utf-8') as infile:
    # outfname=script_conv.transliterate(infname.strip(),'en',langauge)
    #     # translator = Translator()
    #     # translated_result = translator.translate(transcript, src='en', dest=langauge)
    #     # translated_text = translated_result
    #     # print(translated_text)
    #     # try:
    #     #     voice = gTTS(translated_text, lang=langauge)
    #     #     voice.save(output_audio_file_location)
    #     # except:
    #     #     return "error"
    # print(outfname)
    # try:
    #     voice = gTTS(outfname, lang=langauge)
    #     voice.save(output_audio_file_location)
    # except:
    #     return "error"
    return True
