from clicker import *
x=720
y=200
click(x,y,"leftclick",repeat=7)
z='500000000'
write(z)
click(x-378,y,"leftclick")
for i in range(230):
 click(x,y+20,"leftclick",repeat=7)
 write(z)
 click(x-378,y+20,"leftclick")
 click(x,y+40,"leftclick",repeat=7)
 write(z)
 click(x-378,y+40,"leftclick")
 click(x,y+60,"leftclick",repeat=7)
 write(z)
 click(x-378,y+60,"leftclick")
 
 scroll(-150)
 
