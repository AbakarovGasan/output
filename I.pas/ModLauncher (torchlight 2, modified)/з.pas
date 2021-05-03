uses System, system.IOж

const
  path = environment.GetFolderPath(environment.SpecialFolder.MyDocuments) + '\My Games\Runic Games\Torchlight 2';

var
  MODS: Directoryinfo = new directoryinfo(path + '\mods');
  a, b, c, d, e, f: integer;
  modfile: file of byte;
  nt, knt: string;
  aa, bb, cc, dd, ee, ff: string;
  ai, bi, ci, di, ei, fi: byte;
  aw, bw, cw, dw, ew, fw: word;
  awi: array of word;
  txt: pabcsystem.Text;
  z: array of fileinfo;
  an, bn, cn, dn, en, fn: char;
  bni: int64;
  dialog: system.Windows.Forms.FileDialog = new system.Windows.Forms.SaveFileDialog;
  _name: array of string;
  _author: array of string;
  _description: array of string;
  _website: array of string;
  _downloadlink: array of string;
  _filename: array of string;
  _modguid: array of int64;
  _suitablefor: array of array of word;
  _version: array of word;
  nitro, turbo, cheap: boolean;
  kit: collections.generic.list<int64> = new collections.generic.list<int64>;
  original: collections.generic.list<int64> = new collections.generic.list<int64>;
  kkit: collections.generic.list<integer> = new collections.generic.list<integer>;


procedure form1.infoload(H: integer);
begin
  filename.text := _filename[h];
  author.Text := _author[h];
  version.Text := inttostr(_version[h]);
  description.text := _description[h];
  download.Text := _downloadlink[h];
  website.Text := _website[h];
  status.Text := 'suitable for TL2 v.' + inttostr(_suitablefor[h][0]) + '.' + inttostr(_suitablefor[h][1]) + '.' + inttostr(_suitablefor[h][2]) + '.' + inttostr(_suitablefor[h][3]);
end;

procedure setlength(h: integer);
begin
  setlength(_name, h);
  setlength(_version, h);
  setlength(_suitablefor, h);
  setlength(_author, h);
  setlength(_description, h);
  setlength(_website, h);
  setlength(_downloadlink, h);
  setlength(_modguid, h);
  setlength(_filename, h);
end;

procedure setattr(point: integer; version: byte; suitablefor: array of word; filename: string; name: string; author: string; description: string; website: string; downloadlink: string; modguid: int64);
begin
  _suitablefor[point] := suitablefor;
  _version[point] := version;
  _name[point] := name;
  _filename[point] := filename;
  _author[point] := author;
  _website[point] := website;
  _downloadlink[point] := downloadlink;
  _modguid[point] := modguid;
  _description[point] := description;
end;

function readbytes(H: integer): array of byte;
var
  f: array of byte;
begin
  setlength(f, h);
  for var i := 0 to h - 1 do 
  begin
    f[i] := modfile.Read();
  end;
  readbytes := f;
end;

function read1(): byte;
begin
  read1 := modfile.Read()
end;

function read2(): word;
begin
  read2 := modfile.Read + modfile.read * 256;
end;

function read3(): INTEGER;
begin
  read3 := bitconverter.ToInt32(readbytes(4), 0);
end;

function read4(): INT64;
begin
  read4 := bitconverter.ToInt64(readbytes(8), 0);
end;

function readwords(h: word): array of word;
var
  f: array of word;
begin
  setlength(f, h);
  for var i := 0 to h - 1 do 
  begin
    f[i] := read2;
  end;
  readwords := f;
end;

function readtext(h: word): string;
begin
  while h > 0 do 
  begin
    readtext += chr(read2);
    h -= 1;
  end;
end;

function step(t: word): int64;
begin
  step := 1;
  while t > 0 do 
  begin
    t -= 1;
    step *= 256;
  end;
end;

procedure form1.add(h: integer);
begin
  if kkit.IndexOf(h) = -1 then
  begin
    kkit.Add(h);
    listbox2.items.add(listbox1.items.item[h]);
  end;
end;

procedure form1.clear();
begin
  listbox2.items.clear();
  kkit.Clear();
end;

procedure form1.removeat(h: integer);
begin
  kkit.RemoveAt(h);
  listbox2.items.removeat(h);
end;

procedure form1.remove(H: integer);
var
  j: integer = kkit.IndexOf(h);
begin
  if j <> -1 then removeat(j);
end;

procedure form1.replace(h: integer; K: integer);
var
  nit: integer;
  tin: string;
begin
  nit := kkit[k];
  kkit[k] := kkit[h];
  kkit[h] := nit;
  tin := listbox2.items.item[k].tostring;
  listbox2.items.item[k] := listbox2.items.item[h];
  listbox2.items.item[h] := tin;
end;

procedure stackload();
begin
  kit.Clear;
  a := 0;
  b := kkit.Count;
  while a < b do
  begin
    kit.Add(_modguid[kkit[a]]);
    a += 1;
  end;
end;



procedure form1.get1;
begin
  clear();
  a := 0;
  b := kit.Count;
  while a < b do
  begin
    c := _modguid.IndexOf(kit[a]);
    if c <> -1 then listbox1.setitemchecked(c, true);
    a += 1;
  end;
end;


procedure form1.load1;
label 1;
begin
  z := mods.GetFiles;
  a := -1;
  c := 0;
  b := z.Length;
  setlength(b);
  b -= 1;
  while a < b do 
  begin
    writeln();
    a += 1;
    aa := z[a].name;
    if aa.substring(aa.length - 4, 4) <> '.mod' then continue;
    try
      reset(modfile, z[a].fullname);
    except
      continue;
    end;
    
    if modfile.FileSize < 20 then goto 1;
    if read2 <> 4 then goto 1;
    aw := read2;
    awi := readwords(4);
    modfile.seek(12);
    f := read3() - 24;
    d := read3();
    if modfile.FileSize < d then goto 1;
    modfile.Seek(d);
    if read1 <> 2 then goto 1;
    modfile.Seek(f);
    bni := read4();
    if _modguid.IndexOf(bni) <> -1 then goto 1;
    modfile.Seek(20);
    setattr(c, aw, awi, aa, readtext(read2), readtext(read2), readtext(read2), readtext(read2), readtext(read2), bni);
    listbox1.Items.Add(_name[c]);
    c += 1;
    /// end;
    1: modfile.Close()
  end;
end;

procedure reading();
label 1, 2, 3;
begin
  try
    reset(txt, nt, encoding.Unicode);
    1: repeat
      an := txt.readchar();
    until an = '[';
    repeat
      aa += an;
      an := txt.readchar.toupper;
    until an = ']';
    aa += an;
    if aa <> '[MODS]' then goto 1;
    2: repeat
      an := txt.readchar;
      if an = '[' then goto 3;
    until an = '<';
    repeat
      aa := txt.readchar.tolower;
      aa += an
    until an = '>';
    case aa of
      '<integer64>': ai := 0;
      '<integer32>': ai := 4;
      '<integer16>': ai := 2;
      '<integer8>': ai := 1;
    else goto 2;
    end;
    aa := '';
    repeat
      an := txt.readchar.tolower;
      aa += an;
    until an = ':';
    if aa <> 'modguid:' then goto 2;
    an := txt.ReadChar;
    aa := '';
    while aa <> newline do 
    begin
      aa += an;
      an := txt.ReadChar;
    end;
    try
      bni := strtoint(aa);
    except
      bni := 0
    end;
    if bni = 0 then goto 2
    else if bni < 0 then bni += step(ai);
    kit.add(bni);
    goto 2;
    3: aa := an;
    repeat
      an := txt.ReadChar.ToUpper;
      aa += an;
    until an = ']';
    if aa <> '[/mods]' then goto 2;
  except
    txt.close()
  end;
end;


procedure form1.finish;
begin
  stackload;
  rewrite(txt, nt, encoding.Unicode);
  txt.Writeln('[MODS]');
  a := kit.Count;
  while a > 0 do 
  begin
    txt.Writeln('    <INTEGER64>MODGUID:', inttostr(kit[a]));
    a -= 1;
  end;
  txt.Writeln('[/MODS]');
  txt.Close();
end;

procedure Form1.Form1_Load(sender: Object; e: EventArgs);
begin
  load1;
  reading;
  original := kit;
  get1;
end;