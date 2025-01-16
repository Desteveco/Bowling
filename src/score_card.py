class Score_card:

    def __init__(self, rolls):
        self.rolls = rolls

    def total_score(self):
        return sum(self.rolls)