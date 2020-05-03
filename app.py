from flask import Flask, render_template, request
#from euwerkzg import secure_filename
from werkzeug.utils import secure_filename

# Import dependencies
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import pickle 
import librosa
import librosa.display
from sklearn.preprocessing import normalize

# buff depedence 
import os
import io
import cv2 
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_core
import keras
from keras.models import load_model
#from keras.models import Model 

#import pickle
import cloudinary
# URL 
import soundfile as sf
from six.moves.urllib.request import urlopen
# Import .ipynb scripts (should be in parent directory)
#import predict_pitch
#import predict_inst
#import keras
#import tensorflow_core
# import 2 functions for ETL, load models and prediction
import URLtest_predict_pipeline
import cloudinary
import cloudinary.uploader
#import keras.backend.tensorflow_backend as tb
#tb._SYMBOLIC_SCOPE.value = True

#inst_model = None
#pitch_model = None

app = Flask(__name__)
app.config["ALLOWED_EXTENSIONS"] = ["wav", "WAV"]

#----------------------------------load_models BEGIN--------------------------------------------------------
#def load_inst_model():    
   #global inst_model    
   # model variable refers to the global variable, So we dont need to run model code everytime
   #with open('../Result_models/PKL_trained_instruments_model.pkl', 'rb') as instru_f:        
      #inst_model = pickle.load(instru_f)

#def load_CV_inst_model():    
   #global inst_model    
   # model variable refers to the global variable, So we dont need to run model code everytime
   #with open('../Result_models/CV_PKL_trained_instruments_model.pkl', 'rb') as CV_instru_f:        
      # CV_inst_model = pickle.load(CV_instru_f)

#def load_pitch_model():    
   #global pitch_model    
   #with open('../Result_models/PKL_trained_pitch_model.pkl', 'rb') as pitch_f:        
      #pitch_model = pickle.load(pitch_f)

#----------------------------------load_models END--------------------------------------------------------

@app.route('/')
def first_upload_file():
   return render_template('upload_LH.html')



@app.route('/uploader', methods = ['GET', 'POST'])
# @app.route('/uploader')
def upload_file():
   
   if request.method == 'POST': 
      f = request.files['file']
      if   not "." in f.filename:
         return render_template('error.html')
      
      ext = f.filename.rsplit(".", 1)[1]

      if ext.upper() in app.config["ALLOWED_EXTENSIONS"]:
         
         #f.save(secure_filename(f.filename))
         #file_name = (f.filename)
         result = cloudinary.uploader.unsigned_upload(f, upload_preset= 'q8vijdwg', cloud_name = 'dmqj5ypfp', resource_type='auto' )
         wavURL = result['url']
         predicted_pitch = URLtest_predict_pipeline.predict_pitch(wavURL)
         predicted_inst = URLtest_predict_pipeline.predict_instrument(wavURL)

         #testing 
         #predicted_pitch = 'A3'
         #predicted_inst = 'Piano'
         return render_template('dashboard.html', predicted_pitch = predicted_pitch, predicted_inst = predicted_inst) 
      
      else: 
         #return "file type error"
         return render_template('error.html')

        

if __name__ == '__main__':
   #app.run(threaded=False)
   app.run(debug = True)