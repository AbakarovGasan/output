def r1():
 d=[chr(i) for  i in range(65, 91)]
 t=input().upper()
 z=True
 for i in d:
     if not i in t:
         z=False
 print(z)

def r2():
    d=[]
    a=[chr(i) for i in range(65,91)]
    for  i  in a:
        k=i
        for i in a:
            k1=k+i
            for i in range(1000):
                d.append(k1+str(i).zfill(3))
    from random import choice
    for i  in range(int(input())):
        t=choice(d)
        d.remove(t)
        print( t)
def r3():
    t=input()
    k=0
    b=''
    z=1
    ch=t[0]
    try:
        for i in t:
            k+=1
            n=t[k]
            if ch==n:
                z+=1
            else:
                if z==1:
                    b+=ch
                    ch=n
                elif z>1:
                    b+=str(z)
                    b+=ch
                    ch=n
                    z=1
    except IndexError:
        if z==1:
            b+=ch
        elif z>1:
            b+=str(z)
            b+=ch
    print( b)

t=open('1.bat','w')
t.close()    

    
