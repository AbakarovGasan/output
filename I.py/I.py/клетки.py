t=input().strip()
a,b=ord(t[0])-64, int(t[1])
if (a%2+b%2)%2:
    print('WHITE')
else :
    print("BLACK")
