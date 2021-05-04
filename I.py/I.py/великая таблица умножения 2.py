set=lambda : list(map(int,input().split()))
n,m=set()
def r(q):
    i=__builtins__.input
    global r,input, close, exit
    def exit(a):
        close()
        raise AssertionError(a)
    def close():
        for i in range(q):
            input()
    def input(*a,**b):
        nonlocal q
        q-=1
        return i(*a,**b)
r(n)
try:
    if n==1 and m==1: exit("true")
    if n==1:
        z=set()
        a=z[1]-z[0]
        if a<=0: exit("false")
        if z[1]%a: exit("false")
        for i in range(2, m):
            if z[i]-z[i-1]!=a: exit('false')
        exit("true")
    elif m==1:
        a,b=int(input()),int(input())
        q=b-a
        if q<=0: exit("false")
        if b%q: exit("false")
        for i in range(2, n):
            a=b
            b=int(input())
            if (b-a)!=q: exit('false')
        exit("true")
    z,x=set(),set()
    b,a=z[1]-z[0],x[0]-z[0]
    if b<=0 or a<=0:    exit("false")
    for i in range(m):
        if (a+i)*b!=z[i]: exit("false")
    b+=1
    for i in range(m):
        if (a+i)*b!=x[i]: exit("false")
    b-=1
    for s in range(2,n):
      x=set()
      for i in range(m):
        if (a+i)*(b+s)!=x[i]: exit("false")
    exit("true")
except AssertionError as d:
    print(d)
    del exit
