import os
import Opponent
from Scoring import Scoring
import datetime

class GameStats:
    def __init__(self, date, opponent, name, passing_touchdowns, 
                 rushing_touchdowns, receiving_touchdowns, 
                 yards_passing, yards_receiving, yards_rushing, 
                 carries, targets, game_date):
        self._name = name
        self._date = date
        self._opponent = opponent
        self._passing_touchdowns = passing_touchdowns
        self._rushing_touchdowns = rushing_touchdowns
        self._receiving_touchdowns = receiving_touchdowns
        self._yards_passing = yards_passing
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
    def passing_touchdowns(self):
        return self._passing_touchdowns
    
    @property
    def receiving_touchdowns(self):
        return self._receiving_touchdowns
    
    @property
    def rushing_touchdowns(self):
        return self._rushing_touchdowns

    @property
    def yards_passing(self):
        return self._yards_passing

    @property
    def yards_receiving(self):
        return self._yards_receiving

    @property
    def yards_rushing(self):
            return self._yards_rushing
    
    @property
    def yards_passing(self):
            return self._yards_passing

    @property
    def carries(self):
            return self._carries

    @property
    def targets(self):
        return self._targets

    @property
    def game_date(self):
        return self._game_date

    def calculate_game_score(self, scoring: Scoring):
        total_score = (scoring.points_per_reception * self._receptions +
                    scoring.points_per_passing_yard * self._passing_yards +
                    scoring.points_per_rushing_yard * self._rushing_yards +
                    scoring.points_per_receiving_yard * self._receiving_yards +
                    scoring.points_per_passing_TD * self._passing_TDs +
                    scoring.points_per_rushing_TD * self._rushing_TDs +
                    scoring.points_per_receiving_TD * self._receiving_TDs)




