#include <iostream>

int main() 
{
  float pt1,pt2,ep1,ep2=0;

  std::cout << "Informe a nota PT1: ";
  std::cin >> pt1;
  std::cout << "Informe a nota EP1: ";
  std::cin >> ep1;
  std::cout << "Informe a nota PT2: ";
  std::cin >> pt2;
  std::cout << "Informe a nota EP2: ";
  std::cin >> ep2;

  float av1=0.3*pt1+0.15*ep1,av2=0.4*pt2+0.15*ep2;
  std::cout << "A nota na AV1 é: "<<av1<<std::endl;
  std::cout << "A nota na AV2 é: "<<av2<<std::endl;

  float nota=av1+av2;
  std::cout << "A nota no semestra é: "<<nota<<std::endl;
}