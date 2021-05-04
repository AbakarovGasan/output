#анаграмма
input()

j=list(map(int,input().split()))
a=len(j)


while a:
    a-=1
    b=a
    while b:
        b-=1
        if j[a]>j[b]:
         #   print(j[a],j[b])
            q=j.pop(a)
            j.insert(b,q)
            l=j[b+1:]
            l.sort()
            j=j[:b+1]+l
           # if z!=j:
            a=0
            break
print( *(i for i in j))
            
