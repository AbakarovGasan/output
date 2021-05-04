g=lambda :list(map(int,t.split()))
vic= lambda q, w: abs(q[0]-w[0])**2+abs(q[1]-w[1])**2 
    
do = lambda q,w,e: (
    vic(q,w),
    vic(w,e),
    vic(e,q),   )

a,b,c=do(g(),g(),g())
