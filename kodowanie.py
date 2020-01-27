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

a= ''.join(map(str, wez_p))
print(a)



def GetIntegerSlice(i, n, m):
  # return nth to mth digit of i (as int)
  l = math.floor(math.log10(i)) + 1
  return i / int(pow(10, l - m)) % int(pow(10, m - n + 1))
































