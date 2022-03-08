#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int find(int);
int binary(int);
int longitud(int);
int unos(int, int);

int main(){
    int aux, n, bin;
    long count;
    FILE *filePointer;
    time_t t;
    
    do{
        printf("\n***MENU***\n");
        printf("1)Calcular manualmente\n");
        printf("2)Calcular automaticamente\n");
        printf("3)Salir\n");
        printf("\fSelecciona una opcion:");
        scanf("%i", &aux);

        switch (aux)
        {
        case 1:
            do
            {
                printf("\fSelecciona una n (mayor a 0 y menor a 1000) para calcular:");
                scanf("%i", &n);
            } while (n < 0 && n > 1000);
            break;
        
        case 2:
            srand(time(&t));
            n = rand() % 1000;
            break;

        case 3:
            fclose(filePointer);
            return 0;
            break;

        default:
            printf("\nError, opcion incorrecta.\n Seleccione una opcion correcta por favor");
            break;
        }

        filePointer = fopen("resultados.txt", "w");
        count = 1;

        do
        {
            bin = binary(count);
            fprintf(filePointer, "%d\n",bin);
            count++;    
        } while (unos(bin, 0) != n);
    
        n = 0;
        fflush(stdin);
        //system("python3 Practica1.py");
    }while (aux != 3);
}

int binary(int decimal_number)
{
    if (decimal_number==0)
        return 0;
    else
        return ((decimal_number%2)+(10*binary(decimal_number/2)));
}

int unos(int binary, int sum){
    
    int rest;

    if (binary == 0)
    {
        return sum;
    }
    else{
        rest = binary % 10;
        return sum + unos((binary /= 10), rest); 
    }
}
