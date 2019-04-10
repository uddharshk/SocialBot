g=open("uur1.txt",'r')
s=set([])
d={}
x=0
e=0
for i in g:
    l=i.split()
    if x==l[0]:
        for j in range(1,len(l)):
            q=l[j][1:-2]
            if q not in s and q!="":
                s.add(q)
            elif q!="":
                e+=1
    else:
        if x!=0:
            d[x]=e
        e=0
        s=set([])
        x=l[0]
print(d)