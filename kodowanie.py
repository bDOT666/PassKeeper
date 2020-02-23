

def aaaaa():
    pass


class AskiiNieAskii:

    def __init__(self):
        self.wez_p = []
        self.daj_p = []
        self.key = 0

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

    # Obrubka danych zankońcozna, można kodować(Y)

    def koduj(self, tekst):
        askii = self.tekst_na_askii(tekst)

        kod = askii
        return kod

    def odkodowanie(self, kod):
        wynik = kod

        tekst = self.aski_na_tekst(wynik)
        return tekst


p = 'Wiktoria Płaszczyk'

a = AskiiNieAskii()

b = a.koduj(p)
c = a.odkodowanie(b)

print(p)
print(b)
print(c)


