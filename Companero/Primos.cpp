#include<stdio.h>
#include <stdlib.h>
#include<time.h>
#include<math.h>


int menu();
int sii();
int noo();
void creacion(int n, int *u, int *c, int *);
void decimal(int );
void conuno(int );
void contodos(int );
void concadena(int );
void conunol(int );
void contodosl(int );
	

int main(){
	int p=0,c,a=0,b=0,d,h = 1;
	
	 //while(h==1)
	 //{
	 	p = menu();
		 if(p == 1){
		 	
		 	c=sii();
		 }
		 if(p == 2){
		 	
		 	c=noo();
		 }
		 
		 creacion(c,&a,&b,&d);
		//printf("¿Quiere repetir?");
		//printf("\n 1 = si");
		//printf("\n 2 = no");
		//scanf("%d",&h);
		
	//}
	 return 0;
}

void decimal(int na )
{
	
	FILE * flujo4 = fopen("decimales.txt","a");
	if (flujo4 == NULL)
	{
		perror("Eror en la creacion del archivo\n\n");
	
	}
	if(na == 2 )
	{
		fputc('1',flujo4);
		fputc(' ',flujo4);
		
	}
	int n= 0,t,x=10,y,r,m,z,l=0,k,o,d,h=na;
	char j;

		
		if(h>0 && h<10)
		{
			j= h + '0';
			fputc(j,flujo4);
			fputc(' ',flujo4);
		}
		if(h>9)
		{
			n=0;
			x=10;
			l=0;
			r=h;
			for(t=1;t<h+1;t++)
			{
				if(t==x)
				{
					n +=1;
					x*=10;
				}	
			}
		     k=x/10;
		     d=k;
			for(y=0;y<n;y++)
			{
				m=r%10;
				r=r/10;
				l+=(m*k);
				k/=10;
				if(y == n-1)
				{
					l+=r;
				}
			}
			k=d;
			r=l;
			for(o=0;o<n;o++)
			{
				m=r%10;
				r=r/10;
				l=m;
				k/=10;
				j= l + '0';
				fputc(j,flujo4);
				if(o == n-1)
				{
					l=r;
					j= l + '0';
					fputc(j,flujo4);
				}
				
			}
			fputc(' ',flujo4);
		}
	fflush(flujo4);
	fclose(flujo4);
}

void creacion(int n, int *a, int *b, int *d)
{
	FILE * flujo3 = fopen("decimales.txt","w");
	if (flujo3 == NULL)
	{
		perror("Eror en la creacion del archivo\n\n");
	
	}
	fputc(' ',flujo3);
	fflush(flujo3);
	fclose(flujo3);
	
	
	FILE * flujo2 = fopen("binarios.txt","w");
	if (flujo2 == NULL)
	{
		perror("Eror en la creacion del archivo\n\n");
	
	}
	fputc(' ',flujo2);
	fflush(flujo2);
	fclose(flujo2);
	FILE * flujo = fopen("binarios.txt","a");
	if (flujo == NULL)
	{
		perror("Eror en la creacion del archivo\n\n");
	
	} 
	fputc('1',flujo);
	fputc('0',flujo);
	fputc(' ',flujo);
	
	int l,x,k=0,s,t,j=2;
	for(l=2;l<n+1;l++)
	{
	  for(x=2;x<=l;x++)
	  {
	  	if(l%x==0  )
	  	{
	  		k=1;
	  		break;
		}
	  }
	  if(k==1 && l==x)
		{
			k=0;
			t=l;
			decimal(l);
			if(t>pow(2,j))
			{
				j++;
			}
			for(s=0;s<j;s++)
			{
				if(t%2==0)
				{
					fputc('0',flujo);
				}
				else
				{
					fputc('1',flujo);
				}
				t/=2;
				
			}
			fputc(' ',flujo);
		
		}
	}
	fflush(flujo);
	fclose(flujo);
	//fflush(flujo3);
	//fclose(flujo3);
	
}

int menu()
{
	int p=0,n=0,m;
	while(n==0){
		printf("¿Quieres eleguir el valor de n? ");	
		printf("\n\n si=1");
		printf("\n\n no=2\n\n");
		scanf("%d",&m);
		if(m ==1){
			n +=1;
			system("cls");
			return m;
			
		}
		if(m ==2){
			n +=1;
			system("cls");
			return m;
		}	
	}	
}

int sii()
{
	int m,p=0;
	while(p==0){
		printf("\n\n¿Cual es el valor de n ? ");	
		scanf("%d",&m);
		system("cls");
		if(m<pow((2*10),7))
		{
			return m;
		}
		else
		{	
			printf("n es muy grande, eliga otro valor ");	
			scanf("%d",&m);
		}
	
	}
		
}

int noo()
{
	int v = rand()%28;
	return v;	
}

