t=list(map(int,input().split()))
a=t[:2]
b=[2:4]
c=[4:]
class vect():
    def __init__(a,d):
        b,c=d
        a.a=b
        a.b=c
        a.c=[b[0]-c[0],b[1]-c[1]]

vt1,vt2,vt3=map(vect,[[a,b],[b,c],[c,a]])

