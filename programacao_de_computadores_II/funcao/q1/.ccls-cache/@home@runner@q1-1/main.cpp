#include <iostream>
#include <iomanip>

float calculo(float mat, float m, float ener){
  float total;
  total = mat+m+ener;
  return total;
}

int main() {
  float ener, m, mat=0;
  std::cout << "Digite o custo da matéria−prima: ";
  std::cin>>mat;
  std::cout << "Digite o custo da mão de obra: ";
  std::cin>>m;
  std::cout << "Digite o custo da energia elétrica: ";
  std::cin>>ener;
  float total=calculo(mat,m,ener);
  std::cout <<std::fixed<<std::setprecision(2)<< "Custo total: "<<total<<std::endl;
  if (total>1000){
    float val=0;
    val=total-(total-1000)*0.1;
    std::cout <<std::fixed<<std::setprecision(2)<< "Valor excedente: "<<total-1000<<std::endl;
    std::cout <<std::fixed<<std::setprecision(2)<< "Valor com desconto: "<<val<<std::endl;
  }
}