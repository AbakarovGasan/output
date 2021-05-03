unit Unit1;

interface

uses System, system.IO, System.Drawing, System.Windows.Forms;

const
  path = environment.GetFolderPath(environment.SpecialFolder.MyDocuments) + '\My Games\Runic Games\Torchlight 2';
  unicodenewline = chr(13);
  tab = chr(9);

function read2(): word;
function read3: integer;
function read4: int64;
function read1: byte;
procedure crfolder(path: string);

var
  MODS: Directoryinfo = new directoryinfo(path + '\mods');
  a, b, c, d, e, f: integer;
  af: int64;
  modfile: file of byte;
  nt, knt, endl: string;
  aa, bb, cc, dd, ee, ff: string;
  ai, bi, ci, di, ei, fi: byte;
  aw, bw, cw, dw, ew, fw: word;
  awi: array of word;
  txt: pabcsystem.Text;
  z: array of fileinfo;
  an, bn, cn, dn, en, fn: char;
  bni: int64;
  dialog: system.Windows.Forms.openFileDialog = new system.Windows.Forms.openFileDialog;
  _name: array of string;
  _author: array of string;
  _description: array of string;
  _website: array of string;
  _downloadlink: array of string;
  _filename: array of string;
  _modguid: array of int64;
  _suitablefor: array of array of word;
  _version: array of word;
  nitro, turbo, run, cheap: boolean;
  
  kit: system.collections.generic.list<int64> = new system.collections.generic.list<int64>;
  original: system.collections.generic.list<int64> = new system.collections.generic.list<int64>;
  kkit: system.collections.generic.list<integer> = new system.collections.generic.list<integer>;
  time: pabcsystem.datetime = pabcsystem.datetime.Now;
  interval: system.TimeSpan;

type
  Form1 = class(Form)
    procedure infoload(H: integer);
    procedure add(H: integer);
    procedure clear;
    procedure finish;
    procedure infoclear;
    procedure removeat(H: integer);
    procedure remove(H: integer);
    procedure load1;
    procedure get1;
    procedure setall(H: boolean);
    procedure replace(H: integer; k: integer);
    procedure Form1_Load(sender: Object; e: EventArgs);
    procedure ListBox1_ItemCheck(sender: Object; e: ItemCheckEventArgs);
    procedure button1_Click(sender: Object; e: EventArgs);
    procedure ListBox1_SelectedIndexChanged(sender: Object; e: EventArgs);
    procedure button2_Click(sender: Object; e: EventArgs);
    procedure button4_Click(sender: Object; e: EventArgs);
    procedure button3_Click(sender: Object; e: EventArgs);
    procedure button11_Click(sender: Object; e: EventArgs);
    procedure website_DoubleClick(sender: Object; e: EventArgs);
    procedure download_DoubleClick(sender: Object; e: EventArgs);
    procedure listbox2_focus_KeyDown(sender: Object; e: KeyEventArgs);
    procedure listBox2_MouseClick(sender: Object; e: MouseEventArgs);
    procedure listBox2_Enter(sender: Object; e: EventArgs);
    procedure listBox2_KeyDown(sender: Object; e: KeyEventArgs);
    procedure listbox2_focus_Enter(sender: Object; e: EventArgs);
    procedure listBox2_SelectedIndexChanged(sender: Object; e: EventArgs);
    procedure listbox2_focus_Leave(sender: Object; e: EventArgs);
    procedure ListBox1_Leave(sender: Object; e: EventArgs);
    procedure ListBox1_Enter(sender: Object; e: EventArgs);
    procedure button7_Click(sender: Object; e: EventArgs);
    procedure button12_Click(sender: Object; e: EventArgs);
    procedure button8_Click(sender: Object; e: EventArgs);
    procedure button6_Click(sender: Object; e: EventArgs);
    procedure button5_Click(sender: Object; e: EventArgs);
  {$region FormDesigner}
  private
    {$resource Unit1.Form1.resources}
    label7: &Label;
    listBox2: ListBox;
    linkLabel1: LinkLabel;
    button4: Button;
    groupBox1: GroupBox;
    label9: &Label;
    download: TextBox;
    label8: &Label;
    website: TextBox;
    label6: &Label;
    description: RichTextBox;
    status: TextBox;
    filename: TextBox;
    version: TextBox;
    author: TextBox;
    label5: &Label;
    label4: &Label;
    label3: &Label;
    label2: &Label;
    label1: &Label;
    button2: Button;
    ListBox1: CheckedListBox;
    button1: Button;
    button9: Button;
    button10: Button;
    button11: Button;
    button5: Button;
    button6: Button;
    button7: Button;
    button8: Button;
    button12: Button;
    listbox2_focus: TextBox;
    button3: Button;
    {$include Unit1.Form1.inc}
  {$endregion FormDesigner}
  public 
    constructor;
    begin
      InitializeComponent;
    end;
  end;

implementation

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

procedure form1.infoclear();
begin
  filename.text := '';
  author.text := '';
  version.text := '';
  description.text := '';
  download.text := '';
  website.text := '';
  status.text := '';
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
  K := H + K;
  if h <> k then if h > -1 then if k > -1 then if h < listbox2.items.count then if k < listbox2.items.count then 
          begin
            nit := kkit[k];
            kkit[k] := kkit[h];
            kkit[h] := nit;
            tin := listbox2.items.item[k].tostring;
            listbox2.items.item[k] := listbox2.items.item[h];
            listbox2.items.item[h] := tin;
            listbox2.setselected(h, false);
            listbox2.setselected(k, true);
          end;
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

procedure rename(h: string);
var j:string=modfile.name;
b:integer;
begin
  modfile.Close();
  h:=path+h;
  if not fileexists(h) then mkdir(h);
  while fileexists(h+j) do
  begin
  b+=1;
  j:='('+inttostr(b)+') '+j;
  end;
  try
    rename(modfile, h + j);
  except
  end;
end;

procedure form1.get1;
begin
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
begin
  listbox1.items.clear;
  setlength(0);
  mods := new directoryinfo(path + '\mods');
  if not mods.Exists then mkdir(mods.FullName);
  z := mods.GetFiles;
  a := -1;
  c := 0;
  
  b := z.Length;
  setlength(b);
  b -= 1;
  while a < b do 
  begin
    a += 1;
    aa := z[a].name;
    if aa.substring(aa.length - 4, 4).toupper <> '.MOD' then continue;
    ///    try
    reset(modfile, z[a].fullname);
    ///    except
    ///      continue;
    ///    end;
    
    if modfile.FileSize < 20 then begin rename('\crashedmods\'); continue; end;
    if read2 <> 4 then begin rename('\crashedmods\'); continue; end;
    aw := read2;
    awi := readwords(4);
    modfile.seek(12);
    f := read3() - 24;
    d := read3();
    if modfile.FileSize < d then  begin rename('\crashedmods\'); continue; end;
    modfile.Seek(d);
    if read1 <> 2 then  begin rename('\crashedmods\'); continue; end;
    modfile.Seek(f);
    bni := read4();
    if _modguid.IndexOf(bni) <> -1 then begin rename('\mods_2\');  continue; end;
    modfile.Seek(20);
    setattr(c, aw, awi, aa, readtext(read2), readtext(read2), readtext(read2), readtext(read2), readtext(read2), bni);
    listbox1.Items.Add(_name[c]);
    c += 1;
    /// end;
    modfile.Close();
  end;
  setlength(c);
  
end;

procedure crfolder(path: string);
var
  j: string;
begin
  
  a := 3;
  j := path.Substring(0, 3);
  while a < path.Length do
  begin
    a += 1;
    if path[a] = '\' then  if not pabcsystem.FileExists(j) then pabcsystem.mkdir(j);
    j += path[a];
  end;
  
end;

procedure reading();
label 1, 2, 3, const1, end1, cl;
begin
  try
    reset(txt, nt, encoding.Unicode);
    aa := '';
    1: repeat
      an := txt.readchar();
    until an = '[';
    
    repeat
      aa += an;     
      ///     writeln(an);
      ///     sleep(200);
      an := txt.readchar.toupper;
    until an = ']';
    ///     writeln(an);
    ///     sleep(200);
    aa += an;
    if aa <> '[MODS]' then goto 1;
    2: repeat
      ///     writeln(an);
      ///     sleep(200);
      an := txt.readchar;
      if an = '[' then
      begin
        goto 3;
      end;
    until an = '<';
    aa := an;
    repeat
      ///     writeln(an);
      ///     sleep(200);
      an := txt.readchar.tolower;
      aa += an
    until an = '>';
    ///   writeln('aa:',aa);
    case aa of
      '<integer64>': af := 0;
      '<integer32>': af := pabcsystem.MaxLongWord;
      '<integer16>': af := pabcsystem.MaxWord;
      '<integer8>': af := 256;
    else goto 2;
    
    end;
    aa := '';
    repeat
      ///     writeln(an);
      ///     sleep(200);
      an := txt.readchar.tolower;
      aa += an;
    until an = ':';
    if aa <> 'modguid:' then goto 2;
    ///   writeln('aa:',aa);
    an := txt.ReadChar;
    aa := '';
    ///   writeln('begin_number_reading');
    while an <> unicodenewline do 
    begin
      ///     writeln(an);
      ///     sleep(200);
      aa += an;
      an := txt.ReadChar;
    end;
    ///   writeln('end_number_reading');
    ///   writeln('num:',aa,':num');
    ///   sleep(200);
    try
      bni := strtoint64(aa);
    except
      bni := 0
    end;
    ///  writeln(aa);
    ///  sleep(3000);
    if bni = 0 then goto 2
    else if bni < 0 then bni += af;
    ///  writeln(bni);
    ///  sleep(3000);
    kit.add(bni);
    goto 2;
    3: aa := an;
    repeat
      an := txt.ReadChar.ToUpper;
      aa += an;
    until an = ']';
    if aa <> '[/MODS]' then    goto 2;
    txt.Close();
  except
    txt.close()
  end;
end;


procedure form1.finish;
begin
  rewrite(txt, nt, encoding.Unicode);
  txt.Writeln('[MODS]');  
  a := kit.Count; b := 0;
  while b < a do 
  begin
    txt.Writeln(tab + '<INTEGER64>MODGUID:', inttostr(kit[b]));
    b += 1;
  end;
  txt.Writeln('[/MODS]');
  txt.Close();
end;

procedure form1.setall(H: boolean);
begin
  clear();
  a := listbox1.items.count;
  b := 0;
  while b < a do 
  begin
    listbox1.setitemchecked(b, h);
    b += 1;
  end;
end;

procedure getdefault;
begin
  kit.clear;
  for var i := 0 to original.Count - 1 do 
  begin
    kit.Add(original[i]);
  end;
end;

procedure setdefault;
begin
  original.clear;
  for var i := 0 to kit.Count - 1 do 
  begin
    original.Add(kit[i]);
  end;
end;

procedure Form1.Form1_Load(sender: Object; e: EventArgs);
begin
  load1;
  reading;
  setdefault;
  get1;
end;

procedure Form1.ListBox1_ItemCheck(sender: Object; e: ItemCheckEventArgs);
begin
  if e.NewValue = checkstate.Checked then
  begin
  add(e.Index);
  listbox2.selecteditems.clear();
  listbox2.setselected(listbox2.items.count-1,true);
  end
  else if e.NewValue = checkstate.unChecked then remove(e.index);
  text := 'ModLauncher ' + inttostr(listbox2.Items.Count) + ' mod selected';
end;

procedure Form1.button1_Click(sender: Object; e: EventArgs);
begin
  if dialog.ShowDialog() <> system.Windows.Forms.DialogResult.cancel then 
  begin
    nt := dialog.FileName;
    kit.Clear();
    reading;
    setdefault;
  end;
end;

procedure Form1.ListBox1_SelectedIndexChanged(sender: Object; e: EventArgs);
begin
  a := listbox1.SelectedIndex;
  if a <> -1 then infoload(a);
end;

procedure Form1.button2_Click(sender: Object; e: EventArgs);
begin
  stackload;
  finish;
  setdefault;
end;

procedure Form1.button4_Click(sender: Object; e: EventArgs);
const
  jkit = 3000000;
begin
  interval := pabcsystem.DateTime.Now - time;
  if interval.Ticks < jkit then setall(true)
  else setall(false);
  time := pabcsystem.DateTime.Now;
end;

procedure Form1.button3_Click(sender: Object; e: EventArgs);
begin
  load1;
  setall(false);
  getdefault;
  get1;
end;

procedure Form1.button11_Click(sender: Object; e: EventArgs);
begin
  if dialog.ShowDialog() <> system.Windows.Forms.DialogResult.cancel then 
  begin
    ff := nt;
    nt := dialog.FileName;
    stackload;
    reading;
    get1;
    nt := ff;
  end;
end;

procedure Form1.website_DoubleClick(sender: Object; e: EventArgs);
begin
  try
    system.Diagnostics.process.start(website.text);
  except
  end;
end;

procedure Form1.download_DoubleClick(sender: Object; e: EventArgs);
begin
  try
    system.Diagnostics.process.start(download.text);
  except
  end;
end;

procedure Form1.listbox2_focus_KeyDown(sender: Object; e: KeyEventArgs);
begin
  case e.keyvalue of 
    38: replace(listbox2.selectedindex,  -1);
    40: replace(listbox2.selectedindex,  1);
    32: begin SendKeys.Send('{TAB}');SendKeys.Send('{TAB}');    end;
    46: begin listbox1.setitemchecked(kkit[listbox2.selectedindex], false); SendKeys.Send('{TAB}');SendKeys.Send('{TAB}'); end;
  
  end;
end;

procedure Form1.listBox2_MouseClick(sender: Object; e: MouseEventArgs);
begin
  listbox2_focus.focus();
end;

procedure Form1.listBox2_Enter(sender: Object; e: EventArgs);
begin
  listbox2.selecteditems.clear();
  infoclear;
  
end;

procedure Form1.listBox2_KeyDown(sender: Object; e: KeyEventArgs);
begin
  case e.keyvalue of
    32: turbo := true;
  end;
end;

procedure Form1.listbox2_focus_Enter(sender: Object; e: EventArgs);
begin
  a := listbox2.selectedindex;
  if a <> -1 then infoload(kkit[a])
  else listbox2.focus();
end;

procedure Form1.listBox2_SelectedIndexChanged(sender: Object; e: EventArgs);
begin
  if turbo then 
  begin
    listbox2_focus.focus();
    turbo := false;
  end;
end;

procedure Form1.listbox2_focus_Leave(sender: Object; e: EventArgs);
begin
  
  
end;

procedure Form1.ListBox1_Leave(sender: Object; e: EventArgs);
begin
  listbox1.selecteditems.clear();
  infoclear;
end;

procedure Form1.ListBox1_Enter(sender: Object; e: EventArgs);
begin
  listbox2.selecteditems.clear();
  infoclear();
end;

procedure Form1.button7_Click(sender: Object; e: EventArgs);
begin
  replace(listbox2.selectedindex,  1);
end;

procedure Form1.button12_Click(sender: Object; e: EventArgs);
begin
  replace(listbox2.selectedindex,  -1);
end;

procedure Form1.button8_Click(sender: Object; e: EventArgs);
begin
  listbox2.selecteditems.clear();
end;

procedure Form1.button6_Click(sender: Object; e: EventArgs);
begin
  a := listbox2.selectedindex;
  if a > -1 then if  a < listbox2.items.count then listbox1.setitemchecked(kkit[listbox2.selectedindex], false );
end;

procedure Form1.button5_Click(sender: Object; e: EventArgs);
begin
  stackload;
  finish;
  run := true;
  system.Windows.forms.application.exit();
end;





end.
