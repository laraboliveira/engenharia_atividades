#include <iostream>

using namespace std;

struct Aluno{
    string nome;
    float nota;
};

int main (){
    int quant;
    cout<<"Quantidade de alunos: ";
    cin>>quant;

    Aluno aluno[quant];

    for(int i=0;i<quant;i++){
        Aluno *pont=&aluno[i];
        cout<<"\nAluno "<<i+1<<": "<<endl;
        cout<<"   Nome: ";
        cin>>pont->nome;
        cout<<"   Nota: ";
        cin>>pont->nota;
    }
    cout<<"\nResultado: "<<endl;
    for (int j=0;j<quant;j++){
        cout<<"   "<<aluno[j].nome<<" ("<<aluno[j].nota<<"): ";
        if (aluno[j].nota>=6){
            cout<<"Aprovado(a)"<<endl;
        } else if (aluno[j].nota>=3){
            cout<<"Exame Especial"<<endl;
        }else{
            cout<<"Reprovado(a)"<<endl;
        }
    }

}
