# AI_Music

## Presentation

**Description of data source:**

https://zenodo.org/record/3685367#.Xo1NVi2ZOuU

Orginally, this sound data set was recorded for a project called Studio On Line (SOL) at Ircam in Paris (1996-1999). The data set contains an intrument playing a single musical note . In total, there are 14 different instruments, which are listed below. 

1. Bass Tuba
2. French Horn
3. Trombone
4. Trumpet in C
5. Accordion
6. Contrabass
7. Violin
8. Viola
9. Violoncello
10. Bassoon
11. Clarinet in B-flat
12. Flute
13. Oboe
14. Alto Saxophone

TinySOL Data:

The TinySOL data set contains 2913 audio WAV files at 44.1 kHz. Each audio file has an instrument playing one musical note. The information of the insturment family and sound, oridinary playing technique, pitch, dynamic, additional information can be found in the file path. Moreover, this information can be found in the metadata as text, which can be furthered cleaned, organized, and analyzed. 

Metadata Data:

The TinySOL_metadata.csv contains text data and information of each path file in the TinySOL. The csv file contains the path, fold ID, instrument family, abbreviation, name, technique abbreviation and name, pitch, pitch ID, dynamic, dynamic ID, instance ID, string ID, and the need for digital retuning. 

## Git hub

**Communication Plan**

| Communciations | Objective | Stakeholders | Frequency | Channels | Notes |
| --- | --- | --- | --- | --- | --- |
| Flex Session | Update and brainstorm project group | TA, Teacher, Team | twice a week | Zoom | The time to have direct communication and get support in class |
| Quick Updates | Communicate with the team meembers | Team | As often as needed | Zoom and Slack | To share information with the team  outside of zoom meetings|  
| Team Meetings | To ask for help, review weekly tasks and timelines,  review roles and responsibilities, and push final commit | Team | 2-3 times a week | Zoom | To complete all tasks and answer questions before the segment due dates 
| Roles and Responsibilites, decision points, and notes | To review what tasks are assigned to each member and major decision points | Team | As often as needed | Google Docs | Meeting minutes will be recorded in the google docs | 
| Extra Help | Ask for help outside of class and team | The team member(s) and TA | TA office hours are held everyday | Zoom | If extra help is needed, and the team is struggling to find a solution, we will consult with a TA during office hours | 


## Machine Learning Model

**Model:** Neural Network (musical note and instrument)

**why?** 

The model will be able to learn with the data, and eventually be able to identify the musical note and instrument in the inputed audio file. 

**How are you training your model?**

The inputed audio files will be converted into spectograms. The machine will train and learn by associating the image with the intrument and note.

**What is the model’s accuracy?**

Our goal is the model to obtain 80% accuracy. 

**How does this model work?**

We will be converting the audio files into a Fourier Transformation and Fast fourier Transformation, which is a signal/function into it's fundamental frequencies. Moreover, we will convert the FFT into a spectogram image. We are feeding and training the machine to be able to identify the musical note and instrument to visual spectrograms. Eventually, the machine will take an inputted audio file, convert it into a spectogram, and identify the instrument and musical note by associating it to a similar spectogram that the machine was trained with. 

**Model Output:** 

- Instrument : One out of the 14 instruments listed above
- Note and Octave: The musical note letter and the octave number





