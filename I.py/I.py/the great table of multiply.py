
i=lambda:list(map(int,input().split()))

def r():
 global i
 n,m=i()
 k=[]
 
 for f in range(n):
    k.append( i() )
 if n==1:
     z=k[0]
     b=k[0][1]-k[0][0]
     a,w=divmod(k[0][0],b)
     assert (not w), 'false'
     for i in range(m):
         assert (b)*(i+a)==z[i], 'false'
     return True

 if m==1:
     a=k[1][0]-k[0][0]
     b,w=divmod(k[0][0],a)
     assert (not w), 'false'
     for i in range(n):
         assert (b+i)*(a)==k[i][0], 'false'
     return True
         
 a=k[1][0]-k[0][0]
 b=k[0][1]-k[0][0]
 for i in range(m):
     for f in range(n):
         assert (i+a)*(f+b)==k[f][i], 'false'
 return True


try:
    print(str(r()).lower())
except AssertionError as g:
    print(g)

         
