z=0
import sys
k=sys.stdout
l={}
class u:
    j={}
    b=''
def i(k,n,l):
    u.j=l
    u.b=k[n:n+1]
    l.setdefault(u.b,{})
    n+=1
    if len(k)!=n:
        i(k,n,l[u.b])
while 1:
  try:
    b=chr(z)
    k=b.encode()
    i(k,0,l)
    u.j[u.b]=b
  except UnicodeEncodeError:
      pass
  except ValueError:
      break
  finally:
      z+=1
open(r"D:\Doc\Output\.py\compiler\tt.py",'w',encoding='utf-8').write('tt='+repr(l))
