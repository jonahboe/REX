import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import normalize
import matplotlib.pyplot as plt


##################################
# Load the images as an array
##################################
imageData = []
print("Processing images: ")
for i in range(0, 388):
    filePath = "DataCollector/" + str(i) + ".png"

    print("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b", filePath, end="")

    image = tf.keras.preprocessing.image.load_img(
        path=filePath,
        color_mode='rgb',
        target_size=(120, 160),
        interpolation='nearest'
    )

    data = img_to_array(image)

    imageData.append(data)
print()


##################################
# Load the targets as an array
##################################
targets = pd.read_csv("DataCollector/results.txt", header=None).transpose()


##################################
# Split up the data and normalize
##################################
x_train, x_test, y_train, y_test = train_test_split(imageData,
                                                    targets,
                                                    test_size=0.2,
                                                    shuffle=True,
                                                    random_state=9)
x_train = normalize(x_train, axis=1)
x_test = normalize(x_test, axis=1)
plt.imshow(x_train[0])
plt.show()


##################################
# Create a model
##################################
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Conv2D(32,
                                 kernel_size=(8, 8),
                                 activation=tf.nn.swish,
                                 input_shape=(120, 160, 3)))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation=tf.nn.swish))
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))
model.add(tf.keras.layers.Dropout(0.25))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.swish))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(6, activation=tf.nn.softmax))  # Output layer

# Set some training parameters
model.compile(optimizer=tf.keras.optimizers.Adamax(),
              loss=tf.keras.losses.sparse_categorical_crossentropy,
              metrics=['accuracy'])


##################################
# Train the model
##################################
train_accuracy = []
train_loss = []
test_accuracy = []
test_loss = []
for i in range(0, 100):
    tf.keras.models.save_model(model, 'model')
    history = model.fit(x_train, y_train, epochs=1)
    los, acc = model.evaluate(x_test, y_test)
    train_accuracy.append(history.history['accuracy'])
    train_loss.append(history.history['loss'])
    test_accuracy.append(acc)
    test_loss.append(los)
    if i == 100:
        break;

# Training
plt.plot(train_accuracy)
plt.title('Training Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.show()

plt.plot(train_loss)
plt.title('Training Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.show()

# Testing
plt.plot(test_accuracy)
plt.title('Testing Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.show()

plt.plot(test_loss)
plt.title('Testing Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.show()
