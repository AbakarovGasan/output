def setup(**i):
    import subprocess as shell
    import sys 
    f=['version','about']
    g=['0.1','']
    v=i.setdefault
    for t in range(len(f)):
        v(f[t],g[t])
        pass
    b=__import__('os').path.basename
    d=__import__('os').path.dirname
    if 'path' in i:
         z=i['path']+'\\'+i['name']
         v('files',z)
    if 'files' in i:
        try:z=i['files']
        except TypeError:
            try:z=i['files'][0]
            except TypeError:
                z=i['files'][0][0]
        v('name',z)
    v('path',d(i['name']))
    if type(i['files'])==type(''):
        i['files']=((i['files'],),)
    else:
        b=i['files']
        x=[]
        for z in b:
            if type(z)==type(''):
               x.append((z,))
            else:
                x.append(z)
        i['files']=x
    i['version']=str(i['version'])
    lk=(i['path'],i.get('do'))
    for z in i:
        i[z]=repr(i[z])
    i='''from cx_Freeze import setup, Executable as exe
setup(name = {name}, version = {version},
    description = {about},
    executables = [exe(*t) for t in {files}] )'''.format(**i)
    print(i)
    with open(lk[0]+'\\'+'setup.py','w',encoding='utf-8') as f:
        f.write(i)
        f.close()
        if lk[1]:
          if input('do? '):
            z=('python',f.name,'build')
            print(z)
            print(repr(shell.run(z)))
#setup(files="D:\Doc\Output\.py\compiler\main.py",do=True)
            
        
