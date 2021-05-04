n,m,f,p=map(int,input().split())

if not p:
 f-=1
 a,f=divmod(f, m*4)
 a+=1
 b,k=divmod(f,4)

 b+=1
 print(a,b)
else:
    p=list(map(int,input().split()))
    f-=1
    a,f=divmod(f, m*4)
    for i in range(1,a+1):
        if i in p:
            f+=1
    z,f=divmod(f, m*4)
    a+=z+1
    if a in p:
        f+=1
    b,k=divmod(f,4)
    b+=1
    print(a,b)
    
    
    


