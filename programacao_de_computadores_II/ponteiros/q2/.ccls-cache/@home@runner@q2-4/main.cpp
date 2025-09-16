#include <iostream>
#include <array>

using std::cout;
using std::cin;
using std::endl;

int main() {
  int elementos[5];
  for (int i=0;i<5;i++){
    cout << "Elemento "<< i+1<< ":"<<endl;
    cin>> elementos[i];
  }
  cout<<"Vetor: ";
  for (int i=0;i<5;i++){
    cout<<*(elementos+i)*2<<"    ";
  }
}