from globals import *
from sys import argv
from terminal import kernel as __k

f=open(r"D:\Doc\Output\.py\compiler\[].txt",'rb')
__k=__k(kernel_utils)
global_utils(__k)
__k.mode(file('utf-8'))
__k.open(f)
__k.run(start)
