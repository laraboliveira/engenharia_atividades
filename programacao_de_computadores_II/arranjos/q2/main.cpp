#include <iostream>
#include <iomanip>
#include <array>

using std::cout;
using std::cin;
using std::endl;

bool isPrimo(int num){
  for (int j=2; j<num; j++){
    if (num%j==0){
      return false;
    }
  }
  return true;
}
void classifyNumbers(std::array <int, 5> &numbers){
  bool resp;
  cout << "\nClassificações: " << endl;
  for (int k=0; k<numbers.size(); k++){
    resp=isPrimo(numbers[k]);
    if (resp==true) {
      cout<<numbers[k]<<" é um número primo"<<endl;
    }else{
      cout<<numbers[k]<<" não é um número primo"<<endl;
    }
  }
}

int main() {
  int num;
  std::array <int, 5> numbers;
  cout << "Verificação de número primo" << endl;
  for (int i=0;i<5;i++){
    cout << "Digite o número " << i+1 << ": ";
    cin>>num;
    while (num<=0){
      cout << "Número inválido. Digite o número "<<i+1<<" novamente: ";
      cin>>num;
    }
    numbers[i]=num;
  }
  
  classifyNumbers(numbers);
}