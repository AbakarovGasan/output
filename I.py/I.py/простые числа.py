q=[2,3]



input()
p=list(map(int,input().split()))
p.sort()

d=p[-1]
o=3
while o<=d:
     o=q[-1]
     
     y=True
     while y:
       o+=1
       y=False
       for i in q:
          if not o%i:
              y=True
              break
     q.append(o)

out=0
qlt=0

for i in p:
    al=0
    for s in q:
        if i%s==0:
           al+=1
    if qlt<al:
        out=i
        qlt=al
print(out)
    

