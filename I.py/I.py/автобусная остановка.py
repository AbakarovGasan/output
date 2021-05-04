input()
l=0
for i in map(int,input().split()):
    l+=1
    if not i>437:
        print('Crash',l)
        exit()
print('No crash')
    
