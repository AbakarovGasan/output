from win32api import RegQueryValueEx, RegOpenKeyEx
from win32com.client import Dispatch

links=[]
add=links.append
    
desk=RegQueryValueEx(  RegOpenKeyEx(-2147483647,
"Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders",
0, 1), "Desktop")[0]

class link:
  def __init__(s,i):
    try:
      if len(i)<4 or i[-4:]!='.lnk': raise Exception('sda')
      link=Dispatch("WScript.Shell").CreateShortCut(i)
      s.name=i
      s.argv=[abs(link.Targetpath)]
      s.path=abs(link.WorkingDirectory)
      i=link.Arguments
      b=0
      n=len(i)
      while True:
        if b==n:break
        z=i[b]
        b+=1
        while z==' ':
          if b==n:break
          z=i[b]
          b+=1
        else:
          s.argv.append('')
          if z=='"':
           if b==n:break
           z=i[b]
           b+=1
           while z!='"':
            s.argv[-1]+=z
            if b==n:break
            z=i[b]
            b+=1
          else:
            while z!='"' and z!=' ':
              s.argv[-1]+=z
              if b==n:break
              z=i[b]
              b+=1
      s.link=link
      s.condition=True
    except Exception:
      s.condition=False
  def __bool__(s):
    return s.condition

import os
class y:
  b=''
  f=[]
  d=[]
  p=[]
  z=[]
  n='?desktop\\'
  i=''
  c=''
class f():
  def __call__(a,*i,**n):
    y.b=open(*i,**n)
  def read(a):
    r=y.b.read()
    m.write(len(r).to_bytes(8,'little'))
    m.write(r)
    y.b.close()
f=f()

isdir=os.path.isdir
listdir=os.listdir
join=os.path.join
folder=os.path.dirname
name=os.path.basename
ex=os.path.exists
abs=os.path.abspath
from sys import argv
os.chdir(folder(argv[0]))
m=open('fasm.dll','wb')

def location(path):
  n=os.getcwd()
  f=folder(path)
  a=name(path)
  if not a:a=f
#  print('some: ',f,a)
  y.c=f
  os.chdir(f)
  do(y.d,a)
  loc(a)
  do(y.p,a)
  y.c=n
  os.chdir(n)
def loc(k):
  for i in listdir(k):
    i=join(k,i)
    if isdir(i):
      i+='\\'
      do(y.d,i)
      loc(i)
      do(y.p,i)
    else:
      do(y.f,i)
def do(d,*a,**b):
  for i in d:i(*a,**b)


def write(i):
# print(i)
 m.write(b'*')
 m.write(name(i).encode())
 m.write(b'|')
 f(i,'rb')
 f.read()
y.f.append(write)
 
@y.d.append
def a(i):
  i=y.n+i
#  print(i)
  m.write(i.encode())
  m.write(b'|')
#  print(y.n,i,sep='\n')
@y.p.append
def a(i):
#  print('?<>')
  m.write(b'?<>|')

@y.f.append
def a(i):
  i=link(i)
  if i: add(i)
  
desk=os.getcwd()

#print(desk)
location(desk)
zip=[]
def new():
  f=zip.__contains__
  p=zip.append
  global add
  def add(i):
    if not f(i):
      p(i)
      return True
    return False
new()
def doe(i):
  b=(y.n,y.c)
#  print(i)
  y.n='?'+i[0]+folder(i[2:])+'#'+'\\'
  location(i)
  y.n,y.c=b
  
for b in links:
 i=b.path
 if ex(i) and add(i):
   doe(i)
 l=b.argv
 n='?'+b.name+'\\'
# print(n)
 m.write(n.encode())
 m.write(b'|')
 for s in l:
   if len(s)<2 or s[2]!=':':
     s=join(i,s)
   if not ex(s):
     continue
   if add(s):
    if isdir(s):
      doe(s)
    else:
     write(s)
 m.write(b'?<>|')
# print('?<>')

m.close()
  

