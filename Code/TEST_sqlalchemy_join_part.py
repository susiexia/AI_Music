# %%
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# %%
engine = create_engine('postgresql://postgres:'+'1111'+'@localhost:5432/AI_Music_DB')
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect = True)
# We can view all of the classes that automap found
Base.classes.keys()
# %%
# Create our session (link) from Python to the DB
session = Session(engine)

# %%
results = session.query(Pitch_table.Pitch)
# %%
db = create_engine(engine)

# %%
db_string = "postgres://postgres:'+'1111'+'@localhost:5432/AI_Music_DB"

db = create_engine(db_string)

# %%
db.execute("CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")

# %%
