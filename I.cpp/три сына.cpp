#include <iostream>
#include <cmath>
using namespace std;
int main(){
	long long n;
	cin>>n;
	char q=n%3;
	n=n/3;
	
	if (q==0)         cout<<n-1<<" "<<n<<" "<<n+1;
	else if (q==1)        cout<<n-1<<" "<<n<<" "<<n+2;
	else  cout<<n-1<<" "<<n+1<<" "<<n+2;
}
