lst=type('global names', (list,), {} )
synerr=SyntaxError
class End(Exception):
    pass

def main(k):
    srvc=k.com.daemon
    num=k.com.number
    mg=k.com.mgword
    fix=k.com.fix
    srch=k.com.search
    v1={}
    v2={}
    v3=lst([ [{}] ])
    F=[]
    var={'w': v1, '#': v2, 'v': v3, 'F': F}
    add=F.append
    cl=callable
    glbs=k.globals
    glbs['End']=End
    def __():
        g=[]
        class e:
            pass
        @srvc
        def z():
            e.r=g[e.i](e.v)
            e.i+=1
        var['fw']=g
        def j():
            e.v=mg()
            e.i=0
            if not e.v: return
            k.end()
            z()
  #          print(e.r.__name__)
            v= e.r()
            return v
        add=g.append
        @add
        def __(v):
            v=v1.get(v)
            if cl(v): k.end()
            return v
        @add
        def __(v):
            b=v3[-1]
            j=-len(b)
            p=0
            while p>j:
                p-=1
                g=b[p].get(v)
                if cl(g):
                    k.end()
                    return g
        @add
        def __(v):
            k.end()
            raise End(v+' is not defined')
        return j
    add(__())
    @add
    def __():
        g=srch(v2)
        g=v2.get(g)
        if cl(g):
            k.end()
   #         print(g.__name__)
            return g()
    @add
    def __():
        g=num()
  #      print(g)
        if g:
            k.end()
            return fix(g)

    @add
    def __():
        y=k.get()
        raise synerr(y)
    
    add=k.com.add
    def __():
        class e:
            i=0
        @srvc
        def r():
            e.r=F[e.i]()
            e.i+=1
        def do():
            e.i=0
            r()
            return e.r
        return do
    do= add(__())
    fend=k.com.TheFileEnd
    @srvc
    def start():
        try:
            do()
        except fend:
            k.end()
    start.__name__='start'
    add(start)
    
    glbs['var']=var
    def __define__(a,b,c=-1, d=-1):
        v3[d][c][a]=b
        
    glbs['__define__']=__define__
    
    def func(o, *a, **b):
        return lambda: o(*a, **b)
    def __():
        o=k.globals['__str__']
        rd=k.com.rdline
        def R(*f):
            for i in f:
                z=func(o, i)
                z.__name__='__str__ '+i
                v2[i]=z
        R('"', "'''", '"""', "'")
        v2['#']=lambda: rd() 
        v1['print']= lambda: print( do())
    __()
    
            
        
        
        
        
    
