#include <iostream>
#include <iomanip>
#include <vector>

using std::cout;
using std::cin;
using std::endl;
using std::vector;

int soma(vector<int>vetor,int tamVetor){
  if (tamVetor==0){
    return 0;
  }else{
    return vetor[tamVetor-1]+soma(vetor, tamVetor-1);
  }
}

int main() {
  int tamVetor,elemento;
  vector <int> vetor;
  cout << "Digite o tamanho do vetor: ";
  cin >> tamVetor;
  if (tamVetor<=0){
    cout<<"ERRO: Valor inválido informado."<<endl;
  } else{
    cout<<"Digite os elementos do vetor:"<<endl;
    for(int i=0;i<tamVetor;i++){
      cout<<"Elemento "<<i+1<<": ";
      cin>>elemento;
      vetor.push_back(elemento);
    }
    int total=soma(vetor,tamVetor);
    cout<<"A soma dos elementos do vetor é: "<<total<<endl;
  }
}