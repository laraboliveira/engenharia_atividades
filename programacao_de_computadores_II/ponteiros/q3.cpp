#include <iostream>

using namespace std;

int* getIntersection(int quant, int &var, int *pont1, int *pont2){
    int *pont3=new int[var];
    for (int k=0; k<quant;k++){
        if (pont1[k]==pont2[k]){
            pont3[var]=pont1[k];
            var=var+1;
        }
    }
    return pont3;
}

int main() {
    int quant,*pont1,*pont2,var;

    cout << "Quantidade de elementos: ";
    cin >> quant;

    int victor[quant];
    int vitor[quant];

    cout << "Vetor 1: ";
    for (int i=0; i<quant;i++){
        cin>>victor[i];
    }
    cout << "Vetor 2: ";
    for (int j=0; j<quant;j++){
        cin>>vitor[j];
    }
    pont1=&victor[0];
    pont2=&vitor[0];
    int *pont;
    pont=getIntersection(quant, var, pont1, pont2);
    cout<<"Vetor 3: ";
    if (var==0){
        cout<<"Os vetores informados não possuem elementos comuns."<<endl;
    }else{
        for (int m=0;m<var;m++){
            cout<<pont[m]<<" ";
        }
    delete [] pont;
    }
}
