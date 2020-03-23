from dominion.config import Config
from dominion.model import CardDeck
import random

num_of_picks = 10


def pick_cards():
    deck = CardDeck(config)
    for pick in range(0, num_of_picks):
        while True:
            try:
                rnd_num = random.randint(0, deck.get_deck_size() - 1)
                yield deck.pick_card(rnd_num)
                break
            except ValueError:
                continue


if __name__ == '__main__':
    config = Config()
    for picked_card in pick_cards():
        print(picked_card)
