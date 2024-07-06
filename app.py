#from crypt import methods
from flask import Flask
from flask import redirect, render_template, request, send_file,send_from_directory
import os
from werkzeug.utils import secure_filename
import pyttsx3
import PyPDF2

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'C:\\Users\\mayur\\OneDrive\\Desktop\\vs code\\programs\\Audiobook\\static\\doc'
app.config['DOWNLOAD_FOLDER'] = 'C:\\Users\\mayur\\OneDrive\\Download'
ALLOWED_EXTENSIONS = set(['mp3'])

def allowed_file(filename):
	return '.' in filename and \
		filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def hello():
   return render_template('main.html')
	
global f

@app.route("/uploader" , methods=['GET', 'POST'])
def uploader():

   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
      print('file = ',os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
    
      return render_template('main.html',name ='file uploaded successfully '+f.filename)

   return render_template('main.html')
    
    #   return 'file uploaded successfully'

@app.route("/download",methods=['POST'])
def audio():
    print('file :',f.filename)
    save = audio(f.filename)
    #return send_file(save,as_attachment=True)
    send_file("output.mp3",as_attachment=True)
                #return send_from_directory('output', output_file)
                #return redirect(url_for('download'))            

    return render_template('main.html')

def audio(file):
    book = open(file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages

    speaker = pyttsx3.init()
    speaker.setProperty('rate', 130)
    speaker.say('This App is Built by Mayur Pimpude.')
    speaker.setProperty('rate', 130)

    full = ""

    for num in range(pdfReader.numPages):
        page = pdfReader.getPage(num)
        text = page.extractText()
        full += text 

    speaker.save_to_file(full,"output.mp3")
    speaker.runAndWait()

if __name__ == "__main__":
    app.run(debug=True)