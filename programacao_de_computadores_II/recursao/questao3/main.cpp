#include <iostream>

int produto(int thekid[],int q){
  if(q==0){
    return 1;
  }
  return thekid[q-1]*produto(thekid,q-1);
}

using namespace std;

int main() {
  int q;
  cout << "Digite a quantidade de elementos: ";
  cin>>q;
  int billy[q];
  cout << "Digite os valores: ";
  for(int i=0;i<q;i++){
    cin>>billy[i];
  }
  int prod=produto(billy,q);
  cout<<"Produto dos valores informados: "<<prod<<endl;
}