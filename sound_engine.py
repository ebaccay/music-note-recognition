import os
import scipy.io.wavfile as w
import numpy as np
import matplotlib.pyplot as plt

CUTOFF_LEN = 15750  # Useful to have a specified cutoff as to not pass in huge vectors to TensorFlow
PRIMING_DIR = "./training_data/raw_data/to_be_primed/"
FINISHED_DIR = "./training_data/raw_data/primed/"
TRAINING_FILE = "batch1.csv"
SQUISH_RATIO = 10

"""
NOTE: ANY NOTE ABOVE C7 CANNOT BE SAMPLED USING THE KAGGLE DATASET
"""

########################################
#  CODE FOR GENERATING  TRAINING DATA  #
#           FROM SOUND BYTES           #
########################################


def read(wav, folder=PRIMING_DIR):
    """Reads a given sound byte and converts to a 1575-length array."""
    sfreq, sound = w.read(folder + wav)
    # print(wav + " has a sampling frequency of " + str(sfreq)) # Used for debugging to show frequencies of files
    return sound


def save_csv(sbyte, file, label):
    length = len(sbyte)
    new_line = ""
    for i in range(length - 2):
        new_line += str(sbyte[i]) + ','
    file.write(new_line + str(sbyte[length - 1]) + '\n')
    file.write(label + '\n')
    return

########################################
#   CODE FOR RUNNING REAL TIME SOUND   #
#  BYTE GENERATION AND TRANSFORMATION  #
########################################


def listen():
    """Streams audio from the microphone and converts to a 1575-length array."""
    return

########################################
# MAIN FUNCTIONS AND  HELPER FUNCTIONS #
########################################

def prime():
    """Converts training data from audio files into FFT arrays in a CSV file for later parsing."""
    ndict, vdict = note_dictionary()
    raw_files = os.listdir(PRIMING_DIR)
    try:
        new_file = open(TRAINING_FILE, 'x')
    except FileExistsError:
        os.remove(TRAINING_FILE)
        new_file = open(TRAINING_FILE, 'x')
    test = []
    for f in raw_files:
        sbyte = squish(FFT(read(f)))
        # visualize(sbyte)  # Used for visualizing the debugging sound bytes when necessary.
        save_csv(sbyte, new_file, str(ndict[f[:-4]]))  # Gotta save the data somewhere.
        # os.rename(PRIMING_DIR + f, FINISHED_DIR + f)  # Because moving around data set files is a hassle.
        test.append(ndict[f[:-4]])  # To track which notes are accounted for and which aren't.
    print(sorted(test))  # Display all notes read
    new_file.close()
    return

def stream():
    """Streams audio from the microphone and converts to a FFT array for the neural network."""
    return


def visualize(*array):
    """Visualizes audio files in either the time-pressure domain or the frequency domain."""
    for a in array:
        plt.plot(a)
    plt.show()
    return


def FFT(sound_byte):
    """Primes a sound_byte through a FFT."""
    sound_byte = np.matrix.flatten(sound_byte)
    sound_byte = np.fft.fft(sound_byte)
    sound_byte = np.real(sound_byte)
    return sound_byte[:CUTOFF_LEN]


def squish(sound_byte):
    """'Squishes' a sound byte from a ridiculously large input vector to a more manageable size."""
    new_byte = []
    length = len(sound_byte)
    i = 0
    while i < length:
        j = 0
        sum = 0
        while j < SQUISH_RATIO:
            sum += sound_byte[i]
            j += 1
            i += 1
        new_byte.append(sum / SQUISH_RATIO)
    return new_byte


def note_dictionary():
    """Initializes a dictionary mapping of note names to vector names, i.e. C4 |--> 39 and A0 |--> 0 as well as the
        inverse mapping."""
    ndict, vdict = {}, {}
    notes = ["a", "a#", "b", "c", "c#", "d", "d#", "e", "f", "f#", "g", "#g"]
    for i in range(88):
        name = notes[i % 12] + str((i + 9) // 12)
        ndict[name] = i
        vdict[i] = name
    return ndict, vdict


if __name__ == "__main__":
    prime()
