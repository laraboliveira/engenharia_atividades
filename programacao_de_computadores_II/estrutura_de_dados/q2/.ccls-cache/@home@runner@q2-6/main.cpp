#include <iostream>
#include <list>
#include <stack>
#include <vector>
using namespace std;

bool procurar(stack<int, vector<int>> &f,int k){
  stack<int, vector<int>> aux;
  while (!f.empty()){
    int num=f.top();
    f.pop();
    if (num!=k){
      aux.push(num);
    }
    else{
      while (!aux.empty()){
        f.push(aux.top());
        aux.pop();
      }
      return true;
    }
  }
  while (!aux.empty()){
    f.push(aux.top());
    aux.pop();
  }
  return false;
}

int main() {
  int var;
  stack<int, vector<int>>f;
  cout << "Digite os valores inteiros (digite -1 para finalizar)"<<endl;
  cin>>var;
  while (var!=-1){
    f.push(var);
    cout<<"";
    cin>>var; 
  }
  int k;
  cout<<"Digite o valor K a ser removido da pilha: ";
  cin>>k;
  bool resp=procurar(f,k);  
  if (resp){
    cout<<"O valor "<<k<<" foi removido da pilha"<<endl<<endl;
    cout<<"Pilha atual: "<<endl;
  }else{
    cout<<"O valor "<<k<<" não foi encontrado na pilha"<<endl<<endl;
    cout<<"Pilha atual: "<<endl;
  }
  while (!f.empty()){
    int num=f.top();
    f.pop();
    cout<<num<<" ";
  }
}