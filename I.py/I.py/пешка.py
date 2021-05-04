j=lambda: map(int,input().split())
x,y =j()
a,b =j()
v=b-y

if b<y:
    print("NO")
    
elif a!=x:
    print("NO")

elif y==2 and b==4:
    print("YES")
    
elif v==1:
    print('YES')

else:
    print("NO")
