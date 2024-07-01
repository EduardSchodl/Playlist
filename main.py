from __future__ import annotations

from playlist import Playlist
from track import Track


def inputTrack() -> Track | None:
    """
    Metoda od uživatele načte informace o skladbě a vrátí její objekt.
    V případě, že je název skladby prázdný nebo jsou zadány špatné údaje, vrátí None.

    :return: Instance skladby, nebo NoneType
    :rtype: Track | None
    """
    try:
        title: str = input()
        length: int = 0
        rating: float = 0

        if title == "":
            return None
        length: int = int(input())
        rating: float = float(input())

        return Track(title, length, rating)
    except:
        return None


def inputPlaylist() -> Playlist:
    """
    Metoda postupně volá funci pro vytváření skladeb, které jsou poté uloženy do listu.
    Poté, co přijde prázdný objekt NoneType, načítání se ukončí a metoda vrátí seznam skladeb.

    :return: Seznam skladeb
    :rtype: Playlist
    """
    track_list: list[Track] = list()

    while True:
        track = inputTrack()

        if track is None:
            break

        track_list.append(track)

    return Playlist(track_list)


def preparePlaylist(playlist: Playlist, minLength: int) -> Playlist:
    """
    Metoda vytvoří zamíchaný seznam nejlépe hodnocených skladeb.
    Celková délka těchto skladeb bude alespoň minLength a playlist vrátí.

    :param playlist: Původní seznam
    :type playlist: Playlist
    :param minLength: Minimální délka nového seznamu
    :type minLength: int

    :return: Nově vytvořený Playlist
    :rtype: Playlist
    """
    playlist.sortByRating()
    new_playlist = playlist.selectTotalLength(minLength)
    new_playlist.shuffle()
    return new_playlist


if __name__ == '__main__':
    minLength: int = 420
    playlist = inputPlaylist()
    print(playlist)
    print("-----------")
    new_playlist: Playlist = preparePlaylist(playlist, minLength)
    print(new_playlist)
    if new_playlist.totalLength < minLength:
        print("POZOR, JE KRATKY")

