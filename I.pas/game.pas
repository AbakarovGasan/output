uses graphABC , ABCobjects;
type
  pl = class public x, y, speed, damage, hp: integer;sprite: string;end;
  bt = class public x, y, speed, damage, hp: integer;sprite: string;end;
  pt = class public x, y, speed, damage, hp: integer;sprite: string; end;
  ok = class public x, y, speed, damage, hp: integer;sprite: string;end;

var
  u: bt;
  q: pt;
  i: pl;
  f: ok;
  
  ///видимость bot
  z, z2: integer;
  ///видимость bot2
  c, c2: integer;
  ///видимость bot3
  v, v2: integer;
  
  p: integer;
  l: integer;
  
  object1: PictureABC;
  object2: PictureABC;
  object3: PictureABC;
  object4: PictureABC;
  
  ///снаряд bot
  s: array[1..100] of PictureABC;
  pule: string;
  ///снаряд bot2
  s2: array[1..100] of PictureABC;
  pule2: string;
  ///снаряд bot3
  s3: array[1..100] of PictureABC;  
  pule3: string;
  
  ///h:x,b:y
  h, b, h2, b2, h3, b3: array[1..100] of integer;
  
  d, full: array[1..100] of integer;
  
  ///наводка bot
  z3, z4: array[1..100]of integer;
  ///наводка bot2
  c3, c4: array[1..100]of integer;
  ///наводка bot3
  v3, v4: array[1..100]of integer;
  
  mi: array[1..100]of boolean;
  ///очередь запуска снаряда
  second: array[1..100]of integer;
  
  fi: integer;
  num: integer;

//game launcher 
procedure o;
begin
  window.caption := 'first game';
  window.setpos(1, 1);
  window.setsize(1400, 800);
  window.IsFixedSize := true;
  window.Fill('D:\Desktop\игры/angry/FreshPaint-6-2017.04.02-04.00.41.png')
end;

//defense
procedure trish;
begin
  for var num := 1 to 10 do 
  begin
    s[num] := PictureABC.Create(0, 0, 'D:\Desktop\игры\angry/k.png');
    s[num].Destroy;
  end;
end;

procedure location;
begin
  for var num := 1 to 10 do 
  begin
    
    if z2 = 0 then if z <> 0 then if z3[num] = 0 then z3[num] := z;
    if z = 0 then if z2 <> 0 then if z4[num] = 0 then z4[num] := z2;
    
    if v2 = 0 then if v <> 0 then if v3[num] = 0 then v3[num] := v;
    if v = 0 then if v2 <> 0 then if v4[num] = 0 then v4[num] := v2;
    
    if c2 = 0 then if c <> 0 then if c3[num] = 0 then c3[num] := c;
    if c = 0 then if c2 <> 0 then if c4[num] = 0 then c4[num] := c2;
    
  end;
end;

procedure up;
begin
  if mi[num] = true then 
  begin
    if d[num] = 0 then s[num] := PictureABC.Create(h[num], b[num], pule);
    if d[num] < 100 then
    begin
      h[num] += full[num] * 10;
      d[num] += 1;
    end
        else 
    begin
      second[num] := 0;
      d[num] := 0;
      s[num].Destroy;
      h[num] := 0;
      b[num] := 0;
      z3[num] := 0;
      z4[num] := 0;
      c3[num] := 0;
      c4[num] := 0;
      v3[num] := 0;
      v4[num] := 0;
      mi[num] := false;
    end;
  end; 
end;

procedure boom;
begin
  begin
    if z3[num] <> 0 then
    begin
      mi[1] := true;
      full[num] := z3[1];
      if h[num] = 0 then h[1] := i.x;
      if b[num] = 0 then b[1] := i.y;
      up;
      s[num].MoveTo(h[num], b[num]);
    end;
    if z4[1] <> 0 then
    begin
      mi[1] := true;
      full[1] := z4[1];
      if h[1] = 0 then h[1] := i.y;
      if b[1] = 0 then b[1] := i.x;
      up;
      s[1].MoveTo(b[1], h[1]);
    end;
  end;
end;

procedure boom2;
begin
  begin
    if c3[2] <> 0 then
    begin
      mi[2] := true;
      full[2] := c3[2];
      if h[2] = 0 then h[2] := q.x;
      if b[2] = 0 then b[2] := q.y;
      up;
      s[2].MoveTo(h[2], b[2]);
    end;
    if c4[2] <> 0 then
    begin
      mi[2] := true;
      full[2] := c4[2];
      if h[2] = 0 then h[2] := q.y;
      if b[2] = 0 then b[2] := q.x;
      up;
      s[2].MoveTo(b[2], h[2]);
    end;
  end;
end;

procedure boom3;
begin
  begin
    if v3[2] <> 0 then
    begin
      mi[3] := true;
      full[3] := v3[3];
      if h[3] = 0 then h[3] := f.x;
      if b[3] = 0 then b[3] := f.y;
      up;
      s[3].MoveTo(h[3], b[3]);
    end;
    if v4[3] <> 0 then
    begin
      mi[3] := true;
      full[3] := v4[3];
      if h[3] = 0 then h[3] := f.y;
      if b[3] = 0 then b[3] := f.x;
      up;
      s[3].MoveTo(b[3], h[3]);
    end;
  end;
end;

procedure destroy;
begin
  num := 1;
  begin
    boom;
    num += 1;
    boom2;
    num += 1;
    boom3;
  end;
  num := 1;
end;

procedure bo();
begin
  if u.x - 60 > i.x then i.x := i.x + i.speed; 
  if u.x + 120 < i.x then i.x := i.x - i.speed;
  if u.y - 60 > i.y then i.y := i.y + i.speed;
  if u.y + 120 < i.y then i.y := i.y - i.speed;
  object2.MoveTo(i.x, i.y);
end;

procedure bo2();
begin
  if u.x - 60 > q.x then q.x := q.x + q.speed; 
  if u.x + 120 < q.x then q.x := q.x - q.speed;
  if u.y - 60 > q.y then q.y := q.y + q.speed;
  if u.y + 120 < q.y then q.y := q.y - q.speed;
  object3.MoveTo(q.x, q.y);
end;

procedure bo3();
begin
  if u.x - 60 > f.x then f.x := f.x + f.speed; 
  if u.x + 120 < f.x then f.x := f.x - f.speed;
  if u.y - 60 > f.y then f.y := f.y + f.speed;
  if u.y + 120 < f.y then f.y := f.y - f.speed; 
  object4.MoveTo(f.x, f.y);
end;

//bot
procedure bot();
begin
  i := new pl;
  i.sprite := 'D:\Desktop\игры/angry/IMG-20170401-WA0001.png';
  i.hp := 100;
  i.x := 120;
  i.y := 600;
  i.damage := 10;
  i.speed := 1;
  i.hp := 100;
  object2 := PictureABC.Create(i.x, i.y, i.sprite); 
  pule := 'D:\Desktop\игры\angry/k.png';
end;

//bot2
procedure bot2();
begin
  q := new pt;  
  q.sprite := 'D:\Desktop\игры/angry/IMG-20170401-WA0001.png';
  q.hp := 100;
  q.x := 90;
  q.y := 100;
  q.damage := 10;
  q.speed := 1;
  object3 := PictureABC.Create(q.x, q.y, q.sprite); 
  pule2 := 'D:\Desktop\игры\angry/k.png';
end;

//bot3
procedure bot3();
begin
  f := new ok; 
  f.sprite := 'D:\Desktop\игры/angry/IMG-20170401-WA0001.png';
  f.hp := 100;
  f.x := 1000;
  f.y := 87;
  f.damage := 10;
  f.speed := 1;
  object4 := PictureABC.Create(f.x, f.y, f.sprite);
  pule3 := 'D:\Desktop\игры\angry/k.png';
end;

//aim
procedure fight;
begin
  if u.x + 160 > q.x then
    if u.x - 80 < q.x then  
      c := 0
    else c := 1
  else c := -1;
  
  if u.x + 160 > i.x then 
    if u.x - 80 < i.x then 
      z := 0
    else z := 1 
  else z := -1;
  
  if u.x + 160 > f.x then 
    if u.x - 80 < f.x then 
      v := 0
    else v := 1 
  else v := -1;
  
  if u.y + 160 > q.y then
    if u.y - 80 < q.y then
      c2 := 0
    else c2 := 1 
  else c2 := -1;
  
  if u.y + 160 > i.y then 
    if u.y - 80 < i.y then 
      z2 := 0
    else z2 := 1 
  else z2 := -1;
  
  if u.y + 160 > f.y then 
    if u.y - 80 < f.y then
      v2 := 0
    else v2 := 1 
  else v2 := -1;
  
end;

//attack
procedure attack(key: integer);
begin
  if key = VK_ShiftKey then
  begin
    if z = 0 then if z2 = 0 then i.hp -= u.damage;
    if c = 0 then if c2 = 0 then q.hp -= u.damage;
    if v = 0 then if v2 = 0 then f.hp -= u.damage;
  end;
end;

//move 
procedure move(key: integer);
  procedure d;
  var
    o: integer;
  begin
    if p = 1 then for o := 3 to 19 do begin if u.x < 1200 then begin u.x := u.x + u.speed;sleep(10);object1.MoveTo(u.x, u.y) end; end;
    if p = 2 then for o := 3 to 19 do begin if u.x > 0 then begin u.x := u.x - u.speed;sleep(10);object1.MoveTo(u.x, u.y) end; end; end;
  
  procedure w;
  var
    m: integer;
  begin
    if l = 1 then for m := 3 to 19 do begin if u.y < 601 then begin u.y := u.y + u.speed;sleep(10);object1.MoveTo(u.x, u.y) end; end;
    if l = 2 then for m := 3 to 19 do begin if u.y > 0 then begin u.y := u.y - u.speed;sleep(10);object1.MoveTo(u.x, u.y) end; end; end;

begin
  if u.x < 1200 then begin if key = VK_Right then begin p := 1;d; end; end;
  if u.y > 0 then begin if key = VK_Up then begin l := 2;w; end; end;
  if u.y < 601 then begin if key = VK_Down then begin l := 1;w; end; end;
  if u.x > 0 then begin if key = VK_Left then begin p := 2;d; end; end;
  object1.MoveTo(u.x, u.y);
end;

//player
procedure player();
begin
  u := new bt;
  u.sprite := 'D:\Desktop\игры/angry/FreshPaint-0-2017.04.02-05.13.59.png';
  u.x := 500;
  u.y := 500;
  u.damage := 100;
  u.speed := 5;
  u.hp := 100;
  object1 := PictureABC.Create(u.x, u.y, u.sprite);
  if u.hp = 0 then object1.Destroy;
  graphABC.OnKeyUp := attack;
  graphABC.OnKeyDown := move;
end;

//update
procedure j();
begin
  o;
  player;
  bot;
  bot2;
  bot3; 
  trish;
  num := 1;
  while u.hp > 1 do 
  begin
    fight; 
    if i.hp > 1 then bo;
    if q.hp > 1 then bo2; 
    if f.hp > 1 then bo3;   
    if i.hp < 1 then object2 := PictureABC.Create(i.x, i.y, 'D:\Desktop\игры\angry/FreshPaint-6-2017.04.02-04.00.41 — копия.png');
    if q.hp < 1 then object3 := PictureABC.Create(q.x, q.y, 'D:\Desktop\игры\angry/FreshPaint-6-2017.04.02-04.00.41 — копия.png');
    if f.hp < 1 then object4 := PictureABC.Create(f.x, f.y, 'D:\Desktop\игры\angry/FreshPaint-6-2017.04.02-04.00.41 — копия.png');
    if i.hp < 1 then bot;
    if q.hp < 1 then bot2;
    if f.hp < 1 then bot3;
    location;
    destroy;
    sleep(10); 
  end; 
end;

// ########################################################
begin
  j;
end.

{second[num] += 1;
  fi := num * 5;
if second[num] > fi then}