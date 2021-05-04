s=input()
class get():
    def __init__(a,b):
        a.i=b
        
    def __mul__(a,b):
        return get(mul(a.i,b.i))

    def __add__(a,b):
        return get(add(a.i,b.i))

    def __sub__(a,b):
        return get(sub(a.i,b.i))

def add(a,b):
    for i in b:
        if not i in a:
            a+=i
    return a

def sub(a,b):
    for i in b:
        if i in a:
            o=a.index(i)
            a=a[:o]+a[o+1:]
    return a

def mul(a,b):
    o=''
    for  i in a:
        if i in b:
            o+=i
    return o

e=len(s)
i=-1
while i<e:
    i+=1
    if s[i]=='{':
        o=i
        i+=1
        k=''
        while s[i]!='}':
            k+=s[i]
            i+=1
        s=s[:o]+'get('+k+')'+s[i+1:]
        
