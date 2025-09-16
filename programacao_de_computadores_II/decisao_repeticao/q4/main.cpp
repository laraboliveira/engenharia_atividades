#include <iomanip>
#include <iostream>
#include <string>
using std::cin;
using std::cout;
using std::endl;

int main() {
  std::string entrega;
  std::string fechar;
  fechar = "não";
  int contIt,quant = 0;
  float somaT, preço = 0;
  
  std::cout << "Caixa Aberto\n" << endl;
  while (fechar != "sim") {
    cout << "\nQuantidade de itens do pedido: ";
    cin >> quant;
    float somaP=0;
    for (int i = 0; i < quant; i++) {
      cout << ". Preço do item " << i + 1 << ": R$";
      cin >> preço;
      somaP = somaP + preço;
    }
    cout << ". Cobrar delivery? ";
    cin >> entrega;
    if (entrega == "sim") {
      somaP = somaP + 15;
    }
    contIt = contIt + 1;
    cout << std::fixed << std::setprecision(2) << ". Valor do pedido: R$ "
         << somaP << endl;
    cout << "Fechar o caixa? ";
    cin >> fechar;
    somaT=somaT+somaP;
  }
  cout << std::fixed << std::setprecision(2)
       << "\nCaixa fechado!\nNúmero de pedidos: " << contIt
       << "\nValor total vendido: R$ " << somaT << endl;
}