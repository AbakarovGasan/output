
def split(i):
  z=[]
  c=[0]
  x=[0]
  for d in i:
    z.append({d:i[d]})
    c.append(1)
    c[0]+=1
    x.append(i[d])
    x[0]+=i[d]
  return z,c,x
def hit(d):
  for i in d:
    if type(i)==type([]):
      for a in hit(i):
        yield a
    if type(i)==type({}):
      for a in i:
         yield a,i[a]

def bit(num):
   oi=2**(bytes(num)-1)
   og=num-oi
   if og==oi: og=0
   return og
def new(v):
  if type(v)==type([]):
    f=list()
    for i in v:
      f.append(new(i))
  elif type(v)==type({}):
    f=dict()
    for i in v:
      f[i]= new(v[i])
  else:
     f=v
  return f
from bin import *
def bytes(num):
  b=0
  v=1
  while num>v:
    v*=2
    b+=1
  return b
  
def arc(name):
 d={}
 r=open(name,'rb')
 t=r.read(1)
 while t:
  b=0
  x=t
  try:
    d[t]+=1
  except Exception:
    d[t]=1
  t=r.read(1)
 # while x==t:
  #    b+=1
   #   t=r.read(1)
    #  try:
     #  d[b]+=1
      #except Exception:
       #d[b]=1
 r.close()
 return d
def mad(d,fun):
 i=[]
 f=[0]
 l=[0]
 mad=1
 while mad>0:
   try: mad=max(d.values())
   except ValueError: break
   mad=mad//fun
   l.append(0)
   f.append(0)
   i.append({})
   dd=d.copy()
   for a in dd:
     if d[a]>= mad:
      i[-1][a]=d[a]
      l[-1]+=d[a]
      f[-1]+=1
      del d[a]
   if not f[-1]:
     del f[-1]
     del l[-1]
     del i[-1]
 f[0]=len(f)-1
 l[0]=sum(l)
 return f,l,i

def set(ll):
  try:
   ll=ll[1:]
   f=[]
   for i in ll:
    f.append(fire(i))
  except TypeError:
    f=ll
  return f

def index(l,u,k=0,m=0):
  m=len(l)-m
  while k<m:
    try:
      if l[k][0]==u:
        return k
    except TypeError:
      if l[k]==u:
        return k
    k+=1
    

def mix(l):
 p=len(l)-1
 ti=0
 o=[]
 b=[]
 o.extend(l)
 o=set(o)
 o.sort()
 while ti!=p:
   bn=index(l,min(o))
   o.pop(0)
   b.append(bn)
   ti+=1
 del o
 del ti
 del p
 return b

def rt(l):
  h=len(l)
  t=0
  while t<h:
    if l[t]:
      t+=1
    else:
      del l[t]
      h-=1
  return l

def add(num=0,g=0):
  j=[]
  while num:
    j.append(new(g))
    num-=1
  return j

def cut(l,f,i):
    z=fire(l[-1])
    t=l[:-1]
    r=f[:-1]
    y=l
    u=f
    x=i
    z=enter(t,r,z)
    for a in z:
      y=y[a]
      u=u[a]
      x=x[a-1]
    if type(y)==type(0):y,u,x=split(x)
    y.append(new(l[-1]))
    u.append(new(f[-1]))
    x.append(new(i[-1]))
    y[0]+=fire(l[-1])
    u[0]+=1
    l[-1]=0
    f[-1]=0
    i[-1]={}
    f[0]-=1
    return rt(l),rt(f),rt(i)
  
def ord(s,n,i,div):
 # print('\n','order begin with','f',n,'l',s,'i',i,sep='\n',end='\n')
  i.insert(0,{})
  k=add(div+1,[0])
  p=add(div+1,[0])
  p[0]=div
  k[0]=0
  w=add(div+1,[])
  a=[0,0,0]
  g=1
  t=range(len(i))
  for l in range(len(i)-1):
    #lab2
    a[g]+=1*g
    a[0]+=1
    w[a[0]].append(i[a[g]])
    k[a[0]].append(s[a[g]])
    k[a[0]][0]+=fire(s[a[g]])
    p[a[0]].append(n[a[g]])
  #  print('i',i[a[g]],'l',s[a[g]],'f',n[a[g]],'num',t[a[g]])
    p[a[0]][0]+=1
    if a[0]==div:
  #    print(g)
      g*=-1
      a[0]=0
  k[0]=sum(set(k))
  p[0]=len(p)-1
  w=w[1:]
  return k,p,w
  
def find(d,t):
    g=None
    if type(d)==type([]):
       for i in d:
           g=find(i,t)
           if g:
                return g
    if type(d)==type({}):
       for i in d:
           if i==t:
              return d[i]
       return None
      
def fire(i):
  try:fire=i[0]
  except TypeError:fire=i
  return fire

def ni(f,l):
  n=0
  if type(f)==type(0):
    n=l*bytes(f)
    return n
  if type(f)==type([]):
    for i in range(len(f)):
      n+=ni(f[i],l[i])
    return n
      
def mind(l,f,i):
    t=mix(l)
  #  print(l)
    s=-len(t)
    if s==-1:
      l=l[1]
      f=f[1]
      i=i[0]
      return l,f,i
 #   print(s,t,l)
    b=-1
    c=[]
    q=[]
    v=[]
    while s!=b:
      c.append([0])
      q.append([0])
      v.append([])
 #     print(c[-1][0],fire(l[t[-1]]))
      while c[-1][0]!=fire(l[t[-1]]) and s!=b: 
        b-=1
 #       print(s)
 #       print(b)
        c[-1].append(l[t[b]])
        c[-1][0]+=l[t[b]]
        l[t[b]]=0
        q[-1].append(f[t[b]])
        q[-1][0]+=1
        f[t[b]]=0
        v[-1].append(i[t[b]-1])
        i[t[b]-1]={}
      c,q,v=rt(c),rt(q),rt(v)
      l,i,f=rt(l),rt(i),rt(f)
      c,q,v=mind(c[0],q[0],v[0])
      l.append(c)
      f.append(q)
      i.append(v)
      f[0]=len(f)-1
      if fire(l[1])/fire(l[-1])>=2:l,f,i=cut(l,f,i)
    return l,f,i


def div(s,n,b,i):
 div=round(fire(s)/fire(b),0)
 if div>fire(n): return False,False,False
 if type(s)==type(0): i,n,s=split(i)
 k,p,w=ord(s,n,i,div)
 return k,p,w
  
def zs(f,l,i):
  if f[0]<=1:return f,l,i
  b=1
  t=mix(l)
  jz=0
  s=0
  while b:
    s+=1
    b=l[t[0]]
    l[t[0]]=0
    l.append(new([fire(b),b]))
    f.append(new([1,f[t[0]]]))
    f[t[0]]=0
    i.append(new([i[t[0]-1]]))
    i[t[0]-1]={}
   # print('\n\nbegin','\nmin',b,'\nl',l,'\nf',f,'\nord',t)
    for a in t[1:]:
    #  print('\nstart with '+str(a),'\nl',l[a],'\nf',f[a])
      z,m,x=div(l[a],
                f[a],
                b,
                i[a-1])
      if z:
        s=0
        l[a]=0
        f[a]=0
        i[a-1]={}
        l[-1].extend(z[1:])
        f[-1].extend(m[1:])
        i[-1].extend(x)
        l[-1][0]=sum(set(l[-1]))  
        l[-1]=rt(l[-1])
        f[-1][0]=1
        f[-1]=rt(f[-1])
        f[-1][0]=len(set(f[-1]))
        i[-1]=rt(i[-1])
    #    print('f',f,'\nl',l)
      else:
  #      print('false')
        pass
    if s:
      l[-1]=l[-1][1]
      f[-1]=f[-1][1]
      i[-1]=i[-1][0]
    f[0]=1
    l[0]=sum(set(l))
    l=rt(l)
    f=rt(f)
    i=rt(i)
    f[0]=len(f)-1
    t=mix(l)
    if s:
      t=t[s:]
    if t==[0] or not t:b=0
#    print('\nend','\nl',l,'\nf',f,'\nord',t)
  f[0]=len(f)-1
  
  l,f,i=mind(l,f,i)    
  return f,l,i

def abc(n):
  if n<0: n*=-1
  return  n
    
def enter(t,f,z, b=256**8):
  d=[]
  i=0
  r=[]
  for a in range(1,len(t)-1):
    if type(t[a])==type(0):
        i=z-(t[a]/f[a])
        if abc(b)>abc(i):
          b=i
          d=new([a])
    else:
      i=z-t[a][0]/ f[a][0]
      if i<0: i,r=enter(t[a],f[a],z,b)
      if abc(b)>abc(i):
        b=i
        d=new([a])
        if r:
          d.extend(new(r))
          r=[]
  return b,d
          

d=arc('update.py')

f,l,i=mad(d,2)

f,l,i=zs(f,l,i)
