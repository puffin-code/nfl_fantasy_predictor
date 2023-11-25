import os
import Opponent

class GameStats:
    def __init__(self, date, opponent, name, touchdowns, yards_receiving, yards_rushing, carries, targets, game_date, opponent):
        self._name = name
        self._date = date
        self._opponent = opponent
        self._touchdowns = touchdowns
        self._yards_receiving = yards_receiving
        self._yards_rushing = yards_rushing
        self._carries = carries
        self._targets = targets
        self._game_date = datetime.strptime(game_date, '%Y-%m-%d')
        #other metrics to add in the future:
            #-opposition record
            #-weather
            #-opposition rank in defense

    # Getters
    @property
    def name(self):
        return self._name

    @property
    def date(self):
        return self._date

    @property
    def opponent(self):
        return self._opponent

    @property
    def touchdowns(self):
        return self._touchdowns
 
    @property
    def yards_receiving(self):
        return self._yards_receiving

    @property
    def yards_rushing(self):
            return self._yards_rushing

    @property
    def carries(self):
            return self._carries

    @property
    def targets(self):
        return self._targets

    @property
    def game_date(self):
        return self._game_date




