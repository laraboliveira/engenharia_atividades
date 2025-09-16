#include <iostream>
#include <fstream>

using std::cout;
using std::cin;
using std::string;
using std::endl;
using std::ofstream;

int main() {
  ofstream alunos;
  alunos<<"nome"<<" "<<"nota 1"<<" "<<"nota 2"<<" "<<"media"<<endl;
  float media;
  struct Aluno{
    string nome;
    float nota1;
    float nota2;
  };
  Aluno aux[10];
  for (int i=0;i<10;i++){
    cout << "Digite o nome:";
    cin>>aux[i].nome;
    cout << "Digite a nota 1:";
    cin>>aux[i].nota1;
    cout << "Digite a nota 2: ";
    cin>>aux[i].nota2;
    media=(aux[i].nota1+aux[i].nota2)/2;
    alunos<<aux[i].nome<<" "<<aux[i].nota1<<" "<<aux[i].nota2<<" "<<media<<endl;
  }  
}