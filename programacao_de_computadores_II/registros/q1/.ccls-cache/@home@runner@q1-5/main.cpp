#include <iostream>

using std::cout;
using std::string;
using std::cin;
using std::endl;

int main() {
  struct Carro{
    string marca;
    int ano;
    float disPer;
    float consLitros;
  };
  Carro carro;
  float quantL;
  cout << "Digite a marca: ";
  cin>>carro.marca;
  cout << "Digite o ano: ";
  cin>>carro.ano;
  cout << "Digite a distância: ";
  cin>>carro.disPer;
  cout << "Digite o consumo: ";
  cin>>carro.consLitros;
  quantL=carro.disPer/carro.consLitros;
  cout << "Quilômetros por litro: "<<quantL<<endl;
}