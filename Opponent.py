class OpponentNFLTeam:
    def __init__(self, name, location, wins, losses):
        self._name = name
        self._location = location
        self._wins = wins
        self._losses = losses

    # Getters
    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    @property
    def wins(self):
        return self._wins

    @property
    def losses(self):
        return self._losses

    # Setters
    @wins.setter
    def wins(self, value):
        self._wins = value

    @losses.setter
    def losses(self, value):
        self._losses = value

