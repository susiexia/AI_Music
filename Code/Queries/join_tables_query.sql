-- The purpose of this query is combine the notes and instruments table together.

SELECT Spectrogram, (File_Path), ins.Instrument_Name, Pitch, Note, Octave
INTO Instruments_Notes_Spectrogram_Table
FROM Notes_Spectrogram_Table AS ns
INNER JOIN Instruments_Spectrogram_Table AS ins
ON ns.Spectrogram = ins.Spectrogram;