import configparser


class Config:
    def __init__(self):
        self._config = self._parse_config_file('dominion.ini')

    @staticmethod
    def _parse_config_file(config_dir) -> configparser.ConfigParser:
        config = configparser.ConfigParser()
        config.read(config_dir)
        return config

    def get_available_cards(self) -> list:
        return self._config['Cards']['available-property-cards'].split(',')

    def get_num_of_picks(self) -> int:
        return int(self._config['Cards']['number-of-property-picks'])
