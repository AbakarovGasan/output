from creator import *
ext=os.path.splitext
for i in listdir(''):
    print(i, ext(i)[1], 'output/'+ext(i)[1]+'/'+i)
    os.renames(i, 'output/'+ext(i)[1]+'/'+i)
