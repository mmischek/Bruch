class Bruch(object):


    def __init__(self, zaehler=0, nenner=1):
        """
        Konstruktor
        :raise TypeError: Zahler und Nenner muessen int sein
        :param zaehler: int
        :param nenner: int
        """
        if nenner < 0 and zaehler < 0:
            nenner *= (-1)
            zaehler *= (-1)
        if isinstance(zaehler, Bruch):
            self.zaehler, self.nenner = zaehler
            return
        elif type(zaehler) is not int:
            raise TypeError('zaehler muss int sein')
        elif type(nenner) is not int:
            raise TypeError('nenner muss int sein')
        if nenner == 0:
            raise ZeroDivisionError
        self.zaehler = zaehler
        self.nenner = nenner


    def __int__(self):
        """
        Wandelt in int um
        :return: zaehler/nenner als int
        """
        return int(self.zaehler / self.nenner)


    def __float__(self):
        """
         Wandelt in float um
        :return: zaehler/nenner als float
        """
        return float(self.zaehler / self.nenner)

    def __complex__(self):
        """
        Wandelt in complex um
        :return: zaehler/nenner als complex
        """
        return complex(self.zaehler / self.nenner)

    def __eq__(self, other):
        """
        ueberprueft ob brueche gleich sidn
        :return: true wenn Brueche gleich sind
        """
        if float(self) == float(other):
            return True

    def __lt__(self, other):
        """
        ueberprueft ob self kleiner las other ist
        :return: true wenn self kleiner ist als other
        """
        if float(self) < float(other):
            return True

    def __le__(self, other):
        """
        ueberprueft ob self kleiner oder gleich als other ist
        :return: true wenn self kleiner oder gleich ist als other
        """
        if float(self) <= float(other):
            return True

    def __gt__(self, other):
        """
        ueberprueft ob self groesser als other ist
        :return: true wenn self gruesser als other ist
        """
        if float(self) > float(other):
            return True

    def __ge__(self, other):
        """
        eberprueft ob self groesser oder gleich als other ist
        :return: true wenn self groesser oder gleich als other ist
        """
        if float(self) >= float(other):
            return True

    def __invert__(self):
        """
        tauscht nenner und zaehler
        :return: nenner und zahler vertauscht
        """
        return Bruch(self.nenner,self.zaehler)

    def __str__(self):
        """
        wandelt in String um
        :return: string
         """
        if self.nenner == 1:
            return '(%s)' % (str(self.zaehler))
        else:
            return '(%s/%s)' % (str(self.zaehler), str(self.nenner))

    def __pow__(self, hoch):
        """
        bruch hoch xx
        :return: Bruch hoch xx
        """
        return Bruch(self.zaehler ** hoch,self.nenner ** hoch)

    def __abs__(self):
        """
        absoluter Bruch
        :return: positiver bruch
        """
        return Bruch(abs(self.zaehler),abs(self.nenner))

    def __neg__(self):
        """
        zaehler mit - multipizieren
        :return: bruch
        """
        return Bruch(self.zaehler*-1, self.nenner)


    @staticmethod
    def _Bruch__makeBruch(other):
        """
        erzeugt einen bruch
        :param bruch
        :return: bruch
        """
        return Bruch(other,1)


    def __add__(self, other):
        """
        Wenn es sich um int handelt, kann einfach addiert werden
        Wenn es sich um zwei Brueche handelt muss den Groessten gemeinsamen Nenner gefunden werden
        :return: Bruch
        """
        if(isinstance(other,int)):
            return Bruch(self.zaehler+(self.nenner*other),self.nenner)
        elif(isinstance(other,Bruch)):
            zs = self.zaehler
            zo = other.zaehler

            #ermittele Groessten gemeinsamen Nenner
            if self.nenner > other.nenner:
                gg = self.nenner
            else:
                gg = other.nenner
            while (True):
                if ((gg % self.nenner == 0) and (gg % other.nenner == 0)):
                    ggt = gg
                    break
                gg += 1

            newn = ggt
            zs *= newn / self.nenner
            zo *= newn / other.nenner
            return Bruch(int(zs+zo),newn)
        else:
            raise TypeError("Fehler")

    def __iadd__(self, other):
            """
            Zahl zu Bruch addieren
            :param other: Zahl welche dazu addiert werden soll
            :return: Bruch
            """
            return Bruch(self) + other

    def __radd__(self, other):
            """
            Zahl zu Bruch addieren
            :param other: Zahl welche dazu addiert werden soll
            :return: Bruch
            """
            return Bruch(other) + self


    def __sub__(self, zaehler):
        """
        Verwende add methode und rechne * -1 = subtraktion
        :return: Bruch
        """
        return self.__add__(zaehler * -1)


    def __isub__(self, other):
        """
        Bruch mit einer Zahl subtrahiert
        :param other: Zahl welche abgezogen werden soll
        :return: Bruch
        """
        return Bruch(self) - other

    def __rsub__(self, other):
        """
        Bruch mit einer Zahl subtrahiert
        :param other: Zahl welche abgezogen werden soll
        :return: Bruch
        """
        return Bruch(other) - self


    def __truediv__(self, other):
        """
        aussen * aussen / innen * innen
        :param other: bruch oder int
        :return: Bruch
        """
        if(isinstance(other,Bruch)):
            return Bruch(self.zaehler*other.nenner,self.nenner*other.zaehler)
        elif(isinstance(other,int)):
            return self / Bruch(other)
        elif(other == 0):
            raise ZeroDivisionError
        else:
            raise TypeError("Fehler")

    def __itruediv__(self, other):
        """
        Bruch druch Zahl dividieren
        :return: Bruch
        """
        return self / other

    def __rtruediv__(self, other):
        """
        Bruch druch Zahl dividieren
        :return: Bruch
        """
        return Bruch(other) / self

    def __iter__(self):
        """
        Macht die Klasse iterierbar
        """
        for i in self.zaehler,self.nenner:
            yield i

    def __mul__(self, other):
        """
        Mulitipliziert Bruch * bruch oder Bruch * int
        :return: Bruch
        """
        if(isinstance(other,Bruch)):
            return Bruch(self.zaehler * other.zaehler, self.nenner*other.nenner)
        if(isinstance(other,int)):
            return self * Bruch(other)
        else:
            raise TypeError("Fehler")

    def __rmul__(self, other):
        """
        Bruch Mulitpliziert mit other
        :return: Bruch
        """
        return self.__mul__(other)

    def __imul__(self, other):
        """
        Self mulitpliziert mit other
        :return: Bruch
        """
        return self * other