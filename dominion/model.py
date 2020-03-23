from dominion.config import Config


class Card:
    def __init__(self, name):
        self._name = name

    def get_name(self) -> str:
        return self._name


class CardDeck:
    def __init__(self, config: Config):
        config = Config() if config is None else config
        self._deck = dict()
        self.deck_size = len(config.get_available_cards())
        for card in config.get_available_cards():
            self._deck[card] = False

    def get_deck_size(self) -> int:
        return self.deck_size

    def pick_card(self, index: int) -> Card:
        card = list(self._deck)[index]
        if self._is_already_picked(card):
            raise ValueError("Card is already picked")
        self._deck[card] = True
        return card

    def _is_already_picked(self, card: Card) -> bool:
        return self._deck.get(card)
