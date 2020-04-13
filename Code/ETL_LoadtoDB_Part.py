# %%
from sqlalchemy import create_engine
from config import db_password
#import psycopg2 
import pandas as pd 

# %%
# Instruments_table
instrument_category_df = pd.read_csv('../Data/Instrument_Table.csv')

instrument_category_df.columns = ['Instrument_ID', 'Instrument_Name', 'Family']

# %%
# Pitch_table
pitch_df = pd.read_csv('../Data/Pitch_table.csv')

pitch_df.columns = ['Pitch', 'Pitch_ID']
# %%
# load instrument general information into DataBase
engine = create_engine(f'postgres://postgres:{db_password}@127.0.0.1:5432/AI_Music_DB')

movies_with_ratings_df.to_sql(name='Instruments_table', con=engine, if_exists ='replace')

# load pitch general information into DataBase
engine = create_engine(f'postgres://postgres:{db_password}@127.0.0.1:5432/AI_Music_DB')

movies_with_ratings_df.to_sql(name='Pitch_table', con=engine, if_exists ='replace')

