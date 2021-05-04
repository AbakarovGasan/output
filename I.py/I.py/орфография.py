a,b=input().split()
a=int(a)
b=list(b)
del b[a-1]
print(*(i for i in b) , sep='')
