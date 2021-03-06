"""
Manage a game player's High Score list.

Your task is to build a high-score component of the classic Frogger game,
one of the highest selling and addictive games of all time,
and a classic of the arcade era.

Your task is to write methods that return the highest score from the list,
the last added score, the three highest scores,
and a report on the difference between the last and the highest scores.
"""

from random import randint


def generate_scores(scores_num):
    scores_list = list()
    while len(scores_list) < scores_num:
        random_int = randint(0, 100)
        if random_int % 10 == 0:
            scores_list.append(random_int)
    return scores_list


class HighScores:
    def __init__(self, scores):
        self.scores = scores

    # shows the full scores list:
    def show_scores(self):
        return self.scores

    # highest score from the list:
    def personal_best(self):
        return max(self.scores)

    # the last added score:
    def latest(self):

        return self.scores[-1]

    # the three highest scores:
    def personal_top(self):
        return sorted(self.scores, reverse=True)[:3]

    # the difference between the last and the highest scores:
    def last_minus_highest(self):
        return self.personal_best() - self.last_added()

    # Reports custom information about some scores:
    def report(self):
        if self.latest() < self.personal_best():
            return f"Your latest score was {self.latest()}. That's {(self.personal_best() - self.latest())} short of your personal best!"
        if self.latest() == self.personal_best():
            return f"Your latest score was {self.latest()}. That's your personal best!"
