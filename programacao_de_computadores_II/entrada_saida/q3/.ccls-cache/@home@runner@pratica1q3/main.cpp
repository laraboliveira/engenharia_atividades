#include <iostream>
#include <cmath>
#include <iomanip>

using std::cout;
using std::cin;

int main() 
{
  float l,p,m = 0;
  std::cout << "Forneça o comprimento do fio: ";
  std::cin>> l;
  std::cout << "Forneça a força peso: ";
  std::cin>> p;
  std::cout << "Forneça a massa: ";
  std::cin>> m;

  float g=p/m;
  std::cout <<std::fixed << "A aceleração da gravidade é: "<<std::setprecision(3)<<g<<std::endl;

  float t=2*(3.14*pow((l/g),0.5));
  std::cout <<std::fixed << "O período do pêndulo é: "<<std::setprecision(3)<<t<<std::endl;
}