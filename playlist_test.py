import inspect
import unittest
import random
from track import Track
from playlist import Playlist

class TestPlaylist(unittest.TestCase):
    def testConstructor(self):
        """
        - konstruktor vytvari melkou kopii predaneho seznamu
        - spravne pocita delku
        - str vraci spravny pocet radek
        """
        length = 0
        tracks:list[Track] = []
        for i in range(random.randint(5,10)):
            current_length = random.randint(5,500)
            tracks.append(Track(f"Track {i}", current_length, random.random()*4+1))
            length += current_length

        playlist = Playlist(tracks)
        
        self.assertEqual(playlist.totalLength, length)
        tracks.pop()
        self.assertEqual(playlist.totalLength, length)
        self.assertEqual(len(str(playlist).split('\n')), len(tracks)+2)

    def testStr(self):
        """
        - str vraci spravne informace
        """
        tracks = [
            Track("Track 1", 200, 4.75),
            Track("Track 2", 180, 2.2),
            Track("Track 3", 220, 3.3)
        ]
        playlist = Playlist(tracks)

        expected_output = (
            "Track 1 [3:20] (*****)\n"
            "Track 2 [3:00] (**)\n"
            "Track 3 [3:40] (***.)\n"
            "[10:00]"
        )

        self.assertEqual(str(playlist), expected_output)


    def assertNoBuiltInSort(self, playlist):
        method_source = inspect.getsource(playlist.sortByRating)
        self.assertNotIn('.sort(', method_source, "Built-in sort used...")

    def testSortByRating(self):
        """
        - razeni
        - nepouzivani funkce sort
        - predpoklada spravnou funkci __str__
        """
        tracks:list[Track] = []
        count = random.randint(5,10)
        for i in range(count):
            tracks.append(Track(f"Track {i}", random.randint(10,1000), ((count-i)/count)*4+1 ))
        playlist = Playlist(tracks)
        expected = str(playlist)
        
        random.shuffle(tracks)
        playlist = Playlist(tracks)
        playlist.sortByRating()
        self.assertNoBuiltInSort(playlist)
        self.assertEqual(expected, str(playlist))



    def assertNotUsedBuiltInShuffle(self, playlist_source):
        self.assertNotIn('random.shuffle(', playlist_source, "Built-in random.shuffle used")

    def testShuffleChanges(self):
        """
        - dvoje zamichani stop vraci ruzne vysledky
        - nepopuziva se random.shuffle
        """
        tracks:list[Track] = []
        count = random.randint(100,110)
        for i in range(count):
            tracks.append(Track(f"Track {i}", 1,1 ))

        playlist1 = Playlist(tracks)
        playlist1.shuffle()
        playlist2 = Playlist(tracks)
        playlist2.shuffle()

        self.assertNotEqual(str(playlist1), str(playlist2))
        
        shuffle_method_source = inspect.getsource(playlist1.shuffle)
        self.assertNotUsedBuiltInShuffle(shuffle_method_source)

    def testSelectTotalLengthMethod(self):
        tracks:list[Track] = []
        count = random.randint(100,110)
        for i in range(count):
            tracks.append(Track(f"Track {i}", random.randrange(1,10), 1 ))

        playlist = Playlist(tracks)
        original_playlist = Playlist(tracks)

        min_length = 5 + random.randint(20,30)
        selected_playlist = original_playlist.selectTotalLength(min_length)

        self.assertEqual(str(playlist), str(original_playlist))
        self.assertGreaterEqual(selected_playlist.totalLength, min_length)
        self.assertLessEqual(selected_playlist.totalLength, min_length + 10)
