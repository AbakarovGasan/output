write=__import__('sys').stdout.write

glob={}
qwe=glob.setdefault
this=[{}]

def call(a,*b):
  u=id(a)
  qwe(u,{})
  this.append(glob[u])
  q=a(*b)
  this.pop(-1)
  return q

def find(q):
  try:
    p=-1
    s=this[p].get(q)
    while not s:
      p-=1
      s=this[p].get(q)
  except IndexError:
    return object
  return s

class gl:
    def __init__(a,b):
        a.m=b
        a.b=list(b).pop
        a.len=len(b)
    def __bool__(a):
        return bool(a.len)
    def __call__(a):
        a.len-=1
        return a.b(0)

def func(ti):
  j=gl(ti.m)
  return lambda : do(j)
  
def k(ti):
    q='.'
    k=''
    while q!='_':
        q=ti()
        k+=q
 #   print(k)
    if k[0]=='#':
      k=k[1:]
      call( find(k) )
    elif k=="rep_":
#      print('some')
      k=''
      q=ti()
      while q!='_':
        k+=q
        q=ti()
      k=int(k)
      b=func(ti)
      for i in range(k): b()
    else:
    
      this[-1][k]=func(ti)
  #  print(k)
        
    
o={'#':k }

def do(ti):
    #print('do', len(this))
    ti()
    while ti:
        s=ti()
        if s=='}': break
        j=o.get(s)
        if j: j(ti)
        else: write(s)

q=[]
add=q.append
for i in range(int(input())):
    add('{'+input()+'}')
for i in q:
    do(gl(i))
    write('\n')
