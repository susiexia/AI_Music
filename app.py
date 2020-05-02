from flask import Flask, render_template, request
#from euwerkzg import secure_filename
from werkzeug.utils import secure_filename
import pickle 
# Import .ipynb scripts (should be in parent directory)
import preprocess
#import load_model # probably don't need to import this
import predict_pitch
import predict_inst


inst_model = None
pitch_model = None

app = Flask(__name__, static_url_path ="/tmp")
app.config["ALLOWED_EXTENSIONS"] = ["wav", "WAV"]

#----------------------------------load_models BEGIN--------------------------------------------------------
def load_inst_model():    
   global inst_model    
   # model variable refers to the global variable, So we dont need to run model code everytime
   with open('../Result_models/PKL_trained_instruments_model.pkl', 'rb') as instru_f:        
      inst_model = pickle.load(instru_f)

def load_CV_inst_model():    
   global inst_model    
   # model variable refers to the global variable, So we dont need to run model code everytime
   with open('../Result_models/CV_PKL_trained_instruments_model.pkl', 'rb') as CV_instru_f:        
      CV_inst_model = pickle.load(CV_instru_f)

def load_pitch_model():    
   global pitch_model    
   with open('../Result_models/PKL_trained_pitch_model.pkl', 'rb') as pitch_f:        
      pitch_model = pickle.load(pitch_f)

#----------------------------------load_models END--------------------------------------------------------

#def preprocessing(file_binary):
   # preprocessing data from audio to spectrogram

#def predict_sound(file_binary):
   # classifier model code
   #call model


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