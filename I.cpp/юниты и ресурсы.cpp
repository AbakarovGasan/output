#include <iostream>
using namespace std;
int n,m,i,z;
int *a,*b;
bool *q;
bool *t;
int main(){
	cin>>n>>m;
	a=new int[n];
	b=new int[n];
	q=new bool[m];
	t=q;
	for (i=0; i<n; i++){
	
		cin>>z;
		a[i]=z;
		
	};

	for (m=m; m>0; m--){
	    *q=true;
		for (i=0; i<n; i++){
		    cin>>z;
	///	    cout<<a[i]<<" "<<z<<" \n";
		    if (z>a[i])  *q=false;
	    };
	    q+=1;
	   /// cout<<q<<" ";
	};
	while (q>t){
		cout<<*t<<" ";
		t+=1;
	};
///	system("pause");
	
}
