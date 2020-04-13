-- select some columns to feed into Neural Network

-- This is for predict instruments
SELECT Spectrogram, Instrument_name, Pitch
FROM Instruments__Notes_Spectrogram_Table;


-- This is for predict Notes
SELECT Spectrogram, Pitch
FROM Instruments__Notes_Spectrogram_Table;

