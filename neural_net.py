import tensorflow as tf
import tflearn as tl
import numpy as np

LEARNING_RATE = 0.0005
TRAINING_ITERATIONS = 500000
VECTOR_LEN = 1575  # Must be the same length as the sound engine data!
MODEL_FILE = "neural_net.data"

########################################
#    CODE FOR PARSING CSV FILES AND    #
#       NEURAL NETWORK  TRAINING       #
########################################


def parse():
    """Reads CSV training files and saves them into memory."""

    return


def train(model, training_set):
    """Uses training data to train the neural network."""
    data = training_set[0]
    labels = training_set[1]
    total = len(data)
    for i in range(TRAINING_ITERATIONS):
        model.fit(data[i % total], labels[i % total], show_metric=True)
    return


def save(model):
    """Saves the model to be loaded for another session."""
    return

########################################
#   CODE FOR  READING FFT ARRAYS AND   #
#       OUTPUTTING RELEVANT DATA       #
########################################


def load_model():
    """Loads the previously saved model into memory."""
    return tl.DNN.load(MODEL_FILE)


def decide(sbyte):
    """Takes in a streamed FFT array and decides which notes are played."""
    return

########################################
# MAIN FUNCTIONS AND  HELPER FUNCTIONS #
########################################


def learn():
    """Parses CSV files and uses these files to train a neural net and saves this as a file."""
    net = tl.input_data([None, VECTOR_LEN])
    net = tl.lstm(net, 100, dropout=0.8)
    net = tl.fully_connected(net, 88, activation='softmax')
    net = tl.regression(net, optimizer='adam', learning_rate=LEARNING_RATE, loss='categorical_crossentropy')
    model = tl.DNN(net, tensorboard_verbose=0)
    train(model, parse())
    model.save(MODEL_FILE)
    return


def print_out():
    """Prints out the results of the learn() function."""
    return


if __name__ == "__main__":
    learn()
