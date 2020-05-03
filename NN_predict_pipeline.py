# %%
import numpy as np
import pandas as pd 

import librosa
import librosa.display
from sklearn.preprocessing import normalize
from keras.models import load_model

# buff depedence 
import os
import io
#import cv2 
import matplotlib.pyplot as plt

#import urllib3
#from urllib3 import urlopen
# URL 
import cloudinary
import soundfile as sf
from six.moves.urllib.request import urlopen

import tensorflow as tf

#------------------------------------------------
mel_coefs = 50
max_frequency = 10000

#--------------------------------------------------
def predict_instrument(url):
    '''This function includes ETL process, loading trained model, 
        and using model to get prediction'''
    
    # -------------------------------ETL preprocessing part------------------------------------
    '''TESTING: USE LOCAL FILE PATH AS input_audioFile '''
    #f = sf.SoundFile(file_name)
    #length = len(f) / f.samplerate
        

        
    #URL 
    audio, samplerate = sf.read(io.BytesIO(urlopen(url).read()), start=0, stop=44100)
    #data = urlopen(url)
    data_22k = librosa.resample(audio, samplerate, 22050)

    #audio, sample_rate = librosa.load(data, duration=1, res_type='kaiser_fast')

    mfccs = librosa.feature.melspectrogram(y=data_22k)
        
    # Normalize spectrogram values
    mfccs_norm = normalize(mfccs.T, axis=0, norm='max')
    # convert mfccs_norm into 4d array

    channels = 1 # number of audio channels
    row = 1 
    spectrogram_shape1 = (row,) + mfccs_norm.shape + (channels,)

    #x_reshape = np.array(i.reshape( (spectrogram_shape1) ) for i in mfccs_norm) 
    inst_ETL_4d_output = mfccs_norm.reshape( (spectrogram_shape1) ) 

    print(inst_ETL_4d_output.shape)
    
    # --------------------------------Load trained inst model--------------------------
    # load trained inst model
    #with open('CV_PKL_trained_instruments_model.pkl', 'rb') as inst_f:        
    #    inst_model = pickle.load(inst_f)
    #from keras.models import load_model
    inst_model = tf.keras.models.load_model('trained_intruments_model.h5')

    # --------------------------------PREDICTION --------------------------
    # inst_model (from app.py) to predict
    inst_result = inst_model.predict(inst_ETL_4d_output)
    
    # reverse to_categorical() function, get correlated inst_name
    inst_scalar =  np.argmax(inst_result, axis=None, out=None)
    
    # extract inst names from csv to be a list
    inst_Name_df = pd.read_csv('CV_inst_Name.csv')
    inst_name_list = inst_Name_df['0'].tolist()
    
    # reverse labelEncoder() function to get prediction label
    NN_inst_pred = inst_name_list[inst_scalar]
    
    return NN_inst_pred  
# %%
url = "https://raw.githubusercontent.com/susiexia/AI_Music/susie/BTb-ord-A%231-ff-N-T30d.wav"
#url = "https://res.cloudinary.com/dmqj5ypfp/video/upload/v1588530259/Uploaded_audio/a0frl4m8km6rfi48ur6m.wav"
predict_instrument(url)  

# %%
