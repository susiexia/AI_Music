
import numpy as np

# create a function for inst pred
def predict_instrument(input_x):
    # create a instrument and scalar table
    instName_list = ['Bass Tuba','French','Trombone','Trumpet','Accordion','Cello','Contrabass',
                'Viola', 'Violin','Alto Saxophone','Bassoon','Clarinet in Bb',
                'Flute','Oboe']
    # inst_model to predict
    inst_result = inst_model.predict(input_x)
    
    # reverse to_categorical function, get correlated inst_name
    inst_scalar =  np.argmax(inst_result, axis=None, out=None)
    
    inst_pred = instName_list[inst_scalar]
    
    return inst_pred  