def bitli():
 o=open
 f=isinstance
 c=int
 z=bin
 pmk=slice
 v=bytes
 s=str
 gi=getattr
 def owc(a,b):
    t=o(a,'wb')
    t.write(b)
    t.close()
 def bit(a):
    if f(a,c):
        return v([a])
    else:
        return a
 def qw(o):
     o=z(o).__len__()-2
     g=o//8
     if g<o/8:g+=1
     return g
 def nrml(a):
    a=a.text[a.var]
    a=a.decode()
    return a
 def nep(a):
     if not f(a,v):
         a=s(a).encode()
     return a
 def new(*a):
    def z(d):
       for i in a:
           d=gi(d,i)
       return d()
    return z
 def search(f,o,start=None,stop=None,order='little'):
     d=qw(o)
     if start==None:
         start=f.pos
     s=f.text[pmk(start,stop)].find(o.to_bytes(d,order))
     if s<0:
         return -1
     else:
         s+=start
         if f.bool:
             f.pos=s+1
         return s
     
 def nui(a,k=4):
    return a.var.to_bytes(k,'little')
 def num(a):
    return c.from_bytes(a.text[a.var],'little')
 return [owc,bit,nrml,new,nui,num,f,c,nep,search]
def file():
 owc,bit,nrml,new,nui,num,isins,int,nep,se=bitli()
 h={'d':num,'s':nrml}
 def read(a,b='d'):
        return(h[b](a))
 global file
 ln=len
 gtr=getattr
 opn=open
 
 def file():   
    class u:
         w=nui
         r=read
         s=se
         k=''
    def thi(a,n):
        if a.bool: a.pos=n
    def get(a,n):
        a.pos=0
        a.text=bit(a.text.__getitem__(n))
        owc(a.name,a.text)
    class f:
     var=''
     bool=False
     name=''
     text=b''
     pos=0
     len=0
     class cut:
       def __init__(a,b):
           a.s=b
       def __getitem__(a,d):
           return get(a.s,d)
     def __init__(a):
         a.cut=a.cut(a)
     def __call__(a,d):
        a.name=d
        g=opn(d,'rb')
        a.text=g.read()
        a.pos=0
        a.len=ln(a.text)
     def search(a,*b,**c):
         return u.s(a,*b,**c)
     def seek(a,b=0,v=0):
        if v==0:
            a.pos=b
        elif v==1:
            a.pos+=b
        elif v==2:
            a.pos=a.len+b
     def read(a,b=1,*d,**c):
        x=a.pos
        y=a.pos+b
        thi(a,y)
        a.var=slice(x,y)
        return u.r(a,*d,**c)
     
     def write(a,b,*d,**c):
        a.var=b
        b=u.w(a,*d,**c)
        x=a.pos
        y=a.pos+ln(b)
        thi(a,y)
        a.text=a.text[:x]+b+a.text[y:]
        a.len=ln(a.text)
        owc(a.name,a.text)
    f=f()
     
    class file:
         def __getitem__(a,m):
             get(a,m)
         def __setattr__(a,b,k):
             if b=='write':
                 u.w=k
             elif b=='search':
                 u.s=k
             elif b=='read':
                 u.r=k
             elif b=='bool':
                 f.bool=k
         def __call__(a,*c,**x):
             return f(*c,**x)
         
         def __delattr__(a,b):
             pass
         def __getattr__(a,b):
             return gtr(f,b)  
    return file()
file()
f=file()
f(r"D:\WS\WS.exe")
def m():
 iヸヹ=input
 eヸヹ=eval
 xヸヹ=exec
 Pヸヹ=print
 rヸヹ=repr
 Eヸヹ=Exception
 Sヸヹ=SyntaxError
 def tヸヹ():
  while 1:
    try:
      try:
        fヸヹ=iヸヹ('>>> ')
        pヸヹ=eヸヹ(fヸヹ)
        if pヸヹ!=None:
            Pヸヹ(rヸヹ(pヸヹ))
      except Sヸヹ:
          xヸヹ(fヸヹ)
    except Eヸヹ as lヸヹ:
        Pヸヹ(lヸヹ)
 return tヸヹ
def main():
 mヸヹ=m()
 Pヸヹ=print
 KPヸヹ=KeyboardInterrupt
 while 1:
  try:
   while 1:
     mヸヹ()
  except KPヸヹ:
     Pヸヹ('KeyboardInterrupt')
     mヸヹ=m()
#main()

