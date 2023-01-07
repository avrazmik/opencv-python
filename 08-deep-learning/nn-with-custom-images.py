from keras.preprocessing.image import ImageDataGenerator
import cv2

PATH = "C:/Users/Y9ESEH724/Downloads/CATS_DOGS/CATS_DOGS"

img = cv2.imread(PATH + "/train/CAT/0.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

import matplotlib.pyplot as plt


gen = ImageDataGenerator(
    rotation_range=30,
    rescale=1 / 255,
    horizontal_flip=True,
    zoom_range=0.2,
    shear_range=0.2,
)

from keras.models import Sequential
from keras.layers import Dropout, Flatten, Conv2D, MaxPooling2D, Dense

input_shape = (150, 150, 3)
model = Sequential()
model.add(
    Conv2D(filters=32, kernel_size=(3, 3), input_shape=input_shape, activation="relu")
)
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(
    Conv2D(filters=64, kernel_size=(3, 3), input_shape=input_shape, activation="relu")
)
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(
    Conv2D(filters=64, kernel_size=(3, 3), input_shape=input_shape, activation="relu")
)
model.add(MaxPooling2D(pool_size=(2, 2)))


model.add(Flatten())
model.add(Dense(128, activation="relu"))

model.add(Dropout(0.5))

model.add(Dense(1, activation="sigmoid"))
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

model.summary()


batch_size = 16

train_image_gen = gen.flow_from_directory(
    PATH + "/train", target_size=(150, 150), batch_size=batch_size
)
test_image_gen = gen.flow_from_directory(
    PATH + "/test", target_size=(150, 150), batch_size=batch_size
)

results = model.fit(
    train_image_gen, epochs=1, steps_per_epoch_g=100, validation_data=test_imageen
)
