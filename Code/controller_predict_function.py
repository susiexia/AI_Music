# %%
import os
import librosa
from sklearn.preprocessing import normalize
import pickle
import keras
import numpy as np
import soundfile as sf
# %%
#--------------------------------TEST ETL Part----------------------------

file_name = '../Resources/AudioFiles/TinySOL/Strings/Viola/ordinario/Va-ord-C3-pp-4c-N.wav'

f = sf.SoundFile(file_name)

length = len(f) / f.samplerate

#
audio, sample_rate = librosa.load(file_name, offset=length/6, duration=1, res_type='kaiser_fast')
# mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, fmax=max_frequency)
mfccs = librosa.feature.melspectrogram(y=audio, sr=sample_rate)
mfccs_norm = normalize(mfccs.T, axis=0, norm='max')

channels = 1 # number of audio channels
row = 1 
spectrogram_shape1 = (1,) + mfccs_norm.shape + (channels,)

#x_reshape = np.array(i.reshape( (spectrogram_shape1) ) for i in mfccs_norm) 
x_reshape = mfccs_norm.reshape( (spectrogram_shape1) ) 

x_reshape.shape    # (1, 22, 128, 1)

#--------------------------------TEST END--------------------------------
# %%
# load trained model

with open('../Result_models/PKL_trained_instruments_model.pkl', 'rb') as instru_f:        
   model = pickle.load(instru_f)


# %%
# create a function for inst pred

def predict_instrument(input_x):
    # create a instrument and scalar table
    instName_list = ['Bass Tuba','French','Trombone','Trumpet','Accordion','Cello','Contrabass',
                'Viola', 'Violin','Alto Saxophone','Bassoon','Clarinet in Bb',
                'Flute','Oboe']
    # inst_model to predict
    inst_result = model.predict(input_x)
    
    # reverse to_categorical function, get correlated inst_name
    inst_scalar =  np.argmax(inst_result, axis=None, out=None)
    
    inst_pred = instName_list[inst_scalar]
    
    return inst_pred  

# %%
# call predict function
inst = predict_instrument(x_reshape)
inst  # output is an array with 14 elements


# %%
# reverse the to_categorical and get 
#reversed_inst =  np.argmax(inst, axis=None, out=None) 
#[np.argmax(y, axis=None, out=None) for y in inst]
# output is 2

# %%
