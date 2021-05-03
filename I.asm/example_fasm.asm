macro syscall a, b, c, d {
   if ~(a eq)
       mov eax, a
   end if
   if ~(b eq)
       mov ebx, b
   end if
   if ~(c eq)
       mov ecx, c
   end if
   if ~(d eq)
       mov edx, d
   end if  
   int 0x80
}

format ELF executable 3

segment readable executable

entry main

main:

syscall 4, 0, msg, 13
syscall 11, msh, mdj, 0
syscall 1, 0, 0, 0


segment readable writable
point dd   0
msg  db 'hello world!', 10, 0
msh  db '/bin/bash', 0
msj  db '/snap/bin/log', 0
msk  db 'sdfsf',     0
msl  db 'we34',      0
mdj  dd  msh, msj, msk, msl, 0
