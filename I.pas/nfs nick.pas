uses crt;
var sb := System.Environment.GetFolderPath(System.Environment.SpecialFolder.LocalApplicationData)+'\nfs underground 2';
var i:integer;
s:char;
c:string='               ';
h:file of char;
j:file of char;

procedure go();
begin
while i>0 do begin
i-=1;
read(j,s);
write(h,s);
end;
end;
procedure read();
var i:byte;
begin
I:=1;
while True do begin
s:=readkey();
if s=chr(8) then begin
write(s);
write(' ');write(s);
i-=1;
if i<1 then I:=1;
end
else if s=chr(13) then break
else if i<8 then
 begin 
 write(s); 
 c[i]:=s; 
 I+=1;
end;
 end;
 writeln();
 c:=c.Substring(0,i-1);
// writeln(c,' ',c.Length);
// readln(s);
 end;


begin
read();
mkdir(sb);
mkdir(sb+'\'+c);
i:=53797;
assign(j,'#(0_0)#');
reset(j);
assign(h,sb+'\'+c+'\'+c);
rewrite(h);

go();

j.Seek(53804);
I:=1;
repeat
write(h,c[i]);
i+=1;
until i>c.Length;
while i<8 do 
begin
write(h,chr(0));
i+=1;
end;

i:=1162;
go();

end.