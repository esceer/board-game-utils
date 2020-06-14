import random
import sys

from dominion.config import Config
from dominion.model import CardDeck


def pick_cards(deck: CardDeck, num_of_picks: int, pre_selected_cards=None):
    if pre_selected_cards is not None:
        num_of_picks -= len(pre_selected_cards)
        if num_of_picks < 0:
            raise ValueError('Too many cards picked')
        yield from pick_pre_selected_cards(deck, pre_selected_cards)
    yield from pick_random_property_cards(deck, num_of_picks)


def pick_pre_selected_cards(deck: CardDeck, pre_selected_cards: list):
    for pre_selected_card_name in pre_selected_cards:
        yield deck.pick_property_card(pre_selected_card_name)


def pick_random_property_cards(deck: CardDeck, num_of_picks: int):
    for pick in range(0, num_of_picks):
        while True:
            try:
                rnd_num = random.randint(0, deck.get_deck_size() - 1)
                yield deck.pick_property_card(rnd_num)
                break
            except ValueError:
                continue


if __name__ == '__main__':
    if len(sys.argv) > 2:
        print('Invalid arguments')
        print('Usage:')
        print('draw.py [comma-separated-pre-picks]')
        sys.exit(1)

    pre_selected_cards = set(sys.argv[1].split(',')) \
        if len(sys.argv) == 2 \
        else None

    config = Config()

    picked_cards = pick_cards(CardDeck(config), config.get_num_of_picks(), pre_selected_cards)
    for picked_card in sorted(picked_cards, key=lambda c: c.get_name()):
        print(picked_card)
