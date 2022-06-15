# <Tensorflow model to C-Array>

## Description
In order to use Tensorflow models on edge devices they need to be converted into a format that’s optimized for this usecase. For TensorFlow these are known as “TFLITE” models, which is an optimized flatbuffer format. These TFLITE models can be used on systems that include a real time operating system with filesystem. 
In order to use a TensorFlow model on a device that does not include a filesystem, it first has to be converted (or generated at training) to a TFLITE flatbuffer. This TFLITE model can then be converted into a C-Byte-array which can be loaded into the program memory of a microcontroller.

## Installation
In order to use the python script make sure you have python 3 installed with the following libraries:
-	Glob
-	Tensorflow
-	Time

In order to use the batch scipt make sure you have the "windows subsystem for linux" installed.

## Usage
Place the TensorFlow “SavedModel” files inside the “SavedModel” directory and the .h5 files inside the “Keras” directory. (Note, converting “SavedModel” models can only be done one at a time, the script will convert every h5 file inside the “Keras” folder and name them accordingly). 
To use the “Tensorflow model to lite.py” script, open it in Spyder IDE and run it; or execute it in a python terminal. The script will then prompt the user to choose between converting a TensorFlow “SavedModel” model or a Keras.H5 model. After choosing which type to convert the script will automatically go into the relevant folder and place the converted files into the “Output” folder.

Model to lite to C-array/
├─ Keras/
├─ Output/
│  ├─ Convert TFLITE to C array.BAT
│  ├─ Model.tlite
│  ├─ Model.cc
│  ├─ Model.H
├─ SavedModel/
├─ Tensorflow model to lite.py

To convert the TFLITE model into a C byte array the "Convert TFLITE to C array.BAT" batch file can be used.
To use this batchfile simply doubleclick it and follow the instructions. 