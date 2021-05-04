a=[]
b=[]
c=[]

ve=ValueError

ji=[]
d=[]
x=d.append
for i in range(int(input())):
    x(input())
d.sort()

for j in d:
   x=list(j)
   x.sort()
   try:
       o=a.index(x)
       q=b[o]
       if not j in q:
           q.append(j)
       c[o]+=1
   except ve:
       a.append(x)
       c.append(1)
       b.append([j])
       
for i in range(5):
    z=max(c)
    if z==0:
        break
    p=c.index(z)
    c[p]=0
    l=b[p]
    l.sort()
    print("Group of size "+str(z)+':',*l, '.')

   
