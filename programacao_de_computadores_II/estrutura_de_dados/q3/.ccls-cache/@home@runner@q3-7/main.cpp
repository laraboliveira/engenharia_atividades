#include <iostream>
#include <queue>
#include <stack>

using namespace std;

queue<int> inverterFila(queue<int> fila){
  stack<int> aux;
  while (!fila.empty()){
    int num=fila.front();
    fila.pop();
    aux.push(num);
  }
  while (!aux.empty()) {
    int num = aux.top();
    aux.pop();
    fila.push(num);
  }
  return fila;
}

void imprimirFila(queue<int> fila){
  while (!fila.empty()){
    int num=fila.front();
    fila.pop();
    cout<<num<<" ";
  }
}

int main() {
  int var;
  queue<int> fila;
  cout << "Digite um valor inteiro: ";
  cin>>var;
  while (var!=-1){
    fila.push(var);
    cout<<"Digite um valor inteiro: ";
    cin>>var; 
  }
  cout<<"Fila original: ";
  imprimirFila(fila);
  queue<int>invfila=inverterFila(fila);
  cout<<endl<<"Fila invertida: ";
  imprimirFila(invfila);
}