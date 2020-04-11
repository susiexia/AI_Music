
# %%
# Import all dependencies
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np
import pandas as pd
# boto3 is a module to read data from S3 bucket in python.  
#You need to install it using (pip install boto3)
import boto3
# %%
# Connect to the S3 bucket by security credential (accesskeys)
client = boto3.client(
    's3',
    aws_access_key_id= 'AKIAIU2MIGCN6TKOZVBA',
    aws_secret_access_key= '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'
)
# Use the paginator funtion to go access through the folder and files in the S3 bucket
paginator = client.get_paginator('list_objects')
result = paginator.paginate(Bucket='musicalinstrumentsaudiodataset')
# Create an empty list to add in it the list of path for the .wav files from the S3 bucket 
keylist=[]
# Create for loop to go through all the .wav files path in the folders and add them to keylist list we created.
for page in result:
    if "Contents" in page:
        for key in page[ "Contents" ]:
            keyString = key[ "Key" ]
            #print(keyString)
            keylist.append(keyString)
# %%

type(keylist)
len(keylist)
print(keylist[3])
# %%
# open the .wav files and save them as bytes 
from scipy.io import wavfile as wav
from scipy.fftpack import fft
s3 = boto3.resource('s3', aws_access_key_id= 'AKIAIU2MIGCN6TKOZVBA',
    aws_secret_access_key= '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')
bucket = s3.Bucket('musicalinstrumentsaudiodataset')
# Create an empty list to add the open .wav files in. 
body1=[]
# Create for loop to loop through the keylist created previously in order to read the .wavfiles and save them as bytes files in the body1 list created 
# For Ruberic 1, We will just run through the a sample of data (first 6 .wavfiles) 
for j in range(6):
    obj = s3.Object('musicalinstrumentsaudiodataset', keylist[j])
    # Read the .wav file
    body = obj.get()['Body'].read()
    # Append the file read in the body1 list. The file type is bytes.
    body1.append(body)
# %%
# As you can see the .wavfiles is saved as bytes in the body1 list.
type(body1[0])
# %%
print(body1[3])

# %%
import scipy.io.wavfile as sciwav # This used to help read the .wav file
from io import BytesIO # This is used to help change the bytes to a readable .wavfile
# Create a empty list to add to it the arrays of the converted .wavfile.
wav_list= []
# Loop through the list of .wav bytes files.  
# For Ruberic 1 just chose a small sample (5 audiofiles)
for j in range(2,6):# Please note: started from 2 since the first 2 files are not .wav files
    # Change the .wav bytes to .wav file
    wrapper = BytesIO(body1[j])
    # Read the .wav file and convert it to an array
    wav_file = sciwav.read(wrapper)
    # Append it to a list(Note its a list of tuples)
    # If you just want the frequencies without sample rate you can just choose the wav_file[1]
    wav_list.append(wav_file)
# %%
# List of tuples (sample_rate and array )
print(wav_list)

# %% 
# Michaels Part
# This part to transform Data
# %%
# %%
