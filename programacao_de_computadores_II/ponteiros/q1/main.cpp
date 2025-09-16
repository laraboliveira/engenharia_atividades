#include <iostream>

using std::cout;
using std::cin;
using std::endl;

void maiorMenor(int *pont1, int *pont2){
  int maior,menor;
  if (*pont1> *pont2){
    cout<<"v1: "<<*pont1<<"    v2: "<<*pont2<<endl;
    cout<<"v1: "<<*pont1<<"    v2: "<<*pont2<<endl;
  }else{
    cout<<"v1: "<<*pont1<<"    v2: "<<*pont2<<endl;
    cout<<"v1: "<<*pont2<<"    v2: "<<*pont1<<endl;
  }
}
int main() {
  int *pont1, *pont2;
  int num1, num2;
  std::cout << "Digite o primeiro valor: ";
  cin>>num1;
  pont1=&num1;
  std::cout << "Digite o segundo valor: ";
  cin>>num2;
  pont2=&num2;
  maiorMenor(pont1,pont2);
}