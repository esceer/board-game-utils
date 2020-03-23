from dominion.config import Config


class Card:
    def __init__(self, name):
        self._name = name
        self._is_picked = False

    def get_name(self) -> str:
        return self._name

    def is_picked(self) -> bool:
        return self._is_picked

    def pick(self):
        self._is_picked = True
        return self

    def __str__(self):
        return self._name


class CardDeck:
    def __init__(self, config: Config):
        config = Config() if config is None else config
        self._deck = dict()
        self.deck_size = len(config.get_available_cards())
        for card_name in config.get_available_cards():
            self._deck[card_name] = Card(card_name)

    def get_deck_size(self) -> int:
        return self.deck_size

    def pick_property_card(self, selector) -> Card:
        card = self._fetch_card(selector)
        if card.is_picked():
            raise ValueError('Card is already picked')
        return self._deck[card.get_name()].pick()

    def _fetch_card(self, selector_attr) -> Card:
        card = selector_attr
        if isinstance(selector_attr, int):
            card = list(self._deck)[selector_attr]
        return self._deck[card]
