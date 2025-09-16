#include <iostream>
#include <map>


using namespace std;

int main() {
  int q,ele,val;
  cout << "Digite o número de elementos da árvore: ";
  cin >> q;
  cout<<""<<endl;

  map<int,int> s_arv;

  for(int i=0;i<q;i++){
    cout<<"Digite a chave do elemento "<< i+1<<": ";
    cin>>ele;
    val=ele*ele;
    s_arv.insert({ele,val});
  }
  cout<<""<<endl;
  cout<<"Digite o elemento para remoção: ";
  cin>>ele;

  if(s_arv.count(ele)!=0){
    s_arv.erase(ele);
    cout<<""<<endl;
    cout<<"Árvore binária após a remoção: "<<endl;
    for(auto j:s_arv){
      cout<<"Chave: "<<j.first <<", Valor: "<<j.second<<endl;
    }
  }else{
    cout<<"Chave não encontrada!"<<endl;
  }
}