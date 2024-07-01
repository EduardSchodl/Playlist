import random
import unittest
from track import Track


class TestTrack(unittest.TestCase):
    def assertLength(self, minutes: int, seconds: int):
        formatted_time = f'{minutes}:{seconds:02d}'
        total_seconds = minutes * 60 + seconds

        track = Track("Random Song", total_seconds, 3.5)  # Arbitrary rating for the example

        self.assertEqual(str(track), f'Random Song [{formatted_time}] (***.)')

    def testLength(self):
        # Predefined tests
        self.assertLength(1, 0)
        self.assertLength(59, 59)
        self.assertLength(120, 30)

        # Randomly generated tests
        for _ in range(5):
            random_minutes = random.randint(1, 10)
            random_seconds = random.randint(0, 59)
            self.assertLength(random_minutes, random_seconds)

    def assertTitle(self, title: str):
        track = Track(title, 180, 4.2)  
        self.assertEqual(str(track), f'{title} [3:00] (****)')

    def testTitle(self):
        self.assertTitle("Song 1")
        self.assertTitle("Amazing Track")
        self.assertTitle("Random Title")

        for _ in range(5):
            random_title = f'Title_{random.randint(1, 100)}'
            self.assertTitle(random_title)


    def assertRating(self, rating: float, expected_ending: str):        
        formatted_rating = "*" * int(rating) + expected_ending

        track = Track("Random Song", 3599, rating)  

        self.assertEqual(str(track), f'Random Song [59:59] ({formatted_rating})')

    def testRating(self):
        self.assertRating(0.0, "")
        self.assertRating(4.25, ".")
        self.assertRating(3.75, "*")
        self.assertRating(5.0, "")

        self.assertRating(random.randint(0, 4) + random.random()*0.25, "")
        self.assertRating(random.randint(0, 4) + 0.25 + random.random()*0.5, ".")
        self.assertRating(random.randint(0, 4) + +0.75 + random.random()*0.25, "*")
