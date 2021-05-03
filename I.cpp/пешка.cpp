#include <iostream>
using namespace std;
int a,b,c ,d;

int main(){
    cin >>a>>b>>c>>d;
    d-=b;
    
    if (d==2 and b==2) d--;
    
    if (a==c and d==1)cout<<"YES";
    else cout<<"NO"; 
return 0;
    }
