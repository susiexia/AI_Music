# %%
import numpy as np
import pandas as pd 
# create a function for pitch pred
def predict_pitch(input_x):

    # extract pitch names from csv to be a list
    pitch_Name_df = pd.read_csv('Data/pitchName.csv')
    pitch_name_list = pitch_Name_df['0'].tolist()

    # pitch_model (from app.py) to predict
    pitch_result = pitch_model.predict(input_x)
    
    # reverse to_categorical function, get correlated pitch_name
    pitch_scalar =  np.argmax(pitch_result, axis=None, out=None)
    
    pitch_pred = pitch_Name_list[pitch_scalar]
    
    return pitch_pred  
# %%
