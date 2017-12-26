import neural_net as nn
import sound_engine as se


def main():
    nn.load_model()
    while True:
        sound_byte = se.steam()
        note = nn.decide(sound_byte)
        nn.print_out(note)
