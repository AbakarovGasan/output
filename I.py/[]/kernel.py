g={}
t=[g.__getitem__, g.__setitem__, g.__delitem__, g.__contains__, g.keys]
o=staticmethod
gt=getattr
st=setattr
dl=delattr
cn=hasattr
def none(*a):
    pass
kernel=type('kernel', (),{
'__getattr__':o(lambda *a, **b: t[0](*a, **b)),
'__setattr__':o(lambda *a, **b: t[1](*a, **b)),
'__delattr__':o(lambda *a, **b: t[2](*a, **b)),
'__hasattr__':o(lambda *a, **b: t[3](*a, **b)),
'__dir__':o(lambda *a, **b: t[4](*a, **b)), })()
def add(a):
    o=a.__name__
    g[o]=a
k={0:False }

@add
def run(t, *a, **b):
    r=k[0]
    k[0]=True
    while k[0]:
        t(*a, **b)
    k[0]=r
    
@add
def end():
    k[0]=False

def __():
    s=staticmethod
    b=bool
    t=str
    r=repr
    j=k.__setitem__
    g=getattr
    d=dir
    n=type('bool', (int, ),{
    '__bool__': s(lambda: k[0]),
    '__str__': s(lambda: t(k[0])),
    '__repr__': s(lambda: t(k[0])),
    '__name__': 'bool', 
    '__call__': s(lambda v: j(0, b(v))),
    '__setattr__': none,
    '__getattr__': s(lambda a: g(k[0], a)),
    '__dir__': s(lambda: d(k[0])),
    '__delattr__': none})()
    return n

add(__())

def __(): 
 ad=g.__setitem__
 ad('fin', type('fin', (),{
'__getattr__':o(lambda *a, **b: gt(k[1] ,*a, **b)),
'__setattr__':o(lambda *a, **b: st(k[1] ,*a, **b)),
'__delattr__':o(lambda *a, **b: dt(k[1] ,*a, **b)),
'__hasattr__':o(lambda *a, **b: cn(k[1] ,*a, **b)), })())
 ad('fout', type('fout', (),{
'__getattr__':o(lambda *a, **b: gt(k[2] ,*a, **b)),
'__setattr__':o(lambda *a, **b: st(k[2] ,*a, **b)),
'__delattr__':o(lambda *a, **b: dt(k[2] ,*a, **b)),
'__hasattr__':o(lambda *a, **b: cn(k[2] ,*a, **b)), })())
 
__()
#@add
#def get():
 #   return k[1].read(1)
@add
def seek(*a, **b):
   # print(a, b)
    return k[1].seek(*a, **b)

@add
def tell(*a, **b):
    return k[1].tell(*a, **b)

@add
def read(*a, **b):
    return k[1].read(*a, **b)

@add
def write(*a, **b):
    return k[2].write(*a, **b)
@add
def save(*a, **b):
    return k[2].close(*a, **b)

@add
def __():
    return k, t, g

def none(*a, **b):
    pass

@add
def open(a, b=True):
    if b:
        k[1]=a
    else:
        k[2]=a

def add():
    t={'none': none}
    g['globals']=t
    class com:
        __getattr__=o(t.__getitem__)
        __setattr__=none
        __delattr__=none
        __dir__=o(t.keys)
    global add
    g['com']=com()
    def add(a):
        t[a.__name__]=a
        return a
add()
err=Exception
def __():
    isiden=str.isidentifier
    isnum=str.isdigit
    isspace=str.isspace
    def isspec(a):
       if not isiden(a):
          if not isnum(a):
             if not isspace(a):
                return True
       return False
    g['globals'].update(locals())
__()
#    globals().extend(locals())
del open
def main():
    k=kernel
    @add
    def daemon(t):
        return lambda *a, **b: k.run(t, *a, **b)
    t=open('lib.ini','r')
    p=__import__
    e=ImportError
    s=str.strip
    for i in t.readlines():
      i=s(i)
      if i:
        try:
            p(i).main(k)
        except e:
            pass
    return k
if __name__=='__main__':
    main()
        
    
