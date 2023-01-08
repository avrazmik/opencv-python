from multiprocessing.dummy import active_children
from keras.datasets import fashion_mnist

(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

import matplotlib.pyplot as plt


x_train_norm = x_train / x_train.max()
x_test_norm = x_test / x_test.max()

x_train_norm = x_train_norm.reshape(
    x_train_norm.shape[0], x_train_norm.shape[1], x_train_norm.shape[2], 1
)
x_test_norm = x_test_norm.reshape(
    x_test_norm.shape[0], x_test_norm.shape[1], x_test_norm.shape[2], 1
)


from keras.utils import to_categorical

y_train_cat = to_categorical(y_train, 10)
y_test_cat = to_categorical(y_test, 10)


from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten

model = Sequential()
model.add(Conv2D(32, (4, 4), activation="relu", input_shape=x_train_norm[0].shape))
model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(128, activation="relu"))
model.add(Dense(10, activation="softmax"))

model.compile(
    optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"]
)
model.summary()

model.fit(x_train_norm, y_train_cat, epochs=2)


exit(0)
# plt.imshow(x_train[0])
# plt.show()
