j=lambda : list(map(int,input().split()))

n,m=j()
def r(q):
    i=__builtins__.input
    global r,input, close, exit
    def exit(*a):
        raise AssertionError('e')
    def close():
        for i in range(q):
            input()
    def input(*a,**b):
        nonlocal q
        q-=1
        return i(*a,**b)
    
r(n)   
try:
 if n==1 and m==1:
    close()
    print('true')
    exit()
 if m==1:
    a=int(input())
    b=int(input())
    q=b-a
    for i in range(2,n):
        if b-a!=q:
            close()
            print('false')
            exit()
        a=b
        b=int(input())
    if b-a!=q:
        print('false')
    elif b%q:
        print('false')
    else:
        print('true')
    exit()

 z=j()


 a=z[1]-z[0]

 for i in range(2,m):
        if z[i]-z[i-1]!=a:
            print('false')
            exit()
 if n==1:
    if z[0]%a:
        print('false')
    else:
        print('true')
    exit()

 x=j()
 a=x[0]-z[0]
 b=z[1]-z[0]
    

 if a*b!=z[0]:
    close()
    print('false')
    exit()

 e=b+n
 i=b+1
 while i<e:
    g=x[1]-x[0]
    if g!=i:
        for qwe in range(2  , n):
                 input()
        print('false')
        exit()
        
    for c in range(2,m):
        if x[c]-x[c-1]!=g:
            close()
            print('false')
            exit()
    i+=1
    if i >=e:
        break
    x=j()
    n-=1
 print('true')
 exit()
except AssertionError:
    pass

    
