class Scoring:
    def __init__(self, points_per_reception=1.0, points_per_passing_yard=0.04, points_per_rushing_yard=0.1, points_per_receiving_yard=0.1, points_per_passing_TD=4, points_per_rushing_TD=6, points_per_receiving_TD=6):
        self.points_per_reception = points_per_reception
        self.points_per_passing_yard = points_per_passing_yard
        self.points_per_rushing_yard = points_per_rushing_yard
        self.points_per_receiving_yard = points_per_receiving_yard
        self.points_per_passing_TD = points_per_passing_TD
        self.points_per_rushing_TD = points_per_rushing_TD
        self.points_per_receiving_TD = points_per_receiving_TD