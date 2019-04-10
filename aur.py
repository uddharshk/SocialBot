g=open("uur1.txt",'r')
d={}
x=0
e=0
w=0
for i in g:
    j,k,l=i.split()
    if x != int(j) and x != 0:
        if e != 0:
            d[x] = w / e
            e = 0
            w = 0
    x=int(j)
    if k == "1":
        e += 1
        if int(l) > 0:
            w += 1

print(d)
