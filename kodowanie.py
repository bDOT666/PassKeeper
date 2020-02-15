import math

p = 'Wiktoria Płaszczyk'
print(p)
wez_p = [ord(c) for c in p]

print(wez_p)

"""
Ascii na liczbe
"""

for i in range(len(wez_p)):
    if wez_p[i] < 10:
        wez_p[i] = str(wez_p[i])
        wez_p[i] = '00' + str(wez_p[i])
    if wez_p[i] <100:
        wez_p[i] = str(wez_p[i])
        wez_p[i] = '0' + str(wez_p[i])

a = ''.join(map(str, wez_p))
print(a)


b = []
for i in range(0, len(a), 3):
    b.append(int(a[i:i + 3]))
print(b)

daj_p = ''.join(chr(i) for i in b)
print(daj_p)


class KodowanieOdkodowania:
    key = 0

    def __init__(self):
        self.wez_p = []
        self.daj_p = []

    def tekst_na_askii(self, tekst):
        self.wez_p = [ord(c) for c in tekst]
        for i in range(len(self.wez_p)):
            if wez_p[i] < 10:
                self.wez_p[i] = str(self.wez_p[i])
                self.wez_p[i] = '00' + str(self.wez_p[i])
            if self.wez_p[i] < 100:
                self.wez_p[i] = str(wez_p[i])
                self.wez_p[i] = '0' + str(self.wez_p[i])

        return int(''.join(map(str, self.wez_p)))

    def aski_na_tekst(self, liczba):
        for i in range(0, len(liczba), 3):
            self.daj_p.append(int(liczba[i:i + 3]))

        return ''.join(chr(i) for i in b)
















class Yes:
    a = 1

    def __init__(self):
        pass

    def yes(self):
        if Yes.a==1:
            print("Yes")
        else:
            print("No, but yes")


class No(Yes):

    def no(self):
        if Yes.a == 1:
            print("No")
        else:
            print("Yes, but no")
        Yes.a -= 1 #Note this line


Yes().yes()
No().no()
Yes().yes()
No().no()













