from os import listdir
from os.path import splitext, dirname,join
from creator import crfolder,rename
def ext(h):
    f,g=splitext(h)
    return g
for a in listdir(dirname(__file__)):
    x=ext(a)
    crfolder(dirname(__file__)+'/'+x)
    rename(dirname(__file__)+'/'+a,dirname(__file__)+'/'+join(x,a))
    print(join(x,a))
    
