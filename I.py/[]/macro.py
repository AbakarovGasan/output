add=list.append
pop=list.pop
copy=list.copy
synerr=SyntaxError
class g:
    r=''

def main(k):
    sp=k.com.space
    mg=k.com.mgword
    dfn=k.com.__define__
    var=k.com.var
    do=k.com.do
    v3=var['v']
    go=k.com.daemon(lambda: do())
    x=[]
    def args():
        v=mg()
        print(v)
        if v:
            i=[v]
            g=k.get()
       #     print(g)
            while g==',':
                add(i, mg())
                g=k.get()
        #        print(g)
            k.jump(-1)
            return i
    
    def end():
        x.pop(-1)()

    def n():
        g.i=None
        k.end()
        
    def ret():
        g.i=do()
        pop(x,-1)
        k.end()

    v=var["#"]
    v['>']=ret
    v['}']=end
    del v
        
    def run(i, p, u):
        l={}
        u[-1]=l
        for i in i:
            l[i]=do()
        b=k.tell()
        z=v3[-1]
        v3[-1]=u
        add(x, n)
        go()
        v3[-1]=z
        k.seek(b)
        return g.i
        
    def macro():
        v=mg()
        assert v, synerr('name of macro expected')
        g=args()
        t=k.get()
        assert t=="{", synerr('"{" expected')
        p=k.tell()
        while t!="}":
            t=k.get()
        u=copy(v3[-1])
        add(u,{})
        b=lambda: run(g, p, u)
        b.__name__=v
        dfn(v,b)
        return b
    v=var['w']
    v['macro']=macro
