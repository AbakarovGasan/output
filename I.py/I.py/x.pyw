import pygame
from pygame import *
from clicker import *
def returnclick(a,b,c=''):
    return 'click('+str(a)+','+str(b)+',"'+c+'")\n'
def main():
    lo=-1
    from time import time,sleep
    d={K_p:'',K_t:'rightclick',K_y:'leftclick',K_g:'rightup',K_h:'leftup',K_b:'rightdown',K_n:'leftdown'}
    t={K_q:[1,0],K_a:[10,0],K_z:[150,0],K_w:[0,1],K_s:[0,10],K_x:[0,150],K_e:[-1,0],K_d:[-10,0],K_c:[-150,0],K_r:[0,-1],K_f:[0,-10],K_v:[0,-150]}
    ff={K_j:10,K_k:150,K_l:1500}
    pygame.init()
    screen = pygame.display.set_mode((150,50))
    pygame.display.set_caption("kilobyte")
    bg = Surface((150,50))
    bg.fill(Color("#999999")) 
    x=0
    y=0
    f=''
    q=0.0
    ki=True
    tt=open(r"D:\Рабочий стол\txt.txt",'w')
    tt.write('from clicker import *\n')
    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                f=returnclick(x,y)
                tt.write(f)
                print(f)
                tt.close()
                exit()
            if e.type == KEYDOWN:
              if e.key ==K_u:
                  f=returnclick(x,y,'leftclick')
                  tt.write(f)
                  print(f)
                  ftu='write("'+input()+'")\n'
                  tt.write(ftu)
                  print(ftu)
                  exec(f+ftu)
              if e.key==K_i:
                if ki:
                    ki=False
                    q=time()
                else:
                    ki=True
                    q=time()-q
                    f='sleep('+str(q)+')\n'
                    tt.write(f)
                    print(f)
              if e.key in d:
                f=returnclick(x,y,d[e.key])
                exec(f)
                tt.write(f)
                print(f)
              if  e.key in t:
                l=t[e.key]
                x+=l[0]
                y+=l[1]
                click(x,y)
              if e.key==K_m:
                lo=lo*(-1)
              if e.key in ff:
                l=ff[e.key]*lo
                f='scroll('+str(l)+')\n'
                tt.write(f)
                print(f)
                exec(f)
        screen.blit(bg, (0,0))     
        pygame.display.update() 

if __name__ == "__main__":
  main()
#click(410,240,'leftclick',2)
#r=win32api.keybd_event(ord('b'),0, 0, 0)
#r=win32api.keybd_event(ord('b'),0, 2, 0)

