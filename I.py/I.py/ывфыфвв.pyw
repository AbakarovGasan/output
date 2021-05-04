from book import *
from creator import *
from os.path import basename,splitext
file.new(__file__)


h=open('object.txt')
l=h.readlines()
for i in listdir(new):
   for v in listdir(i):
        rename(v,l[int(splitext(basename(v))[0]) ][:-1]+basename(i))
h.close()
        
        
