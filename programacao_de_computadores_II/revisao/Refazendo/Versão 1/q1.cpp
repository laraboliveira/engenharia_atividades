#include <iostream>
#include <iomanip>

using namespace std;

float calcularMedia(int *p, int q){
    float soma=0,media;
    for(int j=0;j<q;j++){
        soma=soma+p[j];
    }
    media=soma/q;
    return media;
}

int main(){
    int quant;
    cout<<"Digite a quantidade de numeros: ";
    cin>>quant;
    int*pont=new int[quant];
    cout<<"Digite os numeros: "<<endl;
    for(int i=0;i<quant;i++){
        cout<<"Numero"<<i+1<<" : ";
        cin>> pont[i];
    }

    double media=calcularMedia(pont, quant);

    cout<<fixed<<setprecision(2)<<"A media dos numeros digitados e: "<<media<<endl;

    delete [] pont;
}
