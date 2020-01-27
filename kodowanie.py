

a = 'TOto1212'

l2 = [ord(c) for c in a]

for i in range(len(l2)):
    if l2[i] < 10:
        l2[i] = str(l2[i])
        l2[i] = '00' + l2[i]
    if l2[i] <100:
        l2[i] = str(l2[i])
        l2[i] = '0' + l2[i]

print(''.join(map(str, l2)))










































