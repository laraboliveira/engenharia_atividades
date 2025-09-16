#include <iostream>
#include <fstream>

using namespace std;

int main() {
  ofstream arquivo("dados.txt");
  if (arquivo.is_open()){
    for(int i=0;i<100;i++){
      arquivo<<i+1<<endl;
    }
    arquivo.close();
  }else{
    cout << "Não foi possível abrir o arquivo" << endl;
  }
  
}