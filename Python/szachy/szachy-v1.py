class Szachownica:
    def __init__(self):
        self.plansza = [['' for _ in range(8)] for _ in range(8)]

class Goniec:
    def __init__(self, kolor):
        self.kolor = kolor

    def dozwolone_ruchy(self, pozycja, szachownica):
        x, y = pozycja
        ruchy = []

        for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                figura = szachownica[nx][ny]
                if figura == '':
                    ruchy.append((nx, ny))
                else:
                    if figura.kolor != self.kolor:
                        ruchy.append((nx, ny))
                    break
                nx += dx
                ny += dy

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

class Goniec:
    def __init__(self, kolor):
        self.kolor = kolor

    def dozwolone_ruchy(self, pozycja, szachownica):
        x, y = pozycja
        ruchy = []

        for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                figura = szachownica[nx][ny]
                if figura == '':
                    ruchy.append((nx, ny))
                else:
                    if figura.kolor != self.kolor:
                        ruchy.append((nx, ny))
                    break
                nx += dx
                ny += dy

        return ruchy

class Goniec:
    def __init__(self, kolor):
        self.kolor = kolor

    def dozwolone_ruchy(self, pozycja, szachownica):
        x, y = pozycja
        ruchy = []

        for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                figura = szachownica[nx][ny]
                if figura == '':
                    ruchy.append((nx, ny))
                else:
                    if figura.kolor != self.kolor:
                        ruchy.append((nx, ny))
                    break
                nx += dx
                ny += dy

        return ruchy
    
class Krol:
    def __init__(self, kolor):
        self.kolor = kolor

    def dozwolone_ruchy(self, pozycja, szachownica):
        x, y = pozycja
        ruchy = []

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx != 0 or dy != 0:  # Król nie może pozostać na swoim miejscu
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 8 and 0 <= ny < 8:
                        figura = szachownica[nx][ny]
                        if figura == '' or figura.kolor != self.kolor:
                            ruchy.append((nx, ny))

        return ruchy


class Hetman:
    def __init__(self, kolor):
        self.kolor = kolor

    def dozwolone_ruchy(self, pozycja, szachownica):
        ruchy = []

        # Hetman łączy ruchy gonca i wieży
        goniec = Goniec(self.kolor)
        wieza = Wieza(self.kolor)
        ruchy.extend(goniec.dozwolone_ruchy(pozycja, szachownica))
        ruchy.extend(wieza.dozwolone_ruchy(pozycja, szachownica))

        return ruchy

def czy_szach(kolor, szachownica):
    # Wyszukaj pozycje króla
    for x in range(8):
        for y in range(8):
            figura = szachownica[x][y]
            if isinstance(figura, Krol) and figura.kolor == kolor:
                krol_pozycja = (x, y)
                break

    przeciwnik = 'czarny' if kolor == 'biały' else 'biały'

    # Sprawdź czy przeciwnik może zaatakować króla
    for x in range(8):
        for y in range(8):
            figura = szachownica[x][y]
            if figura != '' and figura.kolor == przeciwnik:
                ruchy = figura.dozwolone_ruchy((x, y), szachownica)
                if krol_pozycja in ruchy:
                    return True

    return False

def czy_szach_mat(kolor, szachownica):
    for x in range(8):
        for y in range(8):
            figura = szachownica[x][y]
            if figura != '' and figura.kolor == kolor:
                ruchy = figura.dozwolone_ruchy((x, y), szachownica)
                for ruch in ruchy:
                    # Wykonaj próbny ruch
                    szachownica_docelowa = [wiersz[:] for wiersz in szachownica]
                    szachownica_docelowa[ruch[0]][ruch[1]] = szachownica[x][y]
                    szachownica_docelowa[x][y] = ''

                    # Sprawdź czy w wyniku ruchu król nie jest szachowany
                    if not czy_szach(kolor, szachownica_docelowa):
                        return False

    return True

def czy_pat(kolor, szachownica):
    if not czy_szach(kolor, szachownica):
        return czy_szach_mat(kolor, szachownica)
    return False



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
