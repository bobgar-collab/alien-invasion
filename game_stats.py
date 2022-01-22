from game_state import GameState
from utils import load_dictionary, save_dictionary


class GameStats():

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        data = load_dictionary(self.settings.record_file_path)

        self.high_score = data['high_score']

    def update_high_score(self, high_score):
        self.high_score = high_score

        data = {
            'high_score': self.high_score
        }

        save_dictionary(self.settings.record_file_path, data)

    def reset_stats(self):
        self.game_state = GameState.STOP
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
