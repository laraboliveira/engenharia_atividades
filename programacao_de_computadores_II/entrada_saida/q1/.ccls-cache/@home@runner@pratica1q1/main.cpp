#include <iostream>
#include <cmath>
#include <iomanip>

using std::cout;
using std::cin;

int main() 
{
  float a,q,val=0;
  int n=0;
  
  std::cout << "Informe o primeiro termo: ";
  std::cin>>a;
  
  std::cout << "Informe a razão: ";
  std::cin>>q;
    
  std::cout << "Informe o número do termo: ";
  std::cin>>n;

  val=a*pow(q,(n-1));
  
  std::cout<<std::fixed<<"o termo a("<<n<<") é "<<std::setprecision(2)<<val<<std::endl;
}