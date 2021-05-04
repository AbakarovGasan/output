#include <iostream>
using namespace std;
int main(){
	int n, k, q, m, d, l, i ;
	cin>>n;
	l=0;
	int *a = new int[n];
	
	cin>>q;
	k=q;
	 
	 q=q>>1;
	 
	i=1;
	while (i<n){
	   cin>>d;
	   m+=d;
	   if (d<=q) {
	   	k+=d;
	   	a[l]= i;
	   	l+=1;
	   };
	i+=1;
};
if ( (k<<1) >= m  ){
    cout<<l<<endl;
    
    while (l>0){
       l-=1;
	   cout<<a[l];	
	};
 	
};
	
}
