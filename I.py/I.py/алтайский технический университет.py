x,y,r=input().split()
x,y=map(int,(x,y))
r=float(r)
t=r**2
z=[]
for i in range(int(input())):
    a,b=map(int,input().split())
    a-=x
    b-=y
    if (a**2+b**2)<=t:
        z.append((a,b))
