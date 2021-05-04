#include <windows.h>
#include <iostream>
#include <tchar.h>
#include <stdio.h>

using namespace std;
HKEY key;
 
WIN32_FIND_DATA find;
HANDLE root;

const char *ptr = new char[256];
unsigned char *buf= ptr;
DWORD path=sizeof (buf);

int desk (){
RegOpenKeyEx(HKEY_CURRENT_USER,"Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders", 0, KEY_QUERY_VALUE, &key );
RegQueryValueEx(key, "Desktop",0,0,buf, &path);
RegCloseKey(key);

return 0;
}

int main()
{
   WIN32_FIND_DATA FindFileData;
   HANDLE hFind;
   hFind = FindFirstFile(, &FindFileData);
   
   
   if (hFind == INVALID_HANDLE_VALUE) 
   {
      printf ("FindFirstFile failed (%d)\n", GetLastError());
     
   } 
   else 
   {
      _tprintf (TEXT("The first file found is %s\n"), 
                FindFileData.cFileName);
      FindClose(hFind);
   };
   return 0;
}
