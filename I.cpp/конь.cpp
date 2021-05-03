#include <iostream>
#include <math.h>
using namespace std;
int a,b,c ,d;

int main(){
    cin >>a>>b>>c>>d;
    a=abs(a-c);
    b=abs(b-d);
    if ( ( a==1 and b==2 ) or ( a==2 and b==1 ) ) cout<<"YES";
    else cout<<"NO"; 
return 0;
    }
