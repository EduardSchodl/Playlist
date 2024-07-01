import math


class Track:
    """
    Třída Track reprezentuje skladbu, stopu.

    @Author: Eduard Schödl
    @Date: 231205
    """
    def __init__(self, title: str, length: int, rating: float):
        """
        Konstruktor třídy "Track". Vytvoří nový objekt typu Track.

        :param title: Název skladby
        :type title: str
        :param length: Délka skladby
        :type length: int
        :param rating: Hodnocení skladby
        :type rating: float
        """
        self.__title = title
        self.__length = length
        self.__rating = rating

    def __str__(self) -> str:
        """
        Metoda vrací formátovaný výpis skladby.
        Formát: title [length] (rating)

        :return: Formátovaný řetězec
        :rtype: str
        """
        return f"{self.__title} [{self.__formatLength(self.__length)}] ({self.__convertRating(self.__rating)})"

    @property
    def title(self) -> str:
        """
        Metoda vrací název skladby.

        :return: Název skladby
        :rtype: str
        """
        return self.__title

    @property
    def length(self) -> int:
        """
        Metoda vrací název skladby v sekundách.

        :return: Délka skladby v sekundách
        :rtype: int
        """
        return self.__length

    @property
    def rating(self) -> float:
        """
        Metoda vrací hodnocení skladby.

        :return: Hodnocení skladby
        :rtype: float
        """
        return self.__rating

    def __formatLength(self, length: int) -> str:
        """
        Metoda předanou délku skladby přepočítá na minuty a sekundy a vrátí.
        Formát: min:sek

        :param length: Délka skladby v sekundách
        :type length: int

        :return: Formátovaná délka skladby
        :rtype: str
        """
        return f"{length//60}:{str(length%60).zfill(2)}"

    def __convertRating(self, rating: float) -> str:
        """
        Metoada předané hodnocení skladby přepočítá na počet * a vrátí.

        :param rating: Hodnocení skladby
        :type rating: float

        :return: Formátované hodnocení skladby
        :rtype: str
        """
        dec, whole_part = math.modf(rating)
        converted: str = "*" * int(whole_part)

        if dec >= 0.75:
            converted += "*"
        elif dec >= 0.25:
            converted += "."
        return converted
