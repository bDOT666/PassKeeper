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
        wez_p[i] = '00' + wez_p[i]
    if wez_p[i] <100:
        wez_p[i] = str(wez_p[i])
        wez_p[i] = '0' + wez_p[i]

a = ''.join(map(str, wez_p))
print(a)

"""
KODOWANIE
"""
float(a)

a1 = a * 13412
print(a1)







"""
ODKODOWANIE
"""




a2 = 1/13412
print(a2)

"""
liczba na Ascii
"""

b = []
for i in range(0, len(a), 3):
    c = a[i:i + 3]
    b.append(int(a[i:i + 3]))
print(b)

daj_p = ''.join(chr(i) for i in b)
print(daj_p)




import tkinter as tk


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
        if Yes.a==1:
            print("No")
        else:
            print("Yes, but no")
        Yes.a-=1 #Note this line

Yes().yes()
No().no()
Yes().yes()
No().no()

print(b)










