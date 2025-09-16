#include <iostream>
#include <iomanip>

float calcularSálario(float valHora, int numHt,int numProd){
  float sal=0;
  if(numHt<=40){
    sal=valHora*numHt;
  } else{
    sal=valHora*40+(valHora*(numHt-40)*1.5);
  }
  sal=sal+numProd*2;
  return sal;
}

int main() {
  int numFun=0;
  float valHora=0;
  std::cout << "Informe o número de funcionários: ";
  std::cin>>numFun;
  std::cout << "Informe o valor fixo por hora: ";
  std::cin>>valHora;

  for(int i=0; i<numFun;i++){
    std::cout << "\nFuncionário "<<i+1<<std::endl;
    float numHt, numProd, sal=0;
    std::cout << "Informe o número de horas trabalhadas: ";
    std::cin>>numHt;
    std::cout << "Informe o número de produtos produzidos: ";
    std::cin>>numProd;
    sal=calcularSálario(valHora,numHt,numProd);
    std::cout<< std::fixed<<std::setprecision(2)<<"Salário: R$ "<<sal<<std::endl;
  }
}