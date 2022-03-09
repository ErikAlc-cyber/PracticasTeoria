#include <algorithm>
#include <fstream>
#include <iostream>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <string>
#include <vector>
#include <math.h>
#include <sys/time.h>

using namespace std;
unsigned t0, t1;


int permuta(int n);
void Abrirarchi(void);
void Cerrararchi(void);
int conteo(char* cont);
int conteo1(char* cont1);
double logbase(double a, double base);

std::string cadena;
int i=0,m1,cad=0,cad1=0, comas=0, comast=1,contador=0,contador1=0;;
char caracter,caracter1;
double x1 = 0 ,x2=0;
double result, result1;

ofstream archivo;
ofstream archivo2;
ofstream archivo3;
ofstream archivo4;
ofstream archivo5;
ofstream archivo6;
ofstream archivo7;

int main(){
	int m=0, op, num;
	char res;
	srand(time(NULL));
	num = rand();
	
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
                    cout<<"\t\t[-----------Elija el valor de N---------------]\n";
                    cout<<"\t\t--->:";
                    cin>>m;
                    archivo<<"S = {";
             
                    for(int x = 0; x<m+1;x++){
                        
                        struct timeval begin, end;
                        gettimeofday(&begin, 0);
                        
                        permuta(x);
                        archivo<<endl<<endl;
                        gettimeofday(&end, 0);
                        long seconds = end.tv_sec - begin.tv_sec;
                        long microseconds = end.tv_usec - begin.tv_usec;
                        double elapsed = seconds + microseconds*1e-6;
    
						archivo7<<"Para N = "<<cad<<" El tiempo de ejecucion es: "<<elapsed<<"s."<<endl;
						
                        archivo2<<"Para N = "<<cad<<" tiene "<<contador<<" repeticiones "<<" de "<<caracter<<endl;
                        
	                    archivo3<<"Para N = "<<cad<<" tiene "<<contador1<<" repeticiones "<<" de "<<caracter1<<endl;
	                    
	                    x2 = contador1;
                        result1 = logbase(x2, 10);
                        archivo6<<"Para N = "<<cad<<" tiene "<<contador1<<" repeticiones "<<" de "<<caracter1<<" su logaritmo base 10 es:"<<result1<<endl;
                        comas = contador + contador1;
	                    archivo4<<"Para N = "<<cad<<" el numero de signos es "<<comas<<endl;
	                    
	                    x1 = comas;
                        result = logbase(x1, 10);
                        archivo5<<"Para N = "<<cad<<" tiene "<<comas<< " digitos y su log 10 es: "<<result<<endl;
                        
	                    contador = contador1 = comas = 0;
	                    cad++;
	               }
                    
                    archivo4<<"El total de numero de comas es "<<comast;
					Cerrararchi();
			break;
		  }
		case 2:{
			        Abrirarchi();
                    num=1+rand()%(28-1); 
                    for(int x = 0; x<num+1;x++)
                       permuta(x);
      
                    Cerrararchi();
			break;
		}
	  } 
	       
  }
	}while(res == 's'); 
}

int permuta(int n){
  int j = 1;
  int b = n;
  char arreglo[1000];     
      for (int i2 = n+2; i2 > 1; i2--){
           for(int i1 = n; i1 > 0; i1--){
               if(b < i1){
		       cadena += '1';
			   }
               else{
		       cadena += '0';
	           }
           }
           b--;
      do
      {  
         archivo<<"(";
         strcpy(arreglo,cadena.c_str()); 
         
         conteo(arreglo);
         conteo1(arreglo);
         archivo<<arreglo;
         archivo<<")";
         archivo<<",";
        
      } while (std::prev_permutation(cadena.begin( ),cadena.end( )) );
	  cadena.erase(cadena.begin(), cadena.end());
      } 
}

double logbase(double a, double base)
{
   return log(a) / log(base);
}

int conteo(char* cont){
	caracter = '0';
	for(int i=0; i<cadena.length(); i++){
		if(cont[i] == caracter){
			contador++;
		}
	}	
}

int conteo1(char* cont1){
	caracter1 = '1';
	for(int i=0; i<cadena.length(); i++){
		if(cont1[i] == caracter){
			contador1++;
		}
	}
}

void Abrirarchi(void){
	archivo.open("Permutaciones.txt",fstream::out);
	archivo2.open("Conteo de 0.txt",fstream::out);
	archivo3.open("Conteo de 1.txt",fstream::out);
	archivo4.open("Conte de simbolos.txt",fstream::out);
	archivo5.open("Logaritmo base 10 para simbolos.txt",fstream::out);
	archivo6.open("Logaritmo base 10 para 1.txt",fstream::out);
	archivo7.open("Tiempos de ejecucion.txt",fstream::out);
}

void Cerrararchi(void){
	archivo<<"}";
	archivo.close();
	archivo2.close();
	archivo3.close();
	archivo4.close();
	archivo5.close();
	archivo6.close();
	archivo7.close();
}
