#include <iostream>
#include <iomanip>

using namespace std;

double calcularMedia(int *p,int q){
    int soma=0;
    for(int j=0;j<q;j++){
        soma = soma + p[j];
    }
    double media;
    return media=soma/q;
}

int main(){
    int quant;
    cout<<"Digite a quantidade de numeros: ";
    cin>>quant;
    int *pont=new int[quant];
    cout<<"Digite os numeros: "<<endl;
    for(int i=0;i<quant;i++){
        cout<<"Numero "<<i+1<<" : ";
        cin>>pont[i];
    }

    double media=calcularMedia(pont,quant);

    cout<<fixed<<setprecision(2)<<"Media: "<<media<<endl;
}
