class Player(object):
    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):
        return self._lives

    def _set_lives(self, live):
        if live >= 0:
            self._lives = live
            if live > 0:
                self._score += 1000
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        if self._level > 0:
            delta = level - self._level
            self._score += delta * 1000
            self._level = level

    lives = property(_get_lives, _set_lives)
    level = property(_get_level, _set_level)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if score >= 0:
            self._score = score
        else:
            print("Score cannot be negative")
            self._score = 0

    def __str__(self):
        return "Name: {0.name}, Lives: {0._lives}, Level: {0.level}, Score: {0.score}".format(self)