#Imports
import glob as g 
import tensorflow as tf
import time as t
#End of Imports

#Constants
SavedModel = "1"
KerasModel = "2"
#End of constants

'''
THIS SCRIPT DOES NOT CURRENTLY DO ANY OPTIMALISATION OUTSIDE THE CONVERTING PROCESS
THIS COULD BE ADDED IF NEED BE.
'''

start_time = t.time()
print("Tensorflow version " + tf.__version__)

print("Please input a 1 for SavedModel or a 2 for Keras model") 
    
Model_Type = input()
if Model_Type == SavedModel:
    converter = tf.lite.TFLiteConverter.from_saved_model('SavedModel')
    tflite_model = converter.convert()  
    with open('output\savedmodel.tflite', 'wb') as f:
        f.write(tflite_model)
        
elif Model_Type == KerasModel:
    Location = g.glob('Keras/*.h5')
    n=0
    for Model in Location:
        print(Model)
        Keras_Model = tf.keras.models.load_model(str(Model))
        converter = tf.lite.TFLiteConverter.from_keras_model(Keras_Model)
        tflite_model = converter.convert()
        with open('Output/h5model-'+str(n)+'.tflite', 'wb') as f:
            f.write(tflite_model)
            n=n+1
else:  
    print("Error: Wrong value passed")
print("Time = "+str(t.time() - start_time))