from flask import Flask, render_template, request
#from euwerkzg import secure_filename
from werkzeug.utils import secure_filename


# import 2 functions for ETL, load models and prediction
import predict_pipeline


app = Flask(__name__, static_url_path ="/tmp")
app.config["ALLOWED_EXTENSIONS"] = ["wav", "WAV"]


@app.route('/')
def first_upload_file():
   return render_template('upload.html')



@app.route('/uploader', methods = ['GET', 'POST'])
# @app.route('/uploader')
def upload_file():
   
   if request.method == 'POST': 
      f = request.files['file']
      if   not "." in f.filename:
         return render_template('error.html')
      
      ext = f.filename.rsplit(".", 1)[1]

      if ext.upper() in app.config["ALLOWED_EXTENSIONS"]:
         
         f.save(secure_filename(f.filename))
         #file_name = (f.filename)
         # predict_sound(f)
         
         #call fuctions from other files
         # Functions return string
         pitch_result = predict_pipeline.predict_pitch() # need a argument
         instrument_result = predict_pipeline.predict_instrument() # need a argument

         # create dictionary with the variable you want to return
         #return render_template('audio.html', # name parameter equal to variable)	

         #testing for now"
         return "successful"
         # final code
         # return render_template('audio.html', preprocess.<function name>, predict_pitch.<function name., predict_inst.<function name>) 
      
      else: 
         #return "file type error"
         return render_template('error.html')
        

if __name__ == '__main__':

   app.run(debug = True)