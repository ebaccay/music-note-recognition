import neural_net as nn
import sound_engine as se


def main():
    nn.load_model()
    while True:
        sound_byte = se.stream()
        nn.decide(sound_byte)
