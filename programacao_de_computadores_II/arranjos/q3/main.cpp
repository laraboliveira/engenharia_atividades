#include <iostream>
#include <iomanip>
#include <vector>

using std::cout;
using std::cin;
using std::endl;


int main() {
  int soma=0,quant,ra,id;
  float media;
  std::vector<int> matricula;
  std::vector<int> idade;
  cout << "Digite o número de alunos da turma: ";
  cin>>quant;

  for (int i=0;i<quant;i++){
    cout<<"Aluno "<<i+1<<" :"<<endl;
    cout<<"   Matrícula: ";
    cin>>ra;
    cout<<"   Idade: ";
    cin>>id;
    idade.push_back(id);
    matricula.push_back(ra);
    soma=soma+id;
  }
  media=soma/quant;
  cout<<std::fixed<<std::setprecision(2)<<"Alunos com idade pelo menos 5 anos maior que a média ("<<media<<"):"<<endl;
  for (int j=0;j<quant;j++){
    if (idade[j]>media+5){
      cout << "Matrícula: " << matricula[j] << std::endl;
    }
  }
  
}