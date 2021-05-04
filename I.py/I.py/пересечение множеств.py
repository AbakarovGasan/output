t=lambda : list(map(int,input().split()))

n,m=t()
q=t()
w=t()
l=[]
for i in w:
    if i in q:
      if not i in l:
        l.append(i)
l.sort()
import sys
write=sys.stdout.write

for i in l:
  write(str(i))
  write(" ")
