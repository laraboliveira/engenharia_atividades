#include <iostream>
#include <iomanip>

bool temDireitoValeTransporte(float salb){
  if (salb>1500){
    return true;
  }
  return false;
}
float calcularSalarioLiquido(float salb, float numDep,float &sall){
  sall=salb-(salb*0.1)-(salb*0.05)-(numDep*50);
  bool resp=temDireitoValeTransporte(salb);
  if (resp==true){
    sall=sall-100;
    return sall;
  }
  return sall;
}

int main() {
  float salb,numDep,sall=0;
  std::cout << "Digite o salário bruto: ";
  std::cin>>salb;
  std::cout << "Digite o número de dependentes: ";
  std::cin>>numDep;
  float sal=calcularSalarioLiquido(salb,numDep,sall);
  std::cout <<std::fixed<<std::setprecision(2)<< "O salário líquido é: R$"<<sall<<std::endl;
}