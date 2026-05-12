#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void bubble(int conjunto[], int size);

int main(int argc, char const *argv[])
{
    int total = 50000;
    int *arr = malloc(total * sizeof(int));
    if (arr == NULL)
    {
        printf("Falha na alocacao de memoria");
        return 1;
    }

    FILE *teste = fopen("numeros.txt", "r");
    if (teste == NULL)
    {
        printf("Nao foi possivel abrir o arquivo\n");
        return 1;
    }
    
    int cont = 0;

    while(cont < total && fscanf(teste, "%i", &arr[cont]) == 1)
        cont++;


    printf("Carregado com sucesso!");
    fclose(teste);
    bubble(arr, total);
/*   
    for (int i = 0; i < total; i++)
    {
        printf("%i\n", arr[i]);
    }
    */
    free(arr);
    return 0;
}


void bubble(int *conjunto, int size)
{
    int tmp, changes = 10;
    clock_t timeRequired;
    timeRequired = clock();
    do
    {
        changes = 0;
        for (int i = 0; i < size - 1; i++)
        {
            if (conjunto[i] > conjunto[i+1])
            {
                tmp = conjunto[i];
                conjunto[i] = conjunto[i+1];
                conjunto[i+1] = tmp;
                changes++;
            }
        }

    } while (changes != 0);
    timeRequired = clock() - timeRequired;
    printf("Programa demorou %f segundos para organizar", (float)timeRequired / CLOCKS_PER_SEC);
    return;
}

int selection(int conjunto[], int size)
{
    return 0;
}