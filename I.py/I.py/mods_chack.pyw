from time import sleep
while 1:
 d=open(r"C:\Users\Пользователь\Documents\My Games\Runic Games\Torchlight 2\modlauncher.sch",'rb')
 a=d.readlines()[:-2]
 d.close()
 g=''
 try:
     g=open(r"C:\Users\Пользователь\Documents\My Games\Runic Games\Torchlight 2\python_is_a_best.sch",'rb')
     f=g.readlines()
     g.close()
 except FileNotFoundError: f=[] 
 del g
 del d
 try:
  t=open(r"C:\Users\Пользователь\Documents\My Games\Runic Games\Torchlight 2\python_is_a_best.sch",'ab')
  for i in a:
    if not i in f:
        t.write(i)
  t.close()
 except PermissionError: pass
 sleep(2)
