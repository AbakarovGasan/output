def fix(t):
    return type('fixed', (type(t),  ), {"__call__":(lambda t: t) })(t)
class TheFileEnd(Exception):
        pass
tfe=TheFileEnd
class tr:
    u=''
def main(k):
        sp=k.com.isspace
        isn=k.com.isiden
        nu=k.com.isnum
        glbs=k.globals
        def add(s):
            glbs[s.__name__]=s
            return s
        add(fix)
        add(add)
        @add
        def space():
          try:
            while sp(k.get()):
                pass
            k.jump(-1)
          except tfe:
              pass     
        def add():
                f=TheFileEnd
                glbs['TheFileEnd']=f
                u=k.read
                s=k.seek
                t=k.tell
                def jump(i):
                    s(t()+i)
                def get():
                        y=u(1)
                        if not y:
                                raise f('TheFileEnd')
                        return y
                def tm(x):
                    try:
                        x()
                    except f:
                        if not tr.u:
                            raise f('TheFileEnd')
                    finally:
                        y=tr.u
                        tr.u=''
                        return y
                def add(s):
                    j=lambda: tm(s)
                    glbs[s.__name__]=j
                    return j
                k.get=get
                k.jump=jump
                return add
        add=add()
        sc=k.com.isspec
        @add
        def word():
            space()
            h=k.get()
            if sc(h) or nu(h):
                tr.u=None
            else:
                tr.u=h
                o=k.get()
                while isn(o):
                    tr.u+=o
                    o=k.get()
            k.jump(-1)
            return tr.u
        @add
        def mgword():
            space()
            h=k.get()
            if sc(h) or nu(h):
                tr.u=None
            else:
                tr.u=h
                o=k.get()
                print(o)
                while nu(o) or isn(o):
                    tr.u+=o
                    o=k.get()
                    print(o)
            k.jump(-1)
            return tr.u
        @add
        def number():
            space()
            h=k.get()
            if sc(h) or isn(h):
                tr.u=None
            else:
                tr.u=h
                o=k.get()
                while nu(o):
                    tr.u+=o
                    o=k.get()
            k.jump(-1)
            return tr.u
        add=k.com.add
        @add
        def search(t):
          try:
            m=0
            u=k.tell()
            t=list(t)
            j=len(t)
            out=''
            f=k.get()
            while t:
                    i=0
                    while i<j:
                            z=t[i]
                            if len(z)<=m:
                                    out=t[i]
                                    u=k.tell()-1
                                    t.pop(i)
                                    j-=1
                                    i-=1
                            elif z[m]!=f:
                                    t.pop(i)
                                    j-=1
                                    i-=1
                            else:
                                    pass
                            i+=1
                    m+=1
                    f=k.get()
         #   print(u)
            k.seek(u)
            return out
          except TheFileEnd:
            for i in t:
              if len(i)==m:
                 return i
        #    print(u)
            k.seek(u)
            return out
        
        @add
        def __str__(e="'''", u={}):
            s=''
            r=len(e)
       #     print(e)
            m=e[0]
            i=0
            x=''
            while True:
                q=k.get()
                while q==m:
                    i+=1
                    if i==r:
              #          print(i)
                        return s
                    m=e[i]
                    x+=q
                    q=k.get()
                else:
                    s+=q
                    if x:
                        i=0
                        s+=x
                        x=''
        @add
        def rdline(n='\n'):
            while k.get()!=n:
                pass
        
        
