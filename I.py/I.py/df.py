from math import ceil
g = lambda: list(map(int,input().split()))

def r(n,k,x,y,     q,       *ar):
 q=range(q)
 i=((k-1)*y)+x
 a,b=divmod(n,k)
 o=a*i+b*y
 del a ,b

 def rest2(s):
     s=s%o
     if s==0:
      return 7
     j,s=divmod(s,i)
     j*=k
 def rest(s):
   s=s%o
   if s==0:
      return 7
   j,s=divmod(s,i)
   j*=k
   if s:
      q=ceil(s/y)
      
      if q>k:
         q=k
      j+=q
   return j

 if y:
   for m  in q:
    print(rest(ar[m]))
 else:
  for m  in q:
    print(rest2(ar[m]))
     
    

n,k,x,y=g()
q=int(input())


r(n,k,x,y,  q,  *g())
    
