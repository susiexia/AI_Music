from flask import Flask, render_template, request
#from euwerkzg import secure_filename
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/')
def first_upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
# @app.route('/uploader')
def upload_file():
   
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      file_name = (f.filename)
      
      return file_name + ' file uploaded successfully' 
         
      # return render_template('audio.html')		

if __name__ == '__main__':
   app.run(debug = True)