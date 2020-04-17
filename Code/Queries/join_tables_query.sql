-- The purpose of this query is combine the notes and instruments table together.

CREATE TABLE Instruments_Notes_Spectrogram_Table as
select a."index",a."Spectrogram",a."File_Path", a."Note",a."Octave", a."Pitch",b."Instrument_name" 
from public."Notes_Spectrogram_Table" a,
public."Instruments_Spectrogram_Table" b
where a."index" = b."index";