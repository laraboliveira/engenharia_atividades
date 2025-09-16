#include <iostream>
#include <iomanip>

using std::cout;
using std::cin;
using std::endl;

int potencia(int base, int exp){
  if (exp==1){
    return base;
  }else{
    return base*potencia(base,exp-1);
  }
}

int main() {
  int base,exp;
  cout << "Digite a base: ";
  cin >> base;
  cout << "Digite o expoente: ";
  cin >> exp;
  if (exp<0){
    cout << "ERRO: valor de expoente inválido";
  }else{
    int total=potencia(base,exp);
    cout<<base<<" elevado a "<<exp<<" é igual a: "<<total<<endl;
  }
  
}