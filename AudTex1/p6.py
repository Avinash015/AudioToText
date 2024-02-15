from tkinter import *
from tkinter.messagebox import showinfo
from gtts import gTTS
import speech_recognition as sr
import os

mainwindow= Tk()
mainwindow.title('DataFlair Text-To-Speech and Speech-To-Text Converter')
mainwindow.geometry('500x500')
mainwindow.resizable(0, 0)
mainwindow.configure(bg='yellow')




#Initialize recognizer class (for recognizing the speech)

def recordvoice():
    while True:
        r = sr.Recognizer()
        with sr.AudioFile('me.wav') as source:
    
            audio_text = r.listen(source)
    

            try:
        
        # using google speech recognition
                text1 = r.recognize_google(audio_text)
           
            except:
                pass
            return(text1)
        
def SpeechToText():
    speechtotextwindow = Toplevel(mainwindow)
    speechtotextwindow.title('Speech-to-Text Converter by DataFlair')
    speechtotextwindow.geometry("500x500")
    speechtotextwindow.configure(bg='pink')
 
    Label(speechtotextwindow, text='Speech-to-Text Converter by DataFlair', font=("Comic Sans MS", 15), bg='IndianRed').place(x=50)
 
    text = Text(speechtotextwindow, font=12, height=3, width=30)
    text.place(x=7, y=100)
   
    recordbutton = Button(speechtotextwindow, text='import mp3', bg='Sienna', command=lambda: text.insert(END, recordvoice()))
    recordbutton.place(x=140, y=50)
 
Label(mainwindow, text='Speech-To-Text Converter',
     font=('Times New Roman', 16), bg='red', wrap=True, wraplength=450).place(x=25, y=0)
 
speechtotextbutton = Button(mainwindow, text='Speech-To-Text Conversion', font=('Times New Roman', 16), bg='Purple', command=SpeechToText)
speechtotextbutton.place(x=100, y=250)
 
mainwindow.update()
mainwindow.mainloop()
