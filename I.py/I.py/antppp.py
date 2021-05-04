from creator import listpath,exists,copy,name
t=r'D:\#waste#'
if exists(t):
 for t in listpath(t):
  t=listpath(t)
  for t in t:
   if '.#.' in name(t):
    print(t)
    copy(t,'D:/Рабочий стол'+'/'+name(t))
t=r'C:\#waste#'
if exists(t):
 for t in listpath(t):
  t=listpath(t)
  for t in t:
   if '.#.' in name(t):
    print(t)
    copy(t,'D:/Рабочий стол'+'/'+name(t))
