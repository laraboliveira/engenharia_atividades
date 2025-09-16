#include <iostream>

int mdc(int a, int b){
  if (b==0){
    return a;
  }
  return mdc(b,a%b);
}

using namespace std;

int main() {
  int a,b;
  cout << "Digite o primeiro numero: ";
  cin >> a;
  cout << "Digite o segundo numero: ";
  cin >> b;
  int m=mdc(a,b);
  cout<<"MDC("<<a<<","<<b<<") =  "<<m<<endl;
}