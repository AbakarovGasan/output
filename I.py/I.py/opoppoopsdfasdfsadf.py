import math
a=int(input())
b=int(input())
k=int(input())
y=math.ceil(a**(1/3))
s=0
if k==0:
    for i in range(1,1001):
        if a<=i**6<=b:
            s+=1
else:
    zx=y**3
    while zx:
        low=max(a,zx-k)
        low=math.ceil(low**(1/2))
        high=min(b,zx+k)
        high=math.floor(low**(1/2))
        s+=high-low+1
        y+=1
        zx=y**3
print(s)
