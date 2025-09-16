#include <iostream>

using std::cout;
using std::cin;
using std::endl;

int buscaBinária(int num[], int pi, int pf,int chave){
  int meio=(pi+pf)/2;
  if(num[meio]==chave){
    return meio;
  }else{
    if (pi<pf && num[meio]>chave){
      return buscaBinária(num, meio+1, pf, chave); 
    } else if(pi<pf && num[meio]){
      return buscaBinária(num, pi, meio-1, chave); 
    } else{
      return -1;
    }
  }
}

int main() {
  int tam,resp;
  cout << "Digite o tamanho do array: ";
  cin>>tam;
  int num[tam];
  cout <<"Digite os elementos do array separados por espaço: ";
  for (int i=0;i<tam;i++){
    cin>>num[i];
  }
  int chave;
  cout <<"Digite a chave que deseja buscar: ";
  cin>>chave;
  int pi=0,pf=tam-1;

  resp=buscaBinária(num, pi, pf,chave);

    if (resp==-1){
      cout<<"A chave informada não se encontra no array."<<endl;
    } else{
      cout<<"A chave "<<chave<<" foi encontrada no índice "<<resp<<"  do array."<<endl;
    }
}