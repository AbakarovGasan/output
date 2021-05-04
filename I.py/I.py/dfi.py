
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
def full(a='',b='',c='',d='',e=''):
    h='/'
    if not b=='':
        path=a+h+b
    if not c=='':
        path=a+h+b+h+c
    if not d=='':
        path=a+h+b+h+c+h+d
    if not e=='':
        path=a+h+b+h+c+h+d+h+e
    return path

def exists(path):
    from os.path import exists as er
    if er(path):
        return True
    else:
        return False

def crfolder(Path):
    from os import mkdir
    t=[]
    for i in Path.split('\\'):
        t.extend(i.split('/'))
    Path=''
    for i in t:
      Path+=i+'\\'
      if not exists(Path):
        mkdir(Path) 
def dlfolder(Path):
    from os import rmdir
    if exists(Path):
        rmdir(Path)
def remove(Path):
    from os import rename,listdir,mkdir
    from os.path import basename
    if exists(Path):
        waste=Path[:2]+'/'+"#waste#"
        crfolder(waste)
        w=listdir(waste)
        i=str(len(w))
        crfolder(full(waste,i))
        rename(Path,full(waste,i,basename(Path)))
def rename(old,new):
    from os import rename
    if exists(old) and not exists(new):
        rename(old,new)
        
def crtree(Root,List):
        if List:
            for i in List:
                s=i[0]
                g=full(Root,s)
                crfolder(g)
                crtree(g,i[1])
                pass
        else:
            pass
        
def dltree(Root,List):
        if List:
            for i in List:
                s=i[0]
                g=full(Root,s)
                dlfolder(g)
                dltree(g,i[1])    
        else:
            pass
        
def ext(files):
     from os.path import splitext
     n,v=splitext(files)
     return v
    
def listdir(path,Ext=None):
    from os import listdir
    n=[]
    if not Ext:
        n=listdir(path)
    else:
        d=listdir(path)
        for d in d:
            if ext(d)[-1]==Ext:
                n.append(d)
    return n

def listpath(path,Ext=None):
    from os.path import join
    n=[]
    d=listdir(path,Ext)
    for d in d:
        n.append(join(path,d))
    return n

def copy(Old,New,word=None):
     from os.path import isfile,join
     from shutil import copy2
     if isfile(Old):
          if not exists(New):
             copy2(New)
             if word:
                print(New,'''
!//load\\\\!''')
             pass
          elif word:
                print(New,'''
!//exists\\\\!''')
     if not isfile(Old):
      try:
         crfolder(Old,New)
         if not exists(New):
             if word:
               print(New,'''
!//load\\\\!''')
             pass
         elif word:
              print(New,'''
!//exists\\\\!''')        
         m=listdir(Old)
         new=[]
         old=[]
         if m:
             for s in m:
                 old.append(join(Old,s))
                 new.append(join(New,s))
             for s,v in enumerate(m):
                 copy(old[s],new[s],word)
      except BaseException:
            if not  exists(New):
                copy2(Old,New)
                if word:
                    print(New,'''
!//load\\\\!''')
            elif word:
                print(New,'''
!//exists\\\\!''')
                    

def location(path):
    t=[]
    from os.path import isfile
    if isfile(path):
        t.append(path)
    else:
        try:
            m=listpath(path)
            t.append(path)
            for m in m:
               t.extend(location(m))
        except BaseException:
            t.append(path)
    return t

def dir(p):
    from os.path import dirname
    return dirname(p)

def name(p):
    from os.path import basename
    return basename(p)

def setup(code=None):
 from os.path import dirname,join,basename
 tt={}
 tt['v.']=1.0
 tt['dscr']=''
 keys=['path','v.','name','target','file']
 logs=['content','dscr']
 if code:
  p=code
  o=''
  for t in p:
   if t!='\n': o+=t
  p=o
  del o
  r=[]
  r.append('')
  q=0
  b=True
  x=False
  for t in p:
   if x and not b and t=='}':
    b=True
   if t!=';' and b:
    r[q]+=str(t)
   if t==';' and b:
    q+=1
    r.append(str(''))	
   if not b:
    r[q]+=str(t) 
   if t=='{' and b:
    b=False
   if not b and t=='|':
    x=True
  p=r
  del r
  r=[]
  for t in p:
   if t:r.append(t)
  p=r
  del r
  for t in p:
    b=''
    r=0
    try:
     while t[0]==' ':
        t=t[1:]
    except Exception: pass
    try:
     while t[r]!=' ':
        b+=t[r]
        r+=1
    except Exception: pass
    try:
     while t[0]!=' ':
        t=t[1:]
     while t[0]==' ':
        t=t[1:]
     while t[-1]==' ':
        t=t[:-1]
    except Exception: pass
    if b in keys: tt[b]=t
    if b in logs: tt[b]=t[1:-2]
 if 'file' in tt.keys():
   if not 'name' in tt.keys():tt['name']=basename(tt['file'])
   tt['path']=dirname(tt['file'])
 if 'target' in tt.keys():
     with open(tt['target'],'rb') as file:
         ui=file.read()
         file.close()
     with open(join(tt['path'],tt['name']),'wb') as file:
         file.write(ui)
         file.close()
 if 'content' in tt.keys():
     with open(join(tt['path'],tt['name']),'w') as file:
         file.write(tt['content'])
         file.close()
 for t in tt:
  print(t,tt[t])
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''#
