for i in range(int(input())):
    n=int(input())-2
    t=list(map(int,input().split() ) )
    t.remove(max(t))
    k=max(t)-1
    if n<k:
        print(n)
    else:
        print(k)
