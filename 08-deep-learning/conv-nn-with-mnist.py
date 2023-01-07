from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPool2D, Flatten


model = Sequential()
model.add(Conv2D(32, kernel_size=(4, 4), activation="relu", input_shape=(28, 28, 1)))
model.add(MaxPool2D())
model.add(Flatten())
model.add(Dense(128, activation="relu"))
model.add(Dense(10, activation="softmax"))
model.compile(
    loss="categorical_crossentropy", optimizer="rmsprop", metrics=["accuracy"]
)
model.summary()


from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

import matplotlib.pyplot as plt

# single_image = x_train[0]
# plt.imshow(single_image, cmap="gray_r")


from keras.utils.np_utils import to_categorical


y_cat_train = to_categorical(y_train, 10)
y_cat_test = to_categorical(y_test, 10)

x_norm_train = x_train / x_train.max()
x_norm_test = x_test / x_test.max()


x_norm_train = x_norm_train.reshape(60000, 28, 28, 1)
x_norm_test = x_norm_test.reshape(10000, 28, 28, 1)


model.fit(x_norm_train, y_cat_train, epochs=2)

y_pred = model.predict(x_test)
print(model.metrics_names)

exit(0)
