class u(int):
    def __call__(a,b=True):
        a._j=b
    def __bool__(a):
        return a._j
j=lambda r: list(map(int,r.split()))

from math import inf


def new(a,b):
    n=bool(a)
    m=u(b)
    m(n)
    return m

def t1(a):
    if a<0:
        return False
    else:
        return True

def read():
 p=[-inf]
 for i in range(int(input())):
    a,b=j(input())
    a=u(a)
    a(t1(b))
    p.append(a)
 p.append(inf)
 input()
 cp=j(input())
 return p,cp

def get(a):
 p=[-inf]
 ad=a.split('\n')
 q=-1
 def input():
    nonlocal q
    q+=1
    return ad[q]

 for i in range(int(input())):
    a,b=j(input())
    a=u(a)
    a(t1(b))
    p.append(a)
 p.append(inf)
 input()
 cp=j(input())
 return p,cp

def r1(p,cp):
 for i in cp:
     o=1
     k=len(p)-1
     while o<k:
  #       input(str(o))
         n=p[o]
         if n:
             n=new(n , n+i)
             z=p[o+1]
             if not z:
                 if n>=z:
                     k-=2
                     p.pop(o)
                     p.pop(o)
                     o-=1
                 else:
                     p[o]=n
             else:  p[o]=n
             
         else:
             n=new(n , n-i)
             z=p[o-1]
             if z:
                 if n<=z:
                     o-=1
                     k-=2
                     p.pop(o)
                     p.pop(o)
                 else:
                     p[o]=n
             else:  p[o]=n
         o+=1
     print(len(p)-2)
     
def main():
    p,cp=read()
    r1(p,cp)

do=lambda j:r1(*get(j))


main()
