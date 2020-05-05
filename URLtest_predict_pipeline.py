
import numpy as np
import pandas as pd 

import librosa
import librosa.display
from sklearn.preprocessing import normalize
from keras.models import load_model

# buff depedencies 
import os
import io
from cv2 import cv2 
import matplotlib.pyplot as plt

# URL 
import cloudinary
import soundfile as sf
from six.moves.urllib.request import urlopen

import tensorflow as tf


'''This python script includes 2 functions, predict_pitch and predict_instrument'''

# create a function for pitch pred
def predict_pitch(url):
    '''This function includes ETL process, loading trained model, 
        and using model to get prediction'''
    
    #direclt use URL and convert to audio file
    audio, samplerate = sf.read(io.BytesIO(urlopen(url).read()))
    
    audio = audio.T
    data_22k = librosa.resample(audio, samplerate, 21395) # local files: sampleRate = 22050
    fig = plt.figure(figsize=[1.5,10])

    # Convert audio array to 'Constant-Q transform'. 86 bins are created to take pitches form E1 to C#8
    conQfit = librosa.cqt(data_22k,hop_length=4096,n_bins=86)
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
        
    # close the plotted image so it wont show 
    plt.close()
    fig.clf()
    plt.close(fig)
    plt.close('all')

    # convert mfccs_norm into 4d array

    channels = 1 # number of audio channels
    row = 1 
    spectrogram_shape1 = (row,) + mfccs_norm.shape + (channels,)

    pitch_ETL_4d_output = mfccs_norm.reshape( (spectrogram_shape1) ) 

    #print(pitch_ETL_4d_output.shape)
    
    # Load trained CNN model 
    pitch_model = tf.keras.models.load_model('pitch_model.h5')
    
    # use model to predict
    pitch_result = pitch_model.predict(pitch_ETL_4d_output)
    
    # reverse to_categorical() function, get the correlated pitch_name
    pitch_scalar =  np.argmax(pitch_result, axis=None, out=None)
    
    # extract pitch names from csv to be a list
    pitch_Name_df = pd.read_csv('pitchName.csv')
    pitch_name_list = pitch_Name_df['0'].tolist()
    
    # reverse labelEncoder() function to get prediction label
    pitch_pred = pitch_name_list[pitch_scalar]
    
    return pitch_pred  



def predict_instrument(url):
    '''This function includes ETL process, loading trained model, 
        and using model to get instrument prediction'''

    #URL 
    audio, samplerate = sf.read(io.BytesIO(urlopen(url).read()))

    audio = audio.T
    data_22k = librosa.resample(audio, samplerate, 21395)

    fig = plt.figure(figsize=[6,4])

    # Convert audio array to 'Constant-Q transform'. 86 bins are created to take pitches form E1 to C#8
    mfccs = librosa.feature.melspectrogram(data_22k, hop_length = 1024)  
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

    inst_ETL_4d_output = inst_mfccs_norm.reshape( (spectrogram_shape1) ) 

    #print(inst_ETL_4d_output.shape)
    
    # load trained inst model

    inst_model = tf.keras.models.load_model('CV_trained_intruments_model.h5')

    # use loaded model to predict 
    inst_result = inst_model.predict(inst_ETL_4d_output)
    
    # reverse to_categorical() function, get correlated inst_name
    inst_scalar =  np.argmax(inst_result, axis=None, out=None)
    
    # extract inst names from csv to be a list
    inst_Name_df = pd.read_csv('CV_inst_Name.csv')
    inst_name_list = inst_Name_df['0'].tolist()
    
    # reverse labelEncoder() function to get prediction label
    inst_pred = inst_name_list[inst_scalar]
    
    return inst_pred  

# create a functions to get pitch and instrument spectrogram
def get_spect_pitch(url):
    '''This function gets the spectrogram for pitch'''
    
    #direclt use URL and convert to audio file
    audio, samplerate = sf.read(io.BytesIO(urlopen(url).read()))
    
    audio = audio.T
    data_22k = librosa.resample(audio, samplerate, 21395) # local files: sampleRate = 22050
    fig = plt.figure(figsize=[1.5,10])

    # Convert audio array to 'Constant-Q transform'. 86 bins are created to take pitches form E1 to C#8
    conQfit = librosa.cqt(data_22k,hop_length=4096,n_bins=86)
    librosa.display.specshow(conQfit)
               
    # Capture image and convert into 2D array
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=(56))
    buf.seek(0)
    data = buf.read()
    buf.close()
    
    return data

def get_spect_inst(url):
    '''This function get the spectrogram for instrument'''

    #URL 
    audio, samplerate = sf.read(io.BytesIO(urlopen(url).read()))

    audio = audio.T
    data_22k = librosa.resample(audio, samplerate, 21395)

    fig = plt.figure(figsize=[6,4])

    # Convert audio array to 'Constant-Q transform'. 86 bins are created to take pitches form E1 to C#8
    mfccs = librosa.feature.melspectrogram(data_22k, hop_length = 1024)  
    mel_spec = librosa.power_to_db(mfccs, ref=np.max,)
    librosa.display.specshow(mel_spec)

    # Capture image and convert into 2D array
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=(90))
    buf.seek(0)
    data = buf.read()
    buf.close()
    
    
    return data 