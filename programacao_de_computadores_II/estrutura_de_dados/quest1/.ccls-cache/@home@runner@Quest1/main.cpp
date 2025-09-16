#include <iostream>
#include <set>

using namespace std;

int main() {
  int q,ele;
  cout << "Quantos elementos você deseja inserir na árvore binária? ";
  cin >> q;
  cout<<" "<<endl;
  
  set<int> arv;
  for(int i=0;i<q;i++){
    cout<<"Digite o elemento "<<i+1<<": ";
    cin>>ele;
    arv.insert(ele);
  }
  
  cout<<"\nDigite o elemento que você deseja buscar na árvore: ";
  cin>>ele;
  int resp=0;
  resp=arv.count(ele);
  
  if (resp==0){
    cout<<"O elemento "<<ele<<" não está presente na árvore.";
  } else{
    cout<<"O elemento "<<ele<<" está presente na árvore."; 
  }
  
  cout<<" "<<endl;
  cout<<"\nElementos da árvore binária: "<<endl;
  for(int j:arv){
    cout<<j<<" ";
  }
}
