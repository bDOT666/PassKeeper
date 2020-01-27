

p = 'Wiktoria Płaszczyk'

wez_p = [ord(c) for c in p]

for i in range(len(wez_p)):
    if wez_p[i] < 10:
        wez_p[i] = str(wez_p[i])
        wez_p[i] = '00' + wez_p[i]
    if wez_p[i] <100:
        wez_p[i] = str(wez_p[i])
        wez_p[i] = '0' + wez_p[i]

print(''.join(map(str, wez_p)))








































