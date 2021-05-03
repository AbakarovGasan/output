uses Unit1;

label 1;
var
  i: form1;
  j: string;
  beginj, endh, bib: string;

begin
  dialog.initialdirectory := path;
  b:=path.Length;
  a:=3;
  while a<b do 
  begin
  
  a+=1;

  if path[a]='\' then begin 
  mkdir(path.Substring(0,a));

  end;
  mkdir(path);
  end;
  nt := 'modlauncher.sch';
  knt := 'Torchlight2.exe';
  nitro := false;
  try
    reset(txt, 'modlauncher.ini');
  except
    try
      rewrite(txt, 'modlauncher.ini');
      txt.Write('#gamepath and modschemepath must be writed here ');
      txt.Close;
    
    except
    end;
    nitro := true;
  end;
  if nitro then goto 1;
  j := txt.ReadlnString;
  
  while j.length <> 0 do 
   begin
    if j[1] <> '#' then break;
    beginj += j+newline;
    j := txt.ReadlnString;
   end;
   
  
  if j.Length <> 0 then 
  begin
    knt := j;
    j := txt.ReadlnString;
    while j.length <> 0 do 
    begin
      if j[1] <> '#' then break;
      endh += j+newline;
      j := txt.ReadlnString;
    end;
    if j.Length <> 0 then nt := j
    
  end;
  bib := txt.ReadToEnd();
  
  txt.Close;
  1:
  if not pabcsystem.FileExists(path) then crfolder(path);

  NT:=PATH+'\'+NT;
  try
    reset(txt, nt)
  
  except
    rewrite(txt, nt);
  end;
  txt.Close;
  turbo := true;

  
  
  System.Windows.Forms.Application.EnableVisualStyles();
  System.Windows.Forms.Application.SetCompatibleTextRenderingDefault(false);
  i := new form1;
  System.Windows.Forms.Application.Run(i);
  try
  rewrite(txt, 'modlauncher.ini',pabcsystem.Encoding.Unicode);
  nt:=nt.Substring(path.Length+1,nt.length-path.length-1);
  if run then execute(knt,'MODSCHEME='+nt);
  txt.Write(beginj,knt,newline,endh,nt,newline,bib);
  txt.Close;
  except
  end;
end.