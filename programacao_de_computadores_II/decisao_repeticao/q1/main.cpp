#include <iostream>

int main() {
  using std::cout;
  using std::cin;
  float nota,freq=0;
  cout << "Média no semestre: ";
  cin>>nota;
  cout << "Frequência no semestre: ";
  cin>>freq;
 
  if ((nota>=6) and (freq>=75))
  {
    cout << "Conceito: Aprovado"<<std::endl;
  }
  else if (nota<6){
    cout << "Conceito: exame especial"<<std::endl;
    float rest=0;
    rest=6-nota;
    cout<< std::fixed <<std::setprecision(2)<< "Justificativa: média "<<rest<<" abaixo da mínima"<<std::endl;
}
  else{
    cout << "Conceito: reprovado por faltas"<<std::endl;
    float rest=0;
    rest=75-freq;
    cout << std::fixed <<std::setprecision(2)<<"Justificativa: frequência "<<rest<<"% abaixo da mínima"<<std::endl;
  }
    
}