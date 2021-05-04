n,m=map(int,input().split())
dv=[]
i=0
while i<n:
    dv.append(list(input()))
    i+=1

s,t=0,0
l=[]

out=0

def S():
#    print('s')
    global out
    s=l[-1]
    a,b=s[1]+s[3],s[2]
    i=a+1
#    print(i,a,b)
    while i<n:
        g=dv[i][b]
        if g=='.':
            i+=1
#            print('>')
        elif g in ['#','N']:
            dv[i][b]='#'
            dv[a][b]='#'
            del l[-1]
            return 
        else:
            s[3]=i-s[1]-1
            l.append([dc[g],i,b,0])
            return 
#    print('end')
    del l[-1]
    out+=1
    dv[s[1]][s[2]]='.'

def N():
#    print('n')
    global out
    s=l[-1]
    a,b=s[1]-s[3],s[2]
    i=a-1
#    print(i,a,b)
    while i>-1:
        g=dv[i][b]
        if g=='.': i-=1
        elif g in ['#','S']:
            dv[i][b]='#'
            dv[a][b]='#'
            del l[-1]
            return 
        else:
            s[3]=s[1]-i+1
            l.append([dc[g],i,b,0])
            return
#    print('end')
    del l[-1]
    out+=1
    dv[s[1]][s[2]]='.'

def E():
#    print('e')
    global out
    s=l[-1]
    b,a=s[2]+s[3],s[1]
    i=b+1
#    print(i,a,b)
    while i<m:
        g=dv[a][i]
        if g=='.': i+=1
        elif g in ['#','W']:
            dv[a][i]='#'
            dv[a][b]='#'
            del l[-1]
            return 
        else:
            s[3]=i-s[1]-1
            l.append([dc[g],a,i,0])
            return 
    del l[-1]
    out+=1
    dv[s[1]][s[2]]='.'

def W():
#    print('w')
    global out
    s=l[-1]
    b,a=s[2]-s[3],s[1]
    i=b-1
#    print(i,a,b)
    while i>-1:
        g=dv[a][i]
        if g=='.': i-=1
        elif g in ['#','W']:
            dv[a][i]='#'
            dv[a][b]='#'
            del l[-1]
            return 
        else:
            s[3]=s[1]-i+1
            l.append([dc[g],a,i,0])
            return 
    del l[-1]
    out+=1
    dv[s[1]][s[2]]='.'
            
dc={
    "N":N,
    "S":S,
    "W":W,
    "E":E,
    }




while s<n:
#    print(s,';')
    t=0
    while t<m:
#        print(t,'-', end='')
        g=dv[s][t]
#        print(g)
        if g in ['.','#']:
            t+=1
            continue
        l.append([dc[g],s,t,0])
        while l:
            l[-1][0]()
        t+=1
    s+=1
print(out)



        
