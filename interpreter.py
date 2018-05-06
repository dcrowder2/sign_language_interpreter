from math import sqrt
from matplotlib import pyplot
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import numpy as np


# Runs the lstm using keras
def run_lstm(training, expected, batch_size, num_epochs, neurons):
    model = Sequential()
    model.add(LSTM(neurons, batch_input_shape=(batch_size, training.shape[1], training.shape[2]), stateful=True))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    for i in range(num_epochs):
        model.fit(training, expected, epochs=1, batch_size=batch_size, verbose=0, shuffle=False)
        model.reset_states()
    return model


# Make a guess to what sign is signed via the lstm model
def guess_sign(model, data, batch_size):
    in_data = data.reshape(1, 1, len(data))
    guess = model.predict(in_data, batch_size=batch_size)
    return guess[0, 0]


def init():
    return np.load("sign_data.npy")


if __name__ == '__main__':
    data = init()
