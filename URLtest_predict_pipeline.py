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
import cv2 
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_core
import keras
#from keras.models import Model 

import pickle
import cloudinary
# URL 
import soundfile as sf
from six.moves.urllib.request import urlopen
# %%
'''This python script includes 2 functions, predict_pitch and predict_instrument'''
# %%
# create a function for pitch pred
def predict_pitch(url):
    '''This function includes ETL process, loading trained model, 
        and using model to get prediction'''
    
    # -------------------------------ETL preprocessing part------------------------------------
    '''TESTING: USE LOCAL FILE PATH AS input_audioFile '''

    # use librosa convert audio file to spectrogram
    #audio, sample_rate = librosa.load(input_audioFile) # remove offset=length/6, duration=1, res_type='kaiser_fast'

    #URL 
    audio, samplerate = sf.read(io.BytesIO(urlopen(url).read()))


    fig = plt.figure(figsize=[1.5,10])
    # Convert audio array to 'Constant-Q transform'. 86 bins are created to take pitches form C1 to C#8
    conQfit = librosa.cqt(audio,hop_length=4096,n_bins=86)
    librosa.display.specshow(conQfit)
               
    # Capture image and convert into 2D array
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=(56/5))
    buf.seek(0)
    img_arr = np.frombuffer(buf.getvalue(), dtype=np.uint8)
    buf.close()
    img = cv2.imdecode(img_arr, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
    # normalize
    mfccs_norm = normalize(img, axis=0, norm='max')
        
    # close the plotted image so it wont show while in the loop
    plt.close()
    fig.clf()
    plt.close(fig)
    plt.close('all')

    # convert mfccs_norm into 4d array

    channels = 1 # number of audio channels
    row = 1 
    spectrogram_shape1 = (row,) + mfccs_norm.shape + (channels,)

    #x_reshape = np.array(i.reshape( (spectrogram_shape1) ) for i in mfccs_norm) 
    pitch_ETL_4d_output = mfccs_norm.reshape( (spectrogram_shape1) ) 

    #print(pitch_ETL_4d_output.shape)
    
    # --------------------------------Load trained pitch model--------------------------
    # load trained pitch model
    #global pitch_model
    #with open('PKL_trained_pitch_model.pkl', 'rb') as pitch_f:        
     #   pitch_model = pickle.load(pitch_f)
    pitch_model = tf.keras.models.load_model('pitch_model.h5')
    

    # --------------------------------PREDICTION --------------------------
    # pitch_model (from app.py) to predict
    pitch_result = pitch_model.predict(pitch_ETL_4d_output)
    
    # reverse to_categorical() function, get correlated pitch_name
    pitch_scalar =  np.argmax(pitch_result, axis=None, out=None)
    
    # extract pitch names from csv to be a list
    pitch_Name_df = pd.read_csv('Data/pitchName.csv')
    pitch_name_list = pitch_Name_df['0'].tolist()
    
    # reverse labelEncoder() function to get prediction label
    pitch_pred = pitch_name_list[pitch_scalar]
    
    return pitch_pred  


# %%
def predict_instrument(url):
    '''This function includes ETL process, loading trained model, 
        and using model to get prediction'''
    
    # -------------------------------ETL preprocessing part------------------------------------
    '''TESTING: USE LOCAL FILE PATH AS input_audioFile '''

    # use librosa convert audio file to spectrogram
    #audio, sample_rate = librosa.load(input_audioFile) # remove offset=length/6, duration=1, res_type='kaiser_fast'

    #URL 
    audio, samplerate = sf.read(io.BytesIO(urlopen(url).read()))
                               
    fig = plt.figure(figsize=[6,4])
    # Convert audio array to 'Constant-Q transform'. 86 bins are created to take pitches form C1 to C#8
    mfccs = librosa.feature.melspectrogram(audio, hop_length = 1024)  
    mel_spec = librosa.power_to_db(mfccs, ref=np.max,)
    librosa.display.specshow(mel_spec)

    # Capture image and convert into 2D array
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=(43/3))
    buf.seek(0)
    img_arr = np.frombuffer(buf.getvalue(), dtype=np.uint8)
    buf.close()
    img = cv2.imdecode(img_arr, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # normalize
    inst_mfccs_norm = normalize(img, axis=0, norm='max')
    
    # close the plotted image so it wont show while in the loop
    plt.close()
    fig.clf()
    plt.close(fig)
    plt.close('all')
        
    # convert mfccs_norm into 4d array

    channels = 1 # number of audio channels
    row = 1 
    spectrogram_shape1 = (row,) + inst_mfccs_norm.shape + (channels,)

    #x_reshape = np.array(i.reshape( (spectrogram_shape1) ) for i in mfccs_norm) 
    inst_ETL_4d_output = inst_mfccs_norm.reshape( (spectrogram_shape1) ) 

    #print(inst_ETL_4d_output.shape)
    
    # --------------------------------Load trained inst model--------------------------
    # load trained inst model
    #global inst_model
    #with open('CV_PKL_trained_instruments_model.pkl', 'rb') as inst_f:        
    #    inst_model = pickle.load(inst_f)
    #from keras.models import load_model
    inst_model = tf.keras.models.load_model('CV_trained_intruments_model.h5')

    # --------------------------------PREDICTION --------------------------
    # inst_model (from app.py) to predict
    inst_result = inst_model.predict(inst_ETL_4d_output)
    
    # reverse to_categorical() function, get correlated inst_name
    inst_scalar =  np.argmax(inst_result, axis=None, out=None)
    
    # extract inst names from csv to be a list
    inst_Name_df = pd.read_csv('Data/CV_inst_Name.csv')
    inst_name_list = inst_Name_df['0'].tolist()
    
    # reverse labelEncoder() function to get prediction label
    inst_pred = inst_name_list[inst_scalar]
    
    return inst_pred  

# %%
# -----------------------TESTING with local file path------------------------------
#url = "https://raw.githubusercontent.com/susiexia/AI_Music/susie/BTb-ord-A%231-ff-N-T30d.wav"
url = "https://res.cloudinary.com/dmqj5ypfp/video/upload/v1588480295/Uploaded_audio/euzkrwcoshxinmciwofi.wav"
predict_pitch(url)            # OUTPUT IS A STRING 

# %%
# -----------------------TESTING with local file path------------------------------
#file_name = 'Resources/AudioFiles/TinySOL/Strings/Viola/ordinario/Va-ord-C3-pp-4c-N.wav'
#url = "https://raw.githubusercontent.com/susiexia/AI_Music/susie/BTb-ord-A%231-ff-N-T30d.wav"
url = "https://res.cloudinary.com/dmqj5ypfp/video/upload/v1588480295/Uploaded_audio/euzkrwcoshxinmciwofi.wav"
predict_instrument(url)            # OUTPUT IS A STRING 


# %%
