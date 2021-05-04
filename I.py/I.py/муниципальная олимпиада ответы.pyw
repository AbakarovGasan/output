def do(d):
 from time import time
 class Profiler(object):
    pin=open('process time.txt','w')
    def __enter__(self):
        self._startTime = time()
         
    def __exit__(self, type, value, traceback):
        print ("Elapsed time: {:.3f} sec".format(time() - self._startTime) , file = pin)

def main2():
 path=open('input.txt','r')
 def i():
  global path
  return int(path.read(1))
 n=i()
 m=i()
 if m==n:
  m=0
 k=i()
 while k:
  j=i()%n
  if m==1:
    m=j
  elif m==j:
    m=1
  k-=1
 if m==0: m=n
 path.close()
 path=open('output.txt','w')
 print(m,file=path)
 path.close()
def main1():
 path = open('input.txt','r')
 def i():
  global path
  return int(path.read(1))
 pat=open('output.txt','w')
 print( ((-i()+i() ) //i() ) +1,pat)
 path.close()
 pat.close()
do(main2)
