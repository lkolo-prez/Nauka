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
class Wieza:
    def __init__(self, kolor):
        self.kolor = kolor

    def dozwolone_ruchy(self, pozycja, szachownica):
        x, y = pozycja
        ruchy = []

        # Ruchy w poziomie
        for dx in range(-1, 2, 2):
            for nx in range(x + dx, 0 if dx < 0 else 8, dx):
                if szachownica.plansza[nx][y] == '':
                    ruchy.append((nx, y))
                else:
                    if szachownica.plansza[nx][y].kolor != self.kolor:
                        ruchy.append((nx, y))
                    break

        # Ruchy w pionie
        for dy in range(-1, 2, 2):
            for ny in range(y + dy, 0 if dy < 0 else 8, dy):
                if szachownica.plansza[x][ny] == '':
                    ruchy.append((x, ny))
                else:
                    if szachownica.plansza[x][ny].kolor != self.kolor:
                        ruchy.append((x, ny))
                    break

        return ruchy


class Gra:
    def __init__(self):
        self.szachownica = Szachownica()
        self.gracz_bialy = True  # True - gracz biały, False - gracz czarny

    def ruch(self, poczatek, koniec):
        x1, y1 = poczatek
        x2, y2 = koniec
        figura = self.szachownica.plansza[x1][y1]

        if figura == '':
            return False

        if figura.kolor != ('biały' if self.gracz_bialy else 'czarny'):
            return False

        ruchy = figura.dozwolone_ruchy(poczatek, self.szachownica)
        if (x2, y2) not in ruchy:
            return False

        self.szachownica.plansza[x1][y1] = ''
        self.szachownica.plansza[x2][y2] = figura
        self.gracz_bialy = not self.gracz_bialy
        return True
