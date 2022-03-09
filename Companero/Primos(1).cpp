#include <iostream>
#include <algorithm>
#include <fstream>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <string>
#include <vector>
#include <sys/time.h>
#include <limits>
#include <iomanip>
#include <cmath>


using namespace std;
// Definir prototipo de función
bool esPrimo(int numero);
string toBinary(int n);
void escribir(int n);
void Abrirarchi(void);
void Cerrararchi(void);

double logbase(double a, double base);
int conteo(char* cont);
int convertBinaryToDecimal(long long n);

char num[8000000];
int j=1, n1 = 0;
string cadena;

ofstream archivo;
ofstream archivo2;
ofstream archivo3;
ofstream archivo4;
ofstream archivo5;
ofstream archivo6;

int main() {

  int numero,op;
  char res;
  do{
  	cout<<"\t\t[-------Ejecutar s-------]\n";
	  cout<<"\t\t[-------Salir    n-------]\n";
	  cout<<"\t\t--->:";
      cin>>res;	
      if(res == 's'){
        cout<<"\n\t\t[------(1)Elegir numero de N----------------------------------]\n";
	    cout<<"\t\t[------(2)Encontrar el numero de N de forma aleatoria---------]\n";
	    cout<<"\t\t--->:";
	  cin>>op;
      switch(op){
      	case 1:{
      		Abrirarchi();
            cout<<"\t\t[------Escribe un número y te diré cuales son primos:---------]\n";
            cout<<"\t\t--->:";
            cin >> numero;
            archivo<<"Numeros primos son: ";
            archivo2<<"S = {";
               for(int i1 = 0; i1 <= numero;i1++){	
    	           if (esPrimo(i1)){
                       archivo<<i1<<",";
                       
                   }
               }
            archivo2<<"}";
            Cerrararchi();
			break;
		  }
		case 2:{
			Abrirarchi();
            numero=1+rand()%(20000001-1);
            archivo<<"Numeros primos son: ";
            archivo2<<"S = {";
               for(int i1 = 0; i1 <= numero;i1++){	
    	           if (esPrimo(i1)){
                       archivo<<i1<<",";
                       //archivo2<<toBinary(i)<<",";
                   }
               }
            archivo2<<"}";
            Cerrararchi();
			break;
		}
	}
}
  	
  }while(res == 's');
}

int convertBinaryToDecimal(int n)
{
   int z,x,n2=0, co = 0, cot = 0; 
   int binario[50]; 
   binario[0]=0; 
 

     for (x=0;x<50;x++) {   
        binario[x]=n%2; 
         n=n/2; 
          if(n==0)
         break; 
     } 

    for(z=x;z>=0;z--) {
	 
       archivo2<<binario[z];
    
       if(binario[z] == 1)
	   {
    	  co++;
    	  cot++;
	   }
	   else{
	      cot++;
		   }
    }
    archivo2<<",";
    archivo3<<cot<<",";
    archivo4<<logbase(cot,10)<<",";
    archivo5<<co<<",";
	archivo6<<logbase(co,10)<<",";
   }

double logbase(double a, double base)
{
   return log(a) / log(base);
}

bool esPrimo(int numero) {
  if (numero == 0 || numero == 1 || numero == 4) return false;
  for (int x = 2; x < numero / 2; x++) {
    if (numero % x == 0) return false;
  }
  convertBinaryToDecimal(numero);
  return true;
}

void Abrirarchi(void){
	archivo.open("Numeros Primos Enteros.txt",fstream::out);
	archivo2.open("Numeros Primos Binarios.txt",fstream::out);
	archivo3.open("Numero de Signos en cadenas.txt",fstream::out);
	archivo4.open("Log(10) de numeros de Signos en cadenas.txt",fstream::out);
	archivo5.open("Numeros de 1s en cadenas.txt",fstream::out);
	archivo6.open("Log(10) de numeros de 1s en cadenas.txt",fstream::out);
}

void Cerrararchi(void){
	archivo.close();
	archivo2.close();
	archivo3.close();
	archivo4.close();
	archivo5.close();
	archivo6.close();
}
