n,k,x,y=map(int,input().split())

q1=(k-1)*y
q=q1+x

a,b=divmod(n,k)
v=a*q+b*y



def ji(a):
    a=a%v
    if a==0:
        print(n)
        return
    
    b,a=divmod(a,q)
    if a>q1:
        print((b+1)*k)
    else:
        s,a=divmod(a,y)
        if a:s+=1
        print((b*k)+s)
input()
for i in map(int,input().split()):
    ji(i)
