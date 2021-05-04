r=[]
add=r.append
class tr:
    x,y=0,0
    vx,vy=0,0
#*
@add
def i(a):
    tr.y+=a

@add
def i(a):
    tr.vy+=a

@add
def i(a):
    tr.x+=a

@add
def i(a):
    tr.vx+=a
#-
@add
def i(a):
    tr.y-=a

@add
def i(a):
    tr.vy-=a

@add
def i(a):
    tr.x-=a

@add
def i(a):
    tr.vx-=a
#~
for  i in range(int(input())):
    a,b=map(int,input().split())
    r[a-1](b)

if tr.vy:
    a=b=( (abs(tr.vy) **2 ) / 2)   **0.5
    if tr.vy<0:
        
        tr.x-=a
        tr.y-=b
    else:
        tr.x+=a
        tr.y+=b
        
if tr.vx:
    a=b=( (abs(tr.vx) **2 ) / 2)   **0.5
    if tr.vx<0:
        tr.x-=a
        tr.y+=b
    else:
        tr.x+=a
        tr.y-=b


a,b=round(tr.x,3), round(tr.y,3)
print(a,b)
