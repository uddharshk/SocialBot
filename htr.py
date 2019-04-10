g=open("uur1.txt",'r')
d={}
x=0
e=0
w=0
for i in g:
    j,k=i.split()
    if x==int(j):
        e+=1
        w+=int(k)
    else:
        if x!=0:
            d[x]=w/e
        e=1
        w=int(k)
        x=int(j)
print(d)
