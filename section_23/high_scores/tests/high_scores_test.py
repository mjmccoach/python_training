import unittest

from src.high_scores import latest, personal_best, personal_top_three, high_to_low

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):

    # Tests

    # Test latest score (the last thing in the list)
    def test_latest_score(self): 
        self.assertEqual(90,latest([85,86,87,88,89,90]))
    # Test personal best (the highest score in the list)
    def test_highest_score(self):
        self.assertEqual(98, personal_best([85,86,87,98,89,90]))

    # Test top three from list of scores
    def test_top_three(self):
        self.assertEqual([95, 94, 93], personal_top_three([95, 88, 87, 90, 93 ,94]))

    # Test ordered from highest tp lowest
    def test_high_to_low(self):
        self.assertEqual([94,93,92], high_to_low([93, 92, 94]))

    # Test top three when there is a tie
    def test_test_top_three_tie(self):
        self.assertEqual([95, 94, 94], personal_top_three([93, 94, 94, 95]))

    # Test top three when there are less than three
    def test_top_three_less_than_3(self):
        self.assertEqual([93, 92], personal_top_three([92,93]))

    # Test top three when there is only one
