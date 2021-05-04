def t(a):
    for i in range(a):
        yield int(input())
def r1():
 k,x,y=t(3)
 a,b=divmod(y,x)
 if b:a+=1
 print(x*a)
r1()
