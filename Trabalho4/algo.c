#include <locale.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

void bubble(int *conj, int size);
void selection(int *conj, int size);
void insertion(int *conj, int size);

int main(int argc, char const *argv[])
{
    int total = 50000;
    int *arr = malloc(total * sizeof(int));
    int *bubArr = malloc(total * sizeof(int));
    int *insArr = malloc(total * sizeof(int));
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

    memcpy(bubArr, arr, total * sizeof(arr[0]));
    memcpy(insArr, arr, total * sizeof(arr[0]));
    printf("Carregado com sucesso!");
    
    fclose(teste);
    bubble(bubArr, total);
    selection(insArr, total);
/*   
    for (int i = 0; i < total; i++)
    {
        printf("%i\n", arr[i]);
    }
    */
    free(arr);
    free(bubArr);
    free(insArr);
    return 0;
}


void bubble(int *conj, int size)
{
    int tmp, changes = 10, interact = 0;
    clock_t timeRequired;
    timeRequired = clock();
    do
    {
        changes = 0;
        //printf("Interacao %i\n", interact);
        for (int i = 0; i < size - 1; i++)
        {
            if (conj[i] > conj[i+1])
            {
                tmp = conj[i];
                conj[i] = conj[i+1];
                conj[i+1] = tmp;
                changes++;
            }
        }
        interact++;

    } while (changes != 0);
    timeRequired = clock() - timeRequired;
    printf("Programa demorou %f segundos para organizar em bubble\n", (float)timeRequired / CLOCKS_PER_SEC);
    return;
}

void selection(int *conj, int size)
{
    int interact = 0, selecPos;
    clock_t timeReq;
    timeReq = clock();
    while (interact < size)
    {
        printf("Interacao %i\n", interact);
        int selecionado = conj[interact];
        for (int i = interact; i < size - 1; i++)
        {
            if (selecionado < conj[i+1])
            {
                selecionado = conj[i+1];
                selecPos = i+1;
            }
        }

        for (int i = selecPos; i > interact + 1; i--)
        {
            int tmp = conj[i];
            conj[i] = conj[i - 1];
            conj[i - 1] = tmp;
        }

        interact++;
    }
    timeReq = clock() - timeReq;

    printf("Programa demorou %f segundos para organizar em selection\n", (float)timeReq / CLOCKS_PER_SEC);
    
    return;
}

void insertion(int *conj, int size)
{ 
    // TODO
    return;
}

void shell(int *conj, int size)
{ 
    // TODO
    return;
}

void heap(int *conj, int size)
{ 
    // TODO
    return;
}

void merge(int *conj, int size)
{ 
    // TODO
    return;
}

void quick(int *conj, int size)
{ 
    // TODO
    return;
}