n=int(input())
u=list(map(int,input().split()))
u.insert(0,0)
i=0

def end(i):
    if i==3:
        return min(u[2],u[1])+u[i]
    if i==2:
        return u[2]
    if i==1:
        return u[1]

def f(i):
    if i<=3:
        return end(i)
    else:
        return min(f(i-1),f(i-2))+u[i]
print(f(n))
