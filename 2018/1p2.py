f = open("input1.py")
c    = [0]
delt = []
for l in f:
    delt.append(int(l))
while len(c)-len(set(c)) == 0:
    for d in delt:
        c.append(d+c[-1])
for i in range(len(c)-len(delt),len(c)):
    if c[i] in c[:i]:
        print(c[i])
        break