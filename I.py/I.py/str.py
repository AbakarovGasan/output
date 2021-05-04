
import sys,os
import time as s
import creator as df
import shutil as j

flame=sys.argv[1:]
i=0
n=input('имя:')
for f in flame:
     i+=1
     d=os.path.dirname(f)
     r,t=os.path.splitext(os.path.basename(f))
     old=str(df.full(d,r)+t)
     print(old,'''
!//old\\\\!''')
     new=str(df.full(d,n)+t)
     print(new,'''
!//new\\\\!''')
     os.rename(f,new)

a=input()
