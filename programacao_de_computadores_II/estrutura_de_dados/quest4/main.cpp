#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
  int q,id;
  unordered_map<std::string, int> tab;
  string name;
  cout << "Quantas pessoas você quer inserir? ";
  cin>>q;
  for(int i=0;i<q;i++){
    cout<<"Digite o nome da pessoa "<<i+1<<": ";
    cin>>name;
    cout<<"Digite a id da pessoa "<<i+1<<": ";
    cin>>id;
    tab[name]=id;
  }
  cout<<""<<endl;
  cout<<"Digite o nome para consultar a idade: ";
  cin>>name;

  auto it=tab.find(name);
  if(it!=tab.end()){
    cout<<"A idade de "<<name<<" é: "<<tab[name]<<endl;
  }else{
    cout<<"Nome não encontrado na tabela hash."<<endl;
  }
  cout<<""<<endl;
  cout<<"Elementos da tabela hash: "<<endl;
  for(auto j:tab){
    cout<<j.first<<": "<<j.second<<" anos."<<endl;
  }
}