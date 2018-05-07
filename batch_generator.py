import numpy as np
from keras import utils

class batch_generator(object):

    def __init__(self, data, iterations, batch_size, lexicon):
        self.data = data
        self.iterations = iterations
        self.batch_size = batch_size
        self.lexicon = lexicon
        self.current_index = 0

    def generate(self):
        x = np.zeros((self.batch_size, self.iterations))
        y = np.zeros((self.batch_size, self.iterations, self.lexicon))
        while True:
            for i in range(self.batch_size):
                if self.current_index + self.iterations >= len(self.data):
                    self.current_index = 0
                x[i, :] = self.data[self.current_index:self.current_index + self.iterations]
                temp_label = self.data[self.current_index + 1:self.current_index + self.iterations + 1]
                y[i, :, :] = utils.to_categorical(temp_label, num_classes=self.lexicon)
                self.current_index += 1
            yield x, y
