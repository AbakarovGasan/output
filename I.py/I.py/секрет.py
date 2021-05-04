k=''
c=int(input())
if c:
    k+=input()
    c-=1
    while c:
        k+='\n'
        k+=input()
        c-=1
b=k.count('b')+k.count("B")
g=k.count('g')+k.count("G")
print(k, end=' is ')
if b>g:
    print('A BADDY')
elif b<g:
    print("GOOD")
else:
    print("NEUTRAL")

    
