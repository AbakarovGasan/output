from os.path import dirname
from os import rename,listdir,mkdir
def remove(Path):
    #from creator import crfolder
    from os.path import exists,join
    from os.path import basename
    if exists(Path):
        waste=Path[:2]+'/'+"#waste#"
        crfolder(waste)
        w=listdir(waste)
        i=str(len(w))
        crfolder(join(waste,i))
        rename(Path,join(waste,i,basename(Path)))
def crfolder(Path):
    from os import mkdir
    try: mkdir(Path)
    except FileNotFoundError: crfolder(dirname(Path))
    except FileExistsError:pass
    
from sys import prefix
from os.path import join
from os import system
from shutil import copy2 as copy

bt=dirname(__file__)

g=join(bt,'!mods!')

prefix=join(prefix,'Lib')
 
print(prefix,'\n')
k=listdir(g)

for k in k:
  remove(join(prefix,'Lib',k))
  copy(join(g,k),join(prefix,k))
  print(join(prefix,k))
  
t=open(join(bt,'@.consolecommands'),'r',encoding='utf-8')
exec(t.read())
t.close()
print()
for p in q: print(p)
if input('\n')=='go':
  for p in q:
    system(p)
  input()
