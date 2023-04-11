class Szachownica:
    def __init__(self):
        self.plansza = [['' for _ in range(8)] for _ in range(8)]

class Pionek:
    def __init__(self, kolor):
        self.kolor = kolor

    def dozwolone_ruchy(self, pozycja):
        x, y = pozycja
        ruchy = []
        if self.kolor == 'biały':
            if x - 1 >= 0:
                ruchy.append((x - 1, y))
            if x == 6:
                ruchy.append((x - 2, y))
        else:  # kolor == 'czarny'
            if x + 1 < 8:
                ruchy.append((x + 1, y))
            if x == 1:
                ruchy.append((x + 2, y))

        return ruchy
