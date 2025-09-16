#include <iostream>
#include <iomanip>

using std::cin;
using std::cout;

int main() {
  int quant,cont1=0;
  char nome[50]="";
  cout << "Informe o nome do juiz: ";
  cin>>nome;
  cout << "Quantidade de partidas: ";
  cin>>quant;
  
  int imp,fal,car=0;
  float contTemp,contImp,contFal,contCar,temp=0;

  while (cont1!=quant){
    cout << "\nPartida "<<cont1+1<<":"<<std::endl;
    cout << ". Impedimentos.......: ";
    cin>>imp;
    contImp=contImp+imp;
    cout << ". Faltas.............: ";
    cin>>fal;
    contFal=contFal+fal;
    cout << ". Cartões............: ";
    cin>>car;
    contCar=contCar+car;
    cout << ". Tempo de acréscimo.: ";
    cin>>temp;
    contTemp=contTemp+temp;
    cont1++;
  }
  
  contImp=contImp/cont1;
  contFal=contFal/quant;
  contCar=contCar/quant;
  contTemp=contTemp/quant;
  
  cout << "\nEstatísticas do juiz "<<nome<<":"<<std::endl;
  cout<<std::fixed<<std::setprecision(2) << ". Impedimentos.......: "<<contImp<<"."<<std::endl;
  cout<<std::fixed<<std::setprecision(2) << ". Faltas.............: "<<contFal<<"."<<std::endl;
  cout<<std::fixed<<std::setprecision(2) << ". Cartões............: "<<contCar<<"."<<std::endl;
  cout<<std::fixed<<std::setprecision(2) << ". Tempo de acréscimo.: "<<contTemp<<"."<<std::endl;
  
}