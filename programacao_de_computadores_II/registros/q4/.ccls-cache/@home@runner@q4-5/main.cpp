#include <iostream>
#include <fstream>

using namespace std;

struct Aluno{
  string nome;
  float nota1;
  float nota2;
};

int main() {
  
  float media;
  Aluno aluno[10];
  ofstream arquivo("alunos.txt");
  if (arquivo.is_open()){
    for (int i=0;i<10;i++){
      cout << "Digite o nome do aluno "<<i+1<<": ";
      cin >> aluno[i].nome;
      cout << "Digite a nota 1:";
      cin >> aluno[i].nota1;
      cout << "Digite a nota 2: ";
      cin >> aluno[i].nota2;
      media=(aluno[i].nota1+aluno[i].nota2)/2;
      arquivo<<aluno[i].nome<<" ";
      arquivo<<aluno[i].nota1<<" ";
      arquivo<<aluno[i].nota2<<" ";
      arquivo<<media<<endl;
    }
    arquivo.close();
    cout<<"Os dados dos alunos foram gravados no arquivo alunos.txt." << endl;
  } else {
    cout << "Não foi possível abrir o arquivo alunos.txt." << endl;
  }  
}