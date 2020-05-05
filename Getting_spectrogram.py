
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
import cloudinary.uploader
import soundfile as sf
from six.moves.urllib.request import urlopen

import tensorflow as tf



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


