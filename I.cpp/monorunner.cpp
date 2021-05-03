#include <iostream>
#include <string>
#include <fstream>
#include <windows.h>
#include <io.h>
#include <sys/stat.h>
using namespace std;

string l;
string h;
string f;
int i;



void mixtake(){


l="File "+l+" is not found";
MessageBox(NULL,l.c_str(),"",MB_OK |MB_DEFBUTTON1 | MB_ICONSTOP | MB_DEFAULT_DESKTOP_ONLY);

};
bool exists(string f)
			{
			  return access(f.c_str(), 0);
			};


int main(int a, char *k[])
{   setlocale(0,"");
    l=k[0];
    i=l.size();
    do{i-=1;}
    while (l[i]!='.');
    l=l.substr(0,i)+".ini";

    if (exists(l)==0){

    int size;
    ifstream  t(l.c_str());

    struct stat fi;
     stat(l.c_str(),&fi);


    do{i-=1;}
    while (l[i]!='\\');
    h=l.substr(0,i);

    i=fi.st_size-8;

           do {
                getline(t,l);
                getline(t,f);
                cout<<l<<endl<<f<<endl;
                cout<<f.size()+l.size()<<' '<<i;
                i=i-l.size()-f.size()-2;
                if (l[0]!='*'){
                        if (l[0]=='\\'){l=h+l;};
                ShellExecute(0,0,l.c_str(),f.c_str(),0,1);};
                cout<<" "<<i;
             } while (i>0);
    }


    else {
            mixtake();

    };


    return 0;
}

