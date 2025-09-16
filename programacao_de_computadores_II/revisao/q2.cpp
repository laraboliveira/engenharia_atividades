#include <iostream>
#include <iomanip>
#include <locale>
using namespace std;

int calcularSomaDigitos(int num){
    int numAux,socorro;
    if (num%10==0){
        return num;
    }else{
        socorro=num/10;
        numAux=num%10;
        return numAux + calcularSomaDigitos(socorro);
    }
}

int main(){
    setlocale(LC_ALL,"portuguese");
    int num;
    cout<<"Digite um número inteiro: ";
    cin>>num;
    if (num<0){
        cout<<"ERRO: número negativo"<<endl;
    }else{
        int soma=calcularSomaDigitos(num);
        cout<<"A soma dos dígitos de "<<num<<"é: "<<soma<<endl;
    }
}
