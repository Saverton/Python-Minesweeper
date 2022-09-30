
class GameOverException(Exception):
    
    def __init__(self, message="Game ended unexpectedly"):
        self.message = message

    def __str__(self):
        return self.message