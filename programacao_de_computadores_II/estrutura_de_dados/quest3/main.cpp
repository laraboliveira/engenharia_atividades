#include <iostream>
#include <unordered_set>

using namespace std;

int main() {
  cout << "Informe os nomes para serem armazenados na tabela hash."<<endl;
  cout<<"Digite sair para parar de adicionar nomes."<<endl;
  unordered_set<string> map;
  string name="laris";

  while (name!="sair"){
    cout<<"Digite um nome: ";
    cin>>name;
    map.insert(name);
  }
  
  cout<<"Digite o nome que deseja procurar na tabela: ";
  cin>>name;
  unordered_set<string>::iterator ixi=map.find(name);
  unordered_set<string>::iterator eita=map.end();
  if (ixi==eita){
    cout<<name<<" não está na tabela hash."<<endl;
  }else{
    cout<<name<<" está na tabela hash."<<endl;
  }
}