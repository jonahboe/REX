import tensorflow as tf
import numpy as np
import serial
from serial.tools import list_ports
import cv2

# Set up a camera
cam = cv2.VideoCapture(0)

# Load the model
model = tf.keras.models.load_model('./RaspberryPi/model')


image = tf.keras.preprocessing.image.load_img(
        path='./RaspberryPi/0.png',
        color_mode='rgb',
        target_size=(120, 160),
        interpolation='nearest'
    )

dat = tf.keras.preprocessing.image.img_to_array(image)
sampl = np.array([dat])
sampl = tf.keras.utils.normalize(sampl, axis=1)
predicts = model.predict(sampl)
predict = np.argmax(predicts[0])
print(f'I predict: {predict}')


# Get list of available ports
availablePorts = list_ports.comports()

# Print list by name
portNumber = 0
for port in availablePorts:
    print(portNumber, port.device)
    portNumber += 1

# Connect to the port we want
ser = serial.Serial(availablePorts[2].device, 9600)
while True:
    message = ser.read(1)
    print(message)
    if message == b's':

        # Take three images
        samples = []
        for i in range(0, 3):
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")

            data = cv2.resize(frame, (160, 120))
            sample = np.array([data])
            sample = tf.keras.utils.normalize(sample, axis=1)
            predict = model.predict(sample)
            predict = np.argmax(predict[0])
            samples.append(predict)

        index = -1
        if samples[0] == samples[1] or samples[0] == samples[2]:
            index = 0
        else:
            if samples[1] == samples[2]:
                index = 1

        if index == -1:
            ser.write('a')
        else:
            if samples[index] == 0:
                ser.write('a')
            if samples[index] == 1:
                ser.write('b')
            if samples[index] == 2:
                ser.write('c')
            if samples[index] == 3:
                ser.write('d')
            if samples[index] == 4:
                ser.write('e')
            if samples[index] == 5:
                ser.write('f')

