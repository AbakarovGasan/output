import os,shutil
import creator as od
path = 'D:/Desktop/работы/project/assets/models/characters'
folder = 'shot_01'
pad = 4
newpath = 'D:/Desktop'

sy=''
files = os.listdir(path)
ht=0
flames=[]
names=[]
m=0
de=[]
'''folders delete'''
while m<(len(files)):
     if not os.path.isfile(od.full(path,files[m])):
          del files[m]
          m-=1
     m+=1
'''возвращает имя'''
def r(files):
     n,v=os.path.splitext(files)
     return n
'''возвращает тип'''
def s(files):
     n,v=os.path.splitext(files)
     return v
'''удаляет все цифры'''
def q(files):
     m=''
     n=r(files)
     for u in range(len(n)):
          if not n[u].isdigit():
               m+=n[u]
     return m
'''удаляет цифры на конце'''
def h(files):
     n=r(files)  
     while n[-1].isdigit():
          n=n[:-1]
     return n
'''удаляет буквы в начале'''
def u(files):
     b=h(files)
     v=files.replace(b,'')
     return r(v)
        
for p in files:
     names.append(h(p))
     flames.append(u(p).zfill(pad))
     print(h(p),'''
!//name\\\\!''')
     print(u(p).zfill(pad),'''
!//flame\\\\!''')

od.crfolder(od.full(newpath,folder))

for q,k in enumerate(files):
     old=od.full(path,k)
     guf=folder+'_'+str(flames[q])+s(k)
     new=od.full(newpath,folder,guf)
     print(old)
     print('!//old\\\\!')
     print(new)
     print('!//new\\\\!')
     if not os.path.exists(new):
          shutil.copy2(old,new)
     
for i in range(int(min(flames)),int(max(flames))):
     if not i in flames:
          de.append(folder+'_'+str(i).zfill(pad))

m=0
     
while ht<len(de):
     sy+=de[ht]+'  |   '
     ht+=1
     m+=1
     if m == 5:
          print(sy)
          m=0
          sy=''        
if m<5:
     print(sy)
print('!//need\\\\!')

