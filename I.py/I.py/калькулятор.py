m=int(input())
t=list(range(m))
u={}
for i in range(2,m+1):
  if not i%3:
    j=i//3
    i-=1
    t[i]=t[j-1]+1
    u[i]=3
  elif not i%2:
    j=i//2
    i-=1
    t[i]=t[j-1]+1
    u[i]=2
  else:
    i-=1
    t[i]=t[i-1]+1
    u[i]=1
print(t[-1])

