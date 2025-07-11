f=open('a.txt')
f2=open('softwarica.txt','w')
for i in f:
    c=i.strip().split()
    print(c)
    f2.write(c[1])