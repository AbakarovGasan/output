a=int(input())
b=int(input())
c=int(input())
w=3*a+b-c
w,j=divmod(w,3)
if j:w+=1
if w<0:
    print(0)
else:
    print(w)
