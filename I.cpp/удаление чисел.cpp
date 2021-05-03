#include <iostream>
using namespace std;
long long n,a;

void q(){	
	n=n/2;
	a=a/2;
	cout<<"1 ";
};

void w(){
	n++;
	n=n/2;
	a++;
	a=a/2;
	cout<<"0 ";
}

int main(){
	cin>>n>>a;
	while (n!=1){	
		if ((a%2)==1) w();
		else q(); 
	};	
//	system("pause");
	return 0;
}
