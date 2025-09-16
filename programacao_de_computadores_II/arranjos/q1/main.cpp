#include <iostream>
#include <iomanip>
#include<vector>

void getMetrics(std::vector<int>&cqsabe,float &media,int &maior, int &menor){
  float soma=0;
  for (int i=0; i<cqsabe.size();i++){
    soma=soma+cqsabe[i];
    if (cqsabe[i]>maior){
      maior=cqsabe[i];
    }
    if (cqsabe[i]<menor){
      menor=cqsabe[i];
    }
  }
  media=soma/cqsabe.size();
}

int main() {
  char resp='s';
  std::vector<int>cqsabe;
  std::cout << "Digite as notas dos alunos (entre 0 e 100)\n"<<std::endl;
  int nota, maior=-1, menor=101,contNota=1;
  float media=0;
  while (resp == 's'){
    std::cout<<"Digite a nota "<<contNota<<':';
    std::cin>>nota;
    while (nota<0 || nota>100){
      std::cout<<"Nota inválida. Digite novamente a nota "<<contNota<<":";
      std::cin>>nota;
    }
    contNota=contNota+1;
    cqsabe.push_back(nota);
    std::cout<<"Deseja digitar outra nota? (s/n): ";
    std::cin>>resp;
  }
  getMetrics(cqsabe,media,maior,menor);
  std::cout<<std::fixed<<std::setprecision(2) << "\nMédia das notas: "<<media<<std::endl;
  std::cout<<std::fixed<<std::setprecision(0) << "Maior nota: "<<maior<<"\nMenor nota: "<<menor<<std::endl;
}