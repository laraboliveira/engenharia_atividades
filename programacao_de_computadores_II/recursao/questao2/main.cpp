#include <iostream>

bool primo(int num,int div){
  if (num<2){
    return false;
  }
  if(div>=num){
    return true;
  }
  if(num%div==0){
    return false;
  }
  return primo(num,div+1);
}

using namespace std;

int main() {
  int num,div=2;
  cout << "Digite um número: ";
  cin>>num;
  while(num>0){
    bool resp=primo(num,div);
    if (resp){
      cout<<num<<" é um número primo"<<endl;
    }else{
      cout<<num<<" não é um número primo"<<endl;
    }
    cout << "Digite um número: ";
    cin>>num;
  }
}