#include <iostream>
#include <iomanip>

int main() {
  using std::cout;
  using std::cin;
  
  float total,c=0;
  cout << "Capital Total para empréstimo: ";
  cin>>total;

  while (total>=0){
    cout << "Capital emprestado: ";
    cin>>c;
    
    if ((total-c)<0){
      cout <<std::fixed<<std::setprecision(2)<< "Empréstimo negado, capital total é de R$"<<total<<std::endl;
      total=total-c;
    }
      
    else{
      int m=0;
      float j,t=0;
      cout << "Quantidade de meses para quitação: ";
      cin>>m;
      
      if (c<=10000){
        t=0.1;
        cout <<std::fixed<<std::setprecision(2)<< "Taxa de juros aplicada: 10%"<<std::endl;
      }
        
      else{
        t=0.07;
        cout <<std::fixed<<std::setprecision(2)<< "Taxa de juros aplicada: 7%"<<std::endl;
      }
      
      j=c*t*m;
      cout <<std::fixed<<std::setprecision(2)<< "Juros devido: "<<j<<std::endl;
      float vf=0;
      vf=c+j;
      cout <<std::fixed<<std::setprecision(2)<< "Valor total: "<<vf<<std::endl;
      total=total-c;
    }
  }
}