import PyPDF3
import pyttsx3
import pdfplumber
import objc
import os
from gtts import gTTS

import os

script_directory = os.path.dirname(os.path.abspath(__file__))


file = 'Yamamoto Tsunetomo - Hagakure. The Book of Samurai.pdf'

file_path = os.path.join(script_directory, file)

book = open(file_path,'rb')
pdfReader = PyPDF3.PdfFileReader(book)

pages = pdfReader.numPages

finalText = ''
with pdfplumber.open(file_path) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        finalText += text


tts = gTTS(text=finalText, lang='en')
tts.save(os.path.join(script_directory, 'Hagakure.mp3'))


