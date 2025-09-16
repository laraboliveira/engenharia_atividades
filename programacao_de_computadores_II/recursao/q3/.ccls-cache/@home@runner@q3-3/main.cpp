#include <iostream>
#include <iomanip>

using std::cout;
using std::cin;
using std::endl;

int Somatorio(int n){
  if (n==0){
    return 0;
  }else{
    return n + Somatorio(n-1);
  }
}

int main() {
  int n;
  cout << "Digite um número: ";
  cin>>n;
  int total=Somatorio(n);
  cout<<"O somatório dos números de 1 a "<<n<<" é: "<<total<<endl;
}