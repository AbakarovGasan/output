uses graphABC;
procedure f;
var
 m,n:integer;
 a,d,z:real;
begin
 writeln('m=,n=');
 read(m,n);
 writeln('����� �1');
 read(a);
 writeln('����� d');
 read(d);
 if m<n then
 for var i:=m to n do begin
 z:=z+a;
 a:=a+d;
 end
 else
 for var i:=n to m do begin
 z:=z+a;
 a:=a+d;
 end;
 write('����� ���������� ',z);
end;
procedure u;
var
 m,n:integer;
 a,q,d,z:real;
begin
 writeln('����� �(m)');
 read(q);
 writeln('����� �(n)');
 read(a);
 writeln('����� d');
 read(d);
 if m<n then
 for var i:=m to n do begin
 z:=z+a;
 a:=a+d;
 end
 else
 for var i:=n to m do begin
 z:=z+a;
 a:=a+d;
 end;
 write('����� ���������� ',z);
end;
begin
end.