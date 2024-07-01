from __future__ import annotations

import random

from track import Track


class Playlist:
    """
    Třída Playlist reprezentuje seznam skladeb.

    @Author: Eduard Schödl
    @Date: 231205
    """

    def __init__(self, tracks: list[Track]):
        """
        Konstruktor třídy "Playlist". Vytvoří nový objekt typu Playlist a hlubokou kopii předaného seznamu.

        :param title: Název skladby
        :type title: str
        :param length: Délka skladby
        :type length: int
        :param rating: Hodnocení skladby
        :type rating: float
        """
        self.__tracks = tracks.copy()

    def __str__(self):
        """
        Metoda vrací formátovaný seznamu skladeb.

        :return: Formátovaný seznam skladeb
        :rtype: str
        """
        result_string: str = ""

        for track in self.__tracks:
            result_string += track.__str__() + "\n"

        result_string += f"[{self.totalLength // 60}:{str(self.totalLength % 60).zfill(2)}]"

        return result_string

    @property
    def totalLength(self) -> int:
        """
        Metoda vrací celkovou délku v sekundách všech skladeb v seznamu dohromady.

        :return: Celková délka seznamu v sekundách
        :rtype: int
        """
        total_length: int = 0

        for track in self.__tracks:
            total_length += track.length

        return total_length

    def sortByRating(self):
        """
        Metoda seřadí skladby v playlistu podle jejich hodnocení sestupně.
        Použita je metoda Insertion sort

        """
        arr_length = len(self.__tracks)
        if not arr_length == 0 or arr_length == 1:
            for i in range(1, arr_length):
                key = self.__tracks[i]
                j = i - 1
                while j >= 0 and key.rating > self.__tracks[j].rating:
                    self.__tracks[j + 1] = self.__tracks[j]
                    j -= 1
                self.__tracks[j + 1] = key

    def shuffle(self):
        """
        Metoda náhodně proháže pořadí stop.
        Pro každou stopu se vygeneruje náhodný nový index a s danou skladbou se prohodí.

        """
        for i in range(0, len(self.__tracks) - 1):
            random_int: int = random.randint(0, len(self.__tracks) - 1)
            (self.__tracks[i], self.__tracks[random_int]) = (self.__tracks[random_int], self.__tracks[i])

    def selectTotalLength(self, minLength: int) -> Playlist:
        """
        Metoda na základě předané minimální délky vygeneruje nový seznam skladeb.
        Tento seznam obsahuje přesný počet skladeb, jejichž celková délka se rovná nebo je větší než předaný parametr.
        Takový seznam neobsahuje ani jednu stopu navíc.
        V případě, že je skladeb nedostatek, vrátí se všechny skladby.

        :param minLength: Minimální délka nově vytvořeného seznamu v sekundách
        :type minLength: int

        :return: Nově vytvořený seznam
        :rtype: Playlist
        """
        if self.totalLength <= minLength:
            new_playlist = Playlist(self.__tracks)
            return new_playlist
        else:
            track_list: list[Track] = list()
            total_length: int = 0
            for track in self.__tracks:
                track_list.append(track)
                total_length += track.length

                if total_length >= minLength:
                    return Playlist(track_list)
