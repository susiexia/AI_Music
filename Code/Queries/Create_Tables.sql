CREATE TABLE Instruments_table (
	Instrument_ID INT NOT NULL,
	Instrument_Name VARCHAR NOT NULL PRIMARY KEY,
	Family VARCHAR NOT NULL
);

CREATE TABLE Pitch_table (
    Pitch VARCHAR PRIMARY KEY,
    Pitch_ID INT
);

-- ETL dataframes
CREATE TABLE Notes_Sprectrogram_Table(
    Spectrogram ARRAY, -- Please review here
    Path VARCHAR,
    Pitch VARCHAR,
    Pitch_ID int,
    FOREIGN KEY (Pitch) REFERENCES Pitch_table (Pitch)
);

CREATE TABLE Instruments_Sprectrogram_Table(
    Spectrogram ARRAY, -- Please review here
    Path VARCHAR,
    Family VARCHAR,
    Instrument_abbr VARCHAR,
    Instrument_name VARCHAR,
    FOREIGN KEY (Instrument_name) REFERENCES Instruments_table (Instrument_name)
);

CREATE TABLE Instruments__Notes_Sprectrogram_Table(
    Spectrogram ARRAY, -- Please review here
    Path VARCHAR,
    Family VARCHAR,
    Instrument_abbr VARCHAR,
    Instrument_name VARCHAR,
    Pitch VARCHAR,
    Pitch_ID int,
    FOREIGN KEY (Instrument_name) REFERENCES Instruments_table (Instrument_name),
    FOREIGN KEY (Pitch) REFERENCES Pitch_table (Pitch)
);