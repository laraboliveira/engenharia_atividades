#include <iostream>
#include <locale>
#include <fstream>

using namespace std;


struct Estoque{
    int codigo;
    string tecido;
    double metragem;
};

bool vendaTecido(Estoque est[],int sla,int cod, double met){
    for(int i=0;i<sla;i++){
        if ((est[i].metragem>met) && (est[i].codigo==cod)){
            return true;
        }
    }
    return false;
}

int main(){
    setlocale(LC_ALL,"portuguese");
    std::ifstream arq("estoque.txt");
    Estoque est[1000];
    int cod, sla=0;
    double met;
    bool resp;
    for (int i=0;i<1000;i++){
        arq>>est[i].codigo>>est[i].tecido>>est[i].metragem;
        sla++;

    }
    arq.close();
    cout<<"Loja de Tecidos Bela Estampa"<<endl;
    cout<<"Digite o código do tecido: ";
    cin>>cod;
    cout<<"Digite a metragem desejada: ";
    cin>>met;
    resp=vendaTecido(est,sla,cod,met);
    if (resp){
        cout<<"Venda realizada com sucesso!"<<endl;
    } else{
        cout<<"Não foi possível realizar a venda!"<<endl;
    }
}

