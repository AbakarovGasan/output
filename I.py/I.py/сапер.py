n,m,k=map(int,input().split())
p=[]
print=__import__('sys').stdout.write
for i in range(n+2):
    z=[]
    p.append(z)
    for i in range(m+2):
        z.append(0)
for i in range(k):
    y,x=map(int,input().split())
    p[y][x]=201
    
    p[y+1][x]+=1
    p[y+1][x+1]+=1
    p[y][x+1]+=1
    p[y-1][x+1]+=1
    p[y-1][x]+=1
    p[y-1][x-1]+=1
    p[y][x-1]+=1
    p[y+1][x-1]+=1
for s in p[1:-1]:
    for i in s[1:-1]:
        if not i:
            print('.')
        elif i>200:
            print('*')
        else:
            print(str(i))
    print('\n')
