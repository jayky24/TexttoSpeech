from cgitb import text
from gettext import bind_textdomain_codeset
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import PyPDF2
import os 
import tkinter as tk
engine = pyttsx3.init()  
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
voices = engine.getProperty('voices')
voiceFemales = filter(lambda v: v.gender == 'VoiceGenderFemale', voices)
root = Tk()
root.configure(bg="#305065")
root.geometry('900x450+100+100')

import tkinter

def close():  # just a placeholder implementation.
    print('close() called')



# fertig=tk.Toplevel()
# fertig.title("Window")
# text=tkinter.Label(fertig, text="Success")
# text.pack()
# img = tkinter.PhotoImage(file='backgnd.ppm')
# w = tkinter.Label(fertig, image=img)
# w.pack()
# knapp=tkinter.Button(fertig, text="Ok", command=lambda: close())
# knapp.pack()
# knapp.mainloop()



root.title("TEXT TO SPEECH")
root.resizable(False,False)

label_page = Label(root,text="TextToSpeechSynthesizer",font="arial 15 bold",bg="white").place(x=345,y=10)
label_page = Label(root,text="Page Number").place(x=80,y=138)
start_page_number = Entry(root)
start_page_number.place(x=169,y=138)
text_area=Text(root,font="Robote 80",bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=80,y=250,width=300,height=150)

Label(root,text="VOICE",font="arial 15 bold",bg="#305065",fg="white").place(x=580,y=160)
Label(root,text="SPEED",font="arial 15 bold",bg="#305065",fg="white").place(x=760,y=160)
gender_combobox=Combobox(root,values=['Male','Female'],font="arial 14",state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Male')

speed_combobox=Combobox(root,values=['Fast','Normal','slow'],font="arial 14",state='r',width=10)
speed_combobox.place(x=750,y=200)
speed_combobox.set('Normal')

def Speak():
   speaker= pyttsx3.init()
   txt = text_area.get(1.0, "end-1c")
   if not txt:
       txt = "please, PLease enter the Text first"
   if speed_combobox.get() == "Fast":
       speaker.setProperty('rate', 300)
   if speed_combobox.get() == "slow":
       speaker.setProperty('rate', 100)
   print(txt)
   if gender_combobox.get() == "Female":
       voice = speaker.getProperty('voices')
       speaker.setProperty('voice', voice[1].id)
   else:
       voice = speaker.getProperty('voices')
       speaker.setProperty('voice', voice[0].id)
   speaker.say(txt)
   speaker.runAndWait()

btn=Button(root,text="speak",width=10,font="arial 14  bold", command=Speak)
btn.place(x=550,y=280)

def download():
   speaker= pyttsx3.init()
   txt = text_area.get(1.0, "end-1c")
   if not txt:
       txt = "Please upload the file first to download it"
   if speed_combobox.get() == "Fast":
       speaker.setProperty('rate', 300)
   if speed_combobox.get() == "slow":
       speaker.setProperty('rate', 100)
   if gender_combobox.get() == "Female":
       voice = speaker.getProperty('voices')
       speaker.setProperty('voice', voice[1].id)
   else:
       voice = speaker.getProperty('voices')
       speaker.setProperty('voice', voice[0].id)
   speaker.save_to_file(txt, 'speech.mp3')
   speaker.say("File downloaded")
   speaker.runAndWait()

save=Button(root,text="Download",width=10,font="arial 14  bold", command=download)
save.place(x=730,y=280)
label = Label(root, text="which Book u want to read?" ,font="arial 10 bold",bg="white",fg="black").place(x=140,y=90)


def fileDialog():
   path = filedialog.askopenfilename()
   book = open(path, 'rb')
   pdfReader = PyPDF2.PdfFileReader(book)
   pages = pdfReader.numPages
   speaker= pyttsx3.init()
   if speed_combobox.get() == "Fast":
       speaker.setProperty('rate', 300)
   if speed_combobox.get() == "slow":
       speaker.setProperty('rate', 100)
   if gender_combobox.get() == "Female":
       voice = speaker.getProperty('voices')
       speaker.setProperty('voice', voice[1].id)
   else:
       voice = speaker.getProperty('voices')
       speaker.setProperty('voice', voice[0].id)

   for num in range(int(start_page_number.get()), pages):
       page = pdfReader.getPage(num)
       txt = page.extractText()
       print(txt)
       speaker.say(txt)
       speaker.runAndWait()

Button(root, text="Choose Book", command=fileDialog).place(x=195,y=165)
root.mainloop()