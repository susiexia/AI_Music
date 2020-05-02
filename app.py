# Import dependencies
from flask import Flask, render_template, request
#from euwerkzg import secure_filename
from werkzeug.utils import secure_filename

# Import .ipynb scripts (should be in parent directory)
import preprocess
import load_model # probably don't need to import this
import predict_pitch
import predict_inst

# Create flask instance
app = Flask(__name__)

# Connect index page to index function
@app.route('/')
def index():
   # return the upload page (render_template can only load pages in templates folder)
   return render_template('upload.html')

# Connect /uploader page to upload_file function. User will post audio file.
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      file_name = (f.filename)
      
      # return file_name + ' file uploaded successfully'
      # return render_template('audio.html')
      return render_template('audio.html',
                           preprocess.<function name>,
                           predict_pitch.<function name>,
                           predict_inst.<function name>)

# Start flask server
if __name__ == '__main__':
   app.run(debug = True)