a=int(input())
b=int(input())
k=int(input())

q=range(a,b+1)
l=True
i=a
az=0
while i<=b:
    for t in q:
        t=t**3
        if t>b:
            i=b+1000
            break
        y=i**2
        if abs(y-t)<=k:
            az+=1
    i+=1
print(az)
