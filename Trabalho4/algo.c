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
    // TODO: Test setlocale() later
    /*
    if (argc != 2 && argv[1] < 1 || argv[1] > 1000001 && argv[2] == NULL)
    {
        printf("Usage: ./algo <numero_de_elementos> <arquivo.txt>");
        printf("Lembre-se, o máximo que o array pode chegar é 1 milhão);
    }
    */

    setlocale(LC_ALL, "UTF-8");
    int total = 50000;
    int *arr = malloc(total * sizeof(int));
    if (arr == NULL)
    {
        printf("Falha na alocação de memória\n");
        return 1;
    }
    int *bubArr = malloc(total * sizeof(int));
    if (bubArr == NULL)
    {
        printf("Falha na alocação de memória\n");
        free(arr);
        return 1;
    }
    int *insArr = malloc(total * sizeof(int));
    if (insArr == NULL)
    {
        printf("Falha na alocaação de memória\n");
        free(arr);
        free(bubArr);
        return 1;
    }
    int *selecArry = malloc(total * sizeof(int));
    if(selecArry == NULL)
    {
        printf("Falha na alocação de memória\n");
        free(arr);
        free(selecArry);
        return 1;
    }
    int *mergeArry = malloc(total * sizeof(int));
    if(mergeArry == NULL)
    {
        printf("Falha na alocação de memória\n");
        free(arr);
        free(mergeArry);
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
    memcpy(selecArry,arr,total * sizeof(arr[0]));
    printf("Carregado com sucesso!\n");
    
    fclose(teste);
    bubble(bubArr, total);
    selection(selecArry, total);
    insertion(insArr,total);
/*   
    for (int i = 0; i < total; i++)
    {
        printf("%i\n", arr[i]);
    }
    */
    free(arr);
    free(bubArr);
    free(insArr);
    free(selecArry);
    free(mergeArry);
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
    int interact = 0;
    clock_t timeReq;
    timeReq = clock();
    int min;
    while (interact < size)
    {
        //printf("Interacao %i\n", interact);
        min = interact;
        for (int i = interact + 1; i < size ; i++)
        {   
            if (conj[i] < conj[min])
            {
                min = i;
            }
        }
        int tmp = conj[interact];
        conj[interact] = conj[min];
        conj[min] = tmp;

        

        interact++;
    }
    timeReq = clock() - timeReq;
    /*
    for (int i = 0; i < size; i++)
    {
        printf("%i\n", conj[i]);
    }
    */
    printf("Programa demorou %f segundos para organizar em selection\n", (float)timeReq / CLOCKS_PER_SEC);
    
    return;
}

void insertion(int *conj, int size)
{ 
    int interect = 0;
    clock_t timeReq = clock();
    for (int i = 1; i< size; i++){
        int chave = conj[i];
        int j = 1 - 1;

        while( j>= 0){
            interect++;
            if( conj[j] > chave){
                conj[j + 1] = conj[j];
                j--;
            }
            else{
                break;
            }
        conj[j + 1] = chave;
        }
    }
    timeReq = clock() - timeReq;
    printf("Progama demorou %f segundos para organizar em insertion\n",(float)timeReq/CLOCKS_PER_SEC);

    return;
}

void shell(int *conj, int size)
{ 
    // TODO (Héder)
    return;
}

void heap(int *conj, int size)
{ 
    // TODO (Héder)
    return;
}

void merge(int *conj, int size)
{ 
    // TODO (Luiz)
    return;
}

void quick(int *conj, int size)
{ 
    // TODO (Luiz e Ivan)
    return;
}

void free_all()
{
    // TODO
    return;
}