dct=[2,3]
def vi(q):
        while  len(dct)<=q:
            v=dct[-1]
            while True:
                v+=1
                p=False
                for i in dct:
                    if not v%i:
                        p=True
                        break
                if not p:break
            dct.append(v)
        return dct[q]

def dip(q,i):
    b=i
    t=vi(0)
    p=0
    c=1
    while t<q:
        while not (i%t or q%t):
            i//=t
            q//=t
            c*=t
        p+=1
        t=vi(p)
    return b//c

input()
h=list(map(int,input().split()))
h.sort(reverse=True)
q=h.pop(0)



for i in h:
     if q%i:
        q*=dip(q,i)
print(q)

