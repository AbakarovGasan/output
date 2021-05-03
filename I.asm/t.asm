format PE console 4.0
include 'win32ax.inc'
entry start





section '.data' readable writeable

        expr dd "D:\*",0
        k rb 4096
        z rd 256
        y dd z
        t rb 4096
        b rd 256
        n dd b

        find rd 256
        sh dd  find
        fin dd 0
        fout dd 0
        flen dd 0
        fbuf rb 1024*1024
        srch WIN32_FIND_DATA

section '.code' executable
macro write n{
invoke fread , fbuf, 1, n , [fin]
invoke fwrite, fbuf, 1, n , [fout]}

macro fput [n]{
invoke fputs, n , [fout]}

macro getflen{
invoke fseek,[fin],0,2
invoke ftell,[fin]
mov [flen],eax
invoke fseek,[fin],0,0}

macro exit{
invoke ExitProcess, 0}

macro chdir k {
invoke _chdir, k}

macro point z{
mov esi, z
mov esi,[esi]}

macro dir a{
invoke FindFirstFile, a, srch
mov esi, [sh]
mov [esi], eax
}

macro next{
point [sh]
invoke FindNextFile, esi, srch
cmp eax, 0
}

macro close{
point [sh]
invoke FindClose, esi}


macro exit{
invoke ExitProcess,0}


macro put [p]{
invoke puts, p}

start:


      invoke puts, <'hello',0>

      dir expr

loli:
put srch.cFileName
next
jne loli


      invoke _getch
      exit
     ;

;put srch.cFileName



section '.idata' import data readable writeable

library kernel,'kernel32.dll',\
msvcrt,'msvcrt.dll',\
user32,'user32.dll'

       import msvcrt,\
__getmainargs,'__getmainargs',\
fopen,'fopen',\
fseek,'fseek',\
ftell,'ftell',\
malloc,'malloc',\
free,'free',\
fread,'fread',\
fwrite,'fwrite',\
fclose,'fclose',\
printf,'printf',\
_getch,'_getch',\
_chdir,'_chdir',\
puts,'puts' ,\
scanf,'scanf'

  import  kernel,\
          GetStdHandle,'GetStdHandle',\
          WriteFile,'WriteFile',\
          ExitProcess,'ExitProcess',\
          lstrlen,'lstrlen',\
          FindFirstFile,'FindFirstFileA',\
          FindNextFile,'FindNextFileA',\
          FindClose,'FindClose'
