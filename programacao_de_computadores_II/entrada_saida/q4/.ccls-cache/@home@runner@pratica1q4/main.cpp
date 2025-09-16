#include <iostream>
#include <cmath>
#include <iomanip>

using std::cout;
using std::cin;

int main() {
  float p,a,q=0;
  std::cout << "Digite seu peso (em kg): ";
  std::cin>>p;
  std::cout << "Digite sua altura (em metros): ";
  std::cin>>a;
  std::cout << "Digite a circunferência do seu quadril (em cm): ";
  std::cin>>q;

  float imc=p/pow(a,2), iac=(q/pow(a,1.5))-18;
  std::cout << std::fixed<<"IMC: "<<std::setprecision(3)<<imc<<"\nIAC= "<<std::setprecision(3)<<iac<<std::endl;
}