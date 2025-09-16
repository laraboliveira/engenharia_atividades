#include <iostream>
#include <fstream>

using namespace std;

struct Aluno{
  string nome;
  float nota1;
  float nota2;
  float media;
};

int main() {
  ifstream arquivo("alunos.txt");
  Aluno aluno[10];
  float maior=0;
  int a;
  if (!arquivo.is_open()) {
    cout << "Erro ao abrir o arquivo." << endl;
  }else{
    for(int i=0;i<10;i++){
      arquivo >> aluno[i].nome >> aluno[i].nota1 >> aluno[i].nota2 >> aluno[i].media;
      if (aluno[i].media > maior) {
        maior = aluno[i].media;
        a = i;
      }
    }
    arquivo.close();
    cout<<"Aluno com maior média:\n Nome: "<<aluno[a].nome<<"\nNota 1: "<<aluno[a].nota1<<"\nNota 2: "<<aluno[a].nota2<<"\nMedia: "<<aluno[a].media<<endl;
  }
}
  
