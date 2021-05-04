def back(d):
    def t(p):
        return p in d
    return t

class tr:
    gh=''
    en=['\n']
    
def daemon(l):
    def x(*a,**b):
        __k.run(l,*a,**b)
    return x
@daemon
def ty():
    d=__k.get()
    tr.gh+=d
    if d in tr.en:
        __k.end()
@daemon   
def ti():
    if __k.get() in tr.en:
        __k.end()
@daemon
def tu(b=t[0],k=''):
    tr.gh=k
    tr.en=b
@daemon
def tp(b=t[0]):
    tr.en=b
@daemon
def to():
    b=__k.tell()
    if __k.get() in tr.en:
        return
    __k.seek(b)
    __k.end()
@daemon
def te():
    b=__k.tell()
    n=__k.get()
    if n in tr.en:
        tr.gh+=n
        return
    __k.seek(b)
    __k.end()

def sort(t,b):
    n=[]
    k=len(b)
    for i in t:
        if len(i)>=k:
            if i[:k]==b:
                n.append(i)
    return n
@daemon
def sea():
    tr.a=__k.tell()
    t=[]
    n=__k.get()
    for i in tr.ak:
        if len(i)>tr.at:
            if i[tr.at]==n:
                t.append(i)
        else:
                tr.al=n
    tr.ak=t
    if not t:
        __k.end()

def tip(a):
    tr.ad[tr.an]=a


class dg:
    isiden=back(t[2])
    issp=back(t[1])
    isdig=back(t[3])
    word=t[2]
    word.extend(t[3])
def boo():
    tr.ni+=1
    return ex[tr.ni]()

fcsh=[]
ussh={}
krsh={}
trsh={}
ex=[0]
mnsh=[]
t={0:['\n']}

#some_________________________________
def readline(b,n=t[0]):
    tu(n,b)
    ty()
    return tr.gh
def passline(t[0]):
    tp(n)
    ti()
def space(n=t[1]):
    tp(n)
    to()
def add(n):
    tr.an=n
    return tip
def word(n=t[1],b=''):
    tu(n,b)
    te()
    return tr.gh

def cauhgt(a=None):
    if a!=None:tr.ad=a
    else:return tr.ad

def search(t,b=''):
    t=sort(t,b)
    tr.al=''
    tr.at=len(b)
    tr.ak=t
    sea()
    __k.seek(tr.a)
    return tr.al

def keyword():
    b=__k.tell()
    n=__k.get()
    if dg.isiden(n):
        return word(dg.word,n)
    else:
        __k.seek(b)
        pass
    pass

def file(n):
    t=__import__(n).i
    def r1(w):
        try:
            b=t[w(1)]
            while type(b)==dict:
                b=b[w(1)]
            return b
        except KeyError:
            __k.end()
            __k.func.add(exit)
            return ''
        pass
    return r1

caught(trsh)
@add('')
def i():
    tr.ni=-1
    boo()
#def unity(l=[],k=[]):
    
krsh['func']=type('func',unity(fcsh,mnsh))
