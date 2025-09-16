#include <iostream>

using namespace std;

void preencheVetor(int *pont,int quant){
    cout<<"Digite os elementos do vetor: ";
    for(int i=0;i<quant;i++){
        cin>>pont[i];
    }
}

int main(){
    int quant;

    cout<<"Quantidade de elementos: ";
    cin>>quant;

    int* elementos=new int[quant];

    preencheVetor(elementos,quant);

    int *final=&elementos[quant];

    for(int *pontF=elementos;pontF!=final;pontF++){
        cout<<*pontF<<" ";
    }
    delete[]elementos;
}
