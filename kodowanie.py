

import math


class AskiiNieAskii:

    def __init__(self):
        self.wez_p = []
        self.daj_p = []

    def tekst_na_askii(self, tekst):
        self.wez_p = [ord(c) for c in tekst]
        for i in range(len(self.wez_p)):
            if self.wez_p[i] < 10:
                self.wez_p[i] = str(self.wez_p[i])
                self.wez_p[i] = '00' + str(self.wez_p[i])
            if self.wez_p[i] < 100:
                self.wez_p[i] = str(self.wez_p[i])
                self.wez_p[i] = '0' + str(self.wez_p[i])

        kod = ''.join(map(str, self.wez_p))
        self.wez_p.clear()
        return kod

    def aski_na_tekst(self, liczba):
        for i in range(0, len(liczba), 3):
            self.daj_p.append(int(liczba[i:i + 3]))
        tekst = ''.join(chr(i) for i in self.daj_p)
        self.daj_p.clear()
        return tekst


class KodujOdkoduj(AskiiNieAskii):
    key = 0
    a = AskiiNieAskii()

    def koduj(self, tekst):
        askii = a.tekst_na_askii(tekst)

        kod = askii
        return kod

    def odkodowanie(self, kod):
        wynik = kod

        tekst = a.aski_na_tekst(wynik)
        return tekst


p = 'Wiktoria Płaszczyk'

a = AskiiNieAskii()
aa = KodujOdkoduj()

b = a.tekst_na_askii(p)
c = a.aski_na_tekst(b)
bb = aa.koduj(p)
cc = aa.odkodowanie(bb)

print(b)
print(c)
print(bb)
print(cc)


