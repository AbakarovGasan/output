function sep(k:real; i:real):real;
var sum:real;
begin
sum:=1;
if i<0 then 
begin 
repeat
i+=1;
sum*=k;
until i=0;
sum:=1/sum;
end
else 
begin
while i<>0 do begin
i-=1;
sum*=k; end;
result:=sum;
end;end;

var a,b,c,d,q1,q2,q3:real;
begin
writeln('a, b, c, d = ');
readln(a,b,c,d);



end.
