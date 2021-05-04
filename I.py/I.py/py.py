i=open("D:/Рабочий стол/txt.txt",'w')
r=1
e=''
w=15
a=1
q=True
while r:
    if not q:
        e=input(a)
        if e:
         i.write('      '+str(a)+') '+e+"\n")
         a+=1
        else:
         i.write('\n')
         q=True
         a=1
    if q:
        e=input(w)
        if e:
         i.write(str(w)+"."+e+':'+'\n')
         q=False
         w+=1
        else:
            r=False
i.close()
'''
e=open("D:/Рабочий стол/txt.txt",'r')
a=e.readlines()
for m in a:
    x=True
    print(m)
    while x:
        if m[0]=='':
            m=m[1:]
        else:
            x=False
d=''
for m in a:
    d+=m
e.close()
e=open("D:/Рабочий стол/txt.txt",'w')
e.write(d)
e.close()'''
