

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
       
        self.level = self.settings.play_level
        self.top_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit 
        self.score = 0

    def top_score(self):
        with open("high_score.txt", "r") as f:
            line = f.readlines()[0]
            self.high_score = int(line)

