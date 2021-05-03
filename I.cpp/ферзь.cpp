#include <iostream>
#include <math.h>
using namespace std;
int a,b,c ,d;

int main(){
    cin >>a>>b>>c>>d;
    if (a==c) cout<<"YES";
    else if (b==d) cout<<"YES";
    else if (abs(a-c)==abs(b-d)) cout<<"YES";
    else cout<<"NO";
return 0;
    }
