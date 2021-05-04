import sys
r=sys.stdin.read
def cin():
    a=''
    b=r(1)
    while  str.isspace(b):
        b=r(1)
    while not str.isspace(b):
        a+=b
        b=r(1)
    return int(a)

n=cin()

q=cin()

k=q
q=q>>1
a=[1]
i=1
m=0
while i<n:
    i+=1
    l=cin()
    m+=l
    if q>=l:
        print('d',q)
        k+=l
        a.append(i)
if (k<<1)>=m and len(a)>1:
    print(len(a))
    print(*a)
else:
    print(0)


