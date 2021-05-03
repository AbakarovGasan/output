
#include <string>
#include <windows.h>
using std::string;

string l;
char i;



int main(int a, char *k[])
{   setlocale(0,"");
    l=k[0];
    i=l.size();


    do{i-=1;}
    while (l[i]!='\\');
    l=l.substr(0,i)+"\\Chrome\\Application\\chrome.exe";
    
                ShellExecute(0,0,l.c_str(),"",0,1);
    




    return 0;
}

