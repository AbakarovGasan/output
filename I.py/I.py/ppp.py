from creator import remove, listpath, name
from time import sleep
t=listpath(r'D:\Рабочий стол')
h=[]
for t in t:
 if '.#.' in name(t):
  remove(t)
  print(t)
sleep(0.4)  
