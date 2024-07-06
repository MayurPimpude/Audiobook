import pyttsx3
import PyPDF2

def audio(file):
    book = open(file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages

    speaker = pyttsx3.init()
    speaker.setProperty('rate', 130)
    speaker.say('This App is Built by Mayur Pimpude.')
    speaker.setProperty('rate', 145)

    full = ""

    for num in range(pdfReader.numPages):
        page = pdfReader.getPage(num)
        text = page.extractText()
        full += text 
        speaker.runAndWait()

    speaker.save_to_file(full,"output.mp3")
    speaker.runAndWait()
 
    

file = audio('IOT.pdf')
print(file)