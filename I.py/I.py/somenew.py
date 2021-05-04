def r3():
 graph={}
 n,m=map(int,input().split())
 for i in range(1,n+1):
    graph[i]=[]
 for i in range(n):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

 visited=[]

 def dfs(v):
    print(v)
    visited.append(v)
    for i in graph[v]:
        if i not  in visited:
            dfs(i)

 dfs(1)
 globals().update(locals())
def fb(v,p):
    

#r3()



'''
j=lambda :list(map(int,input().split()))
#Заключительный этап 2018, 4 февраль
def r1():#Задача A. Кольцевые гонки
 n,m=j()
 p=j()
 q={}
 we=q.setdefault
 l=0
 k=1
 for i in p:
    we(i,0)
    v=q[i]+1
    q[i]+=1
    if v>l:
        l=v
        k=i
 print(k)
#def r2():
   ''' 
    
