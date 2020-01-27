import math

p = 'Wiktoria Płaszczyk'

wez_p = [ord(c) for c in p]

for i in range(len(wez_p)):
    if wez_p[i] < 10:
        wez_p[i] = str(wez_p[i])
        wez_p[i] = '00' + wez_p[i]
    if wez_p[i] <100:
        wez_p[i] = str(wez_p[i])
        wez_p[i] = '0' + wez_p[i]

a = ''.join(map(str, wez_p))
print(a)









b = []
for i in range(0, len(a), 3):
    c = a[i:i + 3]
    b.append(int(a[i:i + 3]))
print(b)

pmsg = ''.join(chr(i) for i in b)
print(pmsg)





























