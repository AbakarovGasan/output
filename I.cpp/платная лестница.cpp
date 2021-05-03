#include <iostream>
using namespace std;

int n,i,l ;
int *u;

int end(int s){
    if (i==3) {
        if (u[2]>u[1]) return u[2]+u[3];
        else           return u[1]+u[3];
        }
    else return u[s];
}

int f(int s){
    if (s<=3)  return end(s);
    else {
            l=f(s-1);
            i=f(s-2);
            if (l<i) return l+u[s];
            else return l+u[s];
}
    }

int main(){

cin>>n;

u=new int[n+1];

for (i=1;i<=n;i++){

cin>>l;
u[i]=l;


    }

cout<<f(n);
system("pause");
}
