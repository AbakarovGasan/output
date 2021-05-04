from book import *
from creator import *
from os.path import splitext as l, join
file.new(__file__)

g=open('object.txt','w')

h=0
for i in location(old):
  m,v=l(i)
  print(m,file=g)
  rename(i,join(new,v,str(h)+v))
  h+=1
g.close()
