#include <iostream>

using namespace std;

int bubbleSort(int *vetor,int q,int opc){
  int cont=0;
  for(int i=0;i<q;i++){
    for(int j=0;j<q-i-1;j++){
      if (opc==1){ 
        if (vetor[j]>vetor[j+1]){
          swap(vetor[j],vetor[j+1]);
          cont++;
        }
      }else if(opc==2){
        if (vetor[j]<vetor[j+1]){
          swap(vetor[j],vetor[j+1]);
          cont++;
        }
      }
    }
  } 
  return cont;
}

int selectionSort(int *vetor,int q,int opc){
  int cont=0,jaux;
  for(int i=0;i<q;i++){
    jaux=i;
    for(int j=i;j<q;j++){
      if (opc==1){
        if (vetor[j]<vetor[jaux]){        
          jaux=j;
        }
      }else if(opc==2){
        if (vetor[j]>vetor[jaux]){        
          jaux=j;
        }
      }
    }
    if (i!=jaux){
      swap(vetor[i],vetor[jaux]);
      cont++;
    } 
  }
  return cont;
}

int insertionSort(int *vetor,int q,int opc){
  int cont=0,j;
  for(int i=1;i<q;i++){
    j=i-1;
    if (opc==1){
      while((j>=0)&&(vetor[j]>vetor[j+1])){
        swap(vetor[j],vetor[j+1]);
        cont++;
        j=j-1;
      }
    }else if(opc==2){
      while((j>=0)&&(vetor[j]<vetor[j+1])){
        swap(vetor[j],vetor[j+1]);
        cont++;
        j=j-1;
      }
    }
  }
  return cont;
}

void swap(int *val1,int *val2){
  int aux=*val1;
  *val1=*val2;
  *val2=aux;  
}

int main() {
  int q,ord,met;
  cout << "Digite a quantidade de elementos: ";
  cin>>q;
  cout<<"Digite os 10 elementos separados por espaço: ";
  int a[q];
  
  for(int i=0;i<q;i++){
    cin>>a[i];
  }
  cout<<"\n1 − Crescente\n2 − Decrescente"<<endl;
  cout<<"\nEscolha a ordem de ordenacao: ";
  cin>>ord;
  cout<<"\n1 − Bubble Sort\n2 − Selection Sort\n3 − Insertion Sort"<<endl;
  cout<<"\nEscolha o metodo de ordenacao:  ";
  cin>>met;
  
  int *p=a;
  int cont;
  
  if (met==1){ //Bubble Sort
    cont=bubbleSort(p,q,ord);
  }else if(met==2){ //Selection Sorte
    cont=selectionSort(p,q,ord);
  } else{ //Insertion
    cont=insertionSort(p,q,ord);
  }
  
  
  
  cout<<"\nVetor ordenado: ";
  for(int i=0;i<q;i++){
    cout<<a[i]<<" ";
  } 
  
  if (ord==1){
    cout<<"\nMetodo de ordenacao: Crescente"<<endl;
  }else{
    cout<<"\nMetodo de ordenacao: Decrescente"<<endl;
  }
  cout<<"Numero de trocas: "<<cont<<endl;
}