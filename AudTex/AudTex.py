# importing libraries
import speech_recognition as sr
import os
import shutil
import sys
from os import path
import pyaudio
from pydub import AudioSegment
from pydub.silence import split_on_silence
from fpdf import FPDF
# create a speech recognition object
r = sr.Recognizer()

# a function that splits the audio file into chunks
# and applies speech recognition
def get_large_audio_transcription(path):
    """
    Splitting the large audio file into chunks
    and apply speech recognition on each of these chunks
    """
    # open the audio file using pydub
    sound = AudioSegment.from_wav(path)
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-14,
        # keep the silence for 1 second, adjustable as well
        keep_silence=500,
    )
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                print(chunk_filename, ":", text)
                whole_text += text
    # return the text for all chunks detected
    shutil.rmtree(r'C:\Users\jadha\Desktop\AudTex\audio-chunks')
    f = open("Read.txt", "w")
    f.write(whole_text)
    f.close()
    pdf = FPDF() 

    pdf.add_page() 

    pdf.set_font("Arial", size = 15) 

    g = open("Read.txt", "r") 

    for x in g: 
            pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
    
    g.close()
    pdf.output("README.pdf")
    

path = sys.argv[1]
get_large_audio_transcription(path)
shutil.rmtree(r'C:\Users\jadha\Desktop\AudTex\Read.txt')







