uses crt;
label tyu, endname;
var t:char;
n:byte;
b:boolean;
m:byte=10;
f:longint;
litle:longint;
filesearch:integer;
i:file of byte;

procedure search(have:longint);
var ri:byte;
begin
try 
while have<>litle do begin
litle:=0;
M:=1;
for var n:=1 to 8 do begin 
Read(i,ri);
litle+=ri*m;
m*=256;
end;
filesearch+=1;
i.Seek(filesearch);
end;
writeln(filesearch-1);
except on System.IO.EndOfStreamException do
writeln('not found');
end;
end;

procedure duel();
begin
if m<>16 then if f=0 then begin
write(t);
m:=16;
end;
end;

function res(gig:char):byte;
begin
case gig of 
'1':res:=1;
'2':res:=2;
'3':res:=3;
'4':res:=4;
'5':res:=5;
'6':res:=6;
'7':res:=7;
'8':res:=8;
'9':res:=9;
'0':res:=0;
'A':res:=10;
'B':res:=11;
'C':res:=12;
'D':res:=13;
'E':res:=14;
'F':res:=15;
'a':res:=10;
'b':res:=11;
'c':res:=12;
'd':res:=13;
'e':res:=14;
'f':res:=15;
'x':begin duel; res:=16; end;
'X':begin duel; res:=16; end;
else res:=16;
end;
end;

procedure read();
label hu;
begin
t:=readkey;
if t<>chr(13) then begin
if t<>chr(8) then begin
n:=res(t);

if n<m then begin if f=0 then if n=0 then goto hu;
 write(t); f*=m; f+=n;
 hu: end;

end
else begin
write(chr(8),' ',chr(8)); f:=f div m;
if b=true then begin if f=0 then m:=10; b:=false;end;
if f=0 then b:=true
end;
read()
end;
end;

begin
assign(i,'C:\Users\Пользователь\Documents\My Games\Runic Games\Torchlight 2\mods\elemental.mod');
reset(i);

while 1=1 do begin
m:=10;f:=0;
read();
writeln();
search(f);
end;
end.