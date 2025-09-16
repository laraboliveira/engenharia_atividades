#include <iostream>
#include <list>
using namespace std;

int main() {
  int quant;
  list<int> lista;
  cout<<"Quantos elementos voce deseja adicionar a lista? ";
  cin>>quant;

  cout<<"Digite os elementos da lista: ";
  for(int i=0;i<quant;i++){
    int var;
    cin>>var;
    lista.push_back(var);
  }
  cout<<"Elementos da lista: ";

  for(auto it=lista.begin();it!=lista.end();++it){
    cout<<*it<<" ";
  }
  lista.pop_front();
  lista.pop_back();
  cout<<""<<endl;
  cout<<"Elementos da lista após a remoção: ";
  for (int num:lista){
    cout<<num<<" ";
  }
}