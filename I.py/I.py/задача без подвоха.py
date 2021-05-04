def cnt(o,z):
    for i in o:
        if not i in z:
            return False
    return True

for i in range(int(input())):
    o=input()
    y=int(o)
  #  print(o , y)
    if cnt(o,'1'):
        print(0)
        continue
    for t in range(2000000000):
        z=2<<t
        if cnt(o,str(z)):
            print(t+1)
            break
    
   
