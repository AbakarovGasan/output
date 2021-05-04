import sys
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
    if f(a,v):
        a=a.decode()
    return s(a)
 def nep(a):
     a=a.var
     if not f(a,v):
         a=s(a).encode()
     return a
 def new(*a):
    def z(d):
       for i in a:
           d=gi(d,i)
       return d()
    return z

 def arch(f,o,start=None,stop=None):
     if start==None:
         start=f.pos
     s=f.text[pmk(start,stop)].find(o)
     if s<0:
         return -1
     else:
         s+=start
         if f.bool:
             f.pos=s+1
         return s
 def search(f,o,start=None,stop=None,order='little'):
     return arch(f,o.to_bytes(qw(o),order),start,stop)
 def einf(f,o,start=None,stop=None):
     return arch(f,s(o).encode(),start,stop)
     
 def nui(a,k=4):
    return a.var.to_bytes(k,'little')
 def num(a):
    return c.from_bytes(a.text[a.var],'little')
 return [owc,bit,nrml,new,nui,num,f,c,nep,search,einf]
def file():
 global file
 ln=len
 gtr=getattr
 opn=open
 owc,bit,nrml,new,nui,num,isins,int,nep,se,einf=bitli()
 def file():
    class u:
         w=nui
         r=num
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

def m():
 iヸヹ=input
 eヸヹ=eval
 xヸヹ=exec
 Pヸヹ=sys.stdout.write
 rヸヹ=repr
 Eヸヹ=Exception
 Sヸヹ=SyntaxError
 sヸヹ=str
 def uヸヹ(m):
     d=0
     for i in m:
         if i!=' ':
             break
         d+=1
     return ' '*d
 def tヸヹ():
  while True:
    try:
      try:
        fヸヹ=iヸヹ('>>> ').rstrip()
        if fヸヹ[-1]in (':','@'):
           mヸヹ=True
          # lヸヹ=''
           while mヸヹ:
            mヸヹ=iヸヹ()
            #lヸヹ=uヸヹ(mヸヹ)
            fヸヹ+='\n'+mヸヹ
           raise Sヸヹ
        pヸヹ=eヸヹ(fヸヹ)
        Pヸヹ('\n')
        if pヸヹ!=None:
            Pヸヹ(rヸヹ(pヸヹ))
            Pヸヹ('\n')
      except Sヸヹ:
          xヸヹ(fヸヹ)
    except Eヸヹ as lヸヹ:
        Pヸヹ(sヸヹ(lヸヹ))
        Pヸヹ('\n')
 return tヸヹ
def main():
 global m
 Mヸヹ=m
 Pヸヹ=sys.stdout.write
 del m
 mヸヹ=Mヸヹ()
 KPヸヹ=KeyboardInterrupt
 while 1:
  try:
   while 1:
     mヸヹ()
  except KPヸヹ:
     Pヸヹ('KeyboardInterrupt\n')  
     mヸヹ=mヸヹ()
if __name__=="__main__":
    main()

