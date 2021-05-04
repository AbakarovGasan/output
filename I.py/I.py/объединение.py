i=input()
class get():
    def __init__(a,b):
        a.i=b
        a.v=0
        a.l=len(b)
    def __call__(a):
        p=a.i[a.v]
        a.v+=1
        return p
    def __bool__(a):
        return bool(a.v<a.l)

get=get('('+i+')')

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

def word():
    y=get()
    if y=='(':
        return do()
    elif y==')':
        get.v-=1
        return ''
    elif y=='{':
        y=get()
        o=''
        while y!='}':
            o+=y
            y=get()
        return o

def do():
    o=word()
    y=get()
    while y!=')':    
        k=word()
  #      print(k,o,y)
        if y=='+':
            o=add(o,k)
        elif y=='-':
            o=sub(o,k)
        elif y=='*':
            o=mul(o,k) 
        y=get()
    return o
h=list(word())
h.sort()


print('{',*(i for i in h),'}',sep='')


