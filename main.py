# module imports
import PyPDF2
import pyttsx3

# PDF file
path = open('Test_Document.pdf', 'rb')

# create the reader
pdfreader = PyPDF2.PdfFileReader(path)

from_page = pdfreader.getPage(0)

text = from_page.extractText()

speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()

# Conversion request
