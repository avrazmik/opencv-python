import numpy as np
from numpy import genfromtxt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

from keras.models import Sequential
from keras.layers import Dense

from sklearn.metrics import confusion_matrix

PATH = "C:/Users/Y9ESEH724/cv/img/Computer-Vision-with-Python/DATA/bank_note_data.txt"
data = genfromtxt(PATH, delimiter=",")

X = data[:, 0:4]
y = np.int0(data[:, -1])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.33, random_state=42
)

scaler = MinMaxScaler()
scaler.fit(X_train)
scaled_X_train = scaler.transform(X_train)
scaled_X_test = scaler.transform(X_test)


model = Sequential()
model.add(Dense(4, activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(1, activation="sigmoid"))
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(scaled_X_train, y_train, epochs=50, verbose=2)
y_prob = model.predict(scaled_X_test)
y_prob = y_prob.reshape((y_prob.shape[0]))
y_prob = np.where(y_prob > 0.5, 1, 0)

print(confusion_matrix(y_test, y_prob))
