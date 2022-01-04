import json


class GameStats():
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True

        data = self.load_dictionary()

        self.high_score = data['high_score']

    def update_high_score(self, high_score):
        self.high_score = high_score

        data = {
            'high_score': self.high_score
        }
        self.save_dictionary(data)

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.game_active = False
        self.score = 0
        self.level = 1

    def save_dictionary(self, data_dict: dict):
        with open(self.settings.record_file_path, 'w') as f:
            json.dump(data_dict, f)

    def load_dictionary(self) -> dict:
        with open(self.settings.record_file_path, 'r') as f:
            return json.load(f)
