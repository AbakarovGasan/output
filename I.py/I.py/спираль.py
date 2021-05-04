#def main():
n=int(input())

d=[n+1]
p=[]

x=k=n



b=0

print( *(i for i in range(1,n+1)) )

def dec(a):
   for t in range(len(a)):
         a[t]-=1
   return a
def inc(a):
   for t in range(len(a)):
         a[t]+=1
   return a

for i in range((n-1)//2):
#   print('b:' ,b,'x:',x,)
   b=b+x*2+(x-2)*2
   x-=1
   e=b+x
   x-=1
   
   print( *p, *(i for i in range(b,e) )   , *d  )
   
   p.append(b)
   d.insert(0,e-1)
   dec(p)

   inc(d)
  # print(p,d)
 
#   print(p,d)

#

if not n%2:
   p.append(d[0]+1)
else:
   del d[0]

#print("%%%%%%$$$$$$$$$$$###########")


for i in range(n//2):
   b=p.pop(-1)
   e=d.pop(0)-1
  # print()
 #  print(b,e)
   print( *p, *(i for i in range(b,e,-1) )   , *d  )
   dec(p)
   inc(d)


   
 
   
