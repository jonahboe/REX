import tensorflow as tf
import numpy as np
import serial
from serial.tools import list_ports

image = tf.keras.preprocessing.image.load_img(
        path='./RaspberryPi/1.png',
        color_mode='rgb',
        target_size=(120, 160),
        interpolation='nearest'
    )
model = tf.keras.models.load_model('./RaspberryPi/model')
data = tf.keras.preprocessing.image.img_to_array(image)
sample = np.array([data])
sample = tf.keras.utils.normalize(sample, axis=1)
predictions = model.predict(sample)
prediction = np.argmax(predictions[0])
print(f'I predict: {prediction}')

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
    c = ser.read(1)
    print(c)
    if c == b's':
        print("got message")


