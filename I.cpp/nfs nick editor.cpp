#include <fstream>
#include <iostream>
#include <string>
#include <windows.h>

using namespace std;
string d;
int k;
int x=53797;



char * buffer = new char [8];
ifstream  t("(0_0)", ifstream::binary  );
ofstream  m("",ofstream::binary );
char text;

void i ()
{ do
 { text=t.get(); m<<text; k+=1;} 
while (k!=x);
};

   


int main(){
	
cin >> buffer;

buffer[7]=0;

d+=buffer; d+='\\'; d+=buffer;
cout<<d;



CreateDirectory(buffer, NULL);

m.open(d.c_str(), ofstream::binary);

//53797
//54966
//53804

i();
 m.write(buffer,7);
 t.seekg(53804);
x=54966;
k=53804;
i();


 
 
 
 m.close();
 t.close();
return 0;

}
