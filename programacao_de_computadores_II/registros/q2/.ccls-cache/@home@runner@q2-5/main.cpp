#include <iostream>

using std::string;
using std::cout;
using std::cin;
using std::endl;

int main() {
  struct Aluno{
    string nome;
    float media;
    int numFalt;
    string sit;
  };
  int quant;
  
  cout << "Digite a quantidade de alunos: ";
  cin >> quant;

  Aluno aluno[quant];
  
  for (int i=0;i<quant;i++){
    cout << "Aluno "<<i+1<<":"<<endl;
    cout << "    Nome: ";
    cin>>aluno[i].nome;
    cout << "    Média: ";
    cin>>aluno[i].media;
    cout << "    Faltas:";
    cin>>aluno[i].numFalt;
    if (aluno[i].media>=6 && aluno[i].numFalt<=18){
      aluno[i].sit="APROVADO(A)";
    } else{
      aluno[i].sit="REAPROVADO(A)";
    }
  }
  for (int j=0;j<quant;j++){
    cout<<aluno[j].nome<<" "<<aluno[j].sit<<endl;
  }
}