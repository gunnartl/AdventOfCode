f,c,d,l= open("i"),[0],[],len
for n in f:
    d.append(int(n))
while l(c)-l(set(c)) == 0:
    for i in d:
        c.append(i+c[-1])
for i in range(l(c)-l(d),l(c)):
    if c[i] in c[:i]:
        print(c[i])
        break