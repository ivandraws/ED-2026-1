#include <locale.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

float bubble(int *conj, int size);
float selection(int *conj, int size);
float insertion(int *conj, int size);



int main(int argc, char const *argv[])
{
    // TODO: Test setlocale() later
    setlocale(LC_ALL, "pt-BR.utf8");
    if (argc != 2)
    {
        printf("Usage: ./algo <numero_de_elementos> <arquivo.txt>\n");
        printf("Lembre-se, o máximo que o array pode chegar é 1 milhão");
        return(-1);
    }

    int total = 50000;
    int *arr = malloc(total * sizeof(int));
    if (arr == NULL)
    {
        printf("Falha na alocação de memória do array original\n");
        return 1;
    }
    int *bubArr = malloc(total * sizeof(int));
    if (bubArr == NULL)
    {
        printf("Falha na alocação de memória para bubble\n");
        free(arr);
        // free_all(0);
        return 1;
    }
    int *insArr = malloc(total * sizeof(int));
    if (insArr == NULL)
    {
        printf("Falha na alocaação de memória para insertion\n");
        free(arr);
        free(bubArr);
        // free_all(1);
        return 1;
    }
    int *selecArry = malloc(total * sizeof(int));
    if(selecArry == NULL)
    {
        printf("Falha na alocação de memória para select\n");
        free(arr);
        free(bubArr);
        free(insArr);
        // free_all(2);
        return 1;
    }
    int *mergeArry = malloc(total * sizeof(int));
    if(mergeArry == NULL)
    {
        printf("Falha na alocação de memória para merge\n");
        free(arr);
        free(bubArr);
        free(insArr);
        free(selecArry);
        // free_all(3);
        return 1;
    }
    int *shellArr = malloc(total * sizeof(int));
    if (shellArr == NULL)
    {
        printf("Falha na alocação de memória para shell\n");
        free(arr);
        free(bubArr);
        free(insArr);
        free(selecArry);
        free(mergeArry);
        return 1;
    }


    FILE *teste = fopen("numeros.txt", "r");
    if (teste == NULL)
    {
        printf("Nao foi possivel abrir o arquivo\n");
        // free_all(-1);
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
    float timeBubble = bubble(bubArr, total);
    float timeSelect = selection(selecArry, total);
    float timeIns = insertion(insArr,total);
/*   
    for (int i = 0; i < total; i++)
    {
        printf("%i\n", arr[i]);
    }
    */

    FILE *results = fopen("resultados.csv", "w");
    if (results == NULL)
    {
        printf("Erro em criar o relatório de tempos\n");
    }
    else
    {
        fprintf(results, "algoritmos, tempo(segundos)\n");
        fprintf(results, "tempoBubble, %f\n", timeBubble);
        fprintf(results, "tempoSelection, %f\n", timeSelect);
        fprintf(results, "tempoInsertion, %f\n", timeIns);
    }
    fclose(results);
    free(arr);
    free(bubArr);
    free(insArr);
    free(selecArry);
    free(mergeArry);
    return 0;
}


float bubble(int *conj, int size)
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
    return (float)timeRequired / CLOCKS_PER_SEC;
}

float selection(int *conj, int size)
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
    
    return (float)timeReq / CLOCKS_PER_SEC;
}

float insertion(int *conj, int size)
{ 
    // FIXME - O tempo estava em 0.0000067 segundos. Fui testar e Não Está Ordenando.
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
    /*
    for (int i = 0; i < size; i++)
    {
        printf("%i\n", conj[i]);
    }
    */
    return (float)timeReq / CLOCKS_PER_SEC;
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

void free_all(int mode)
{
    // Ideia de criar uma função para limpar os malloc para reduzir quantidade de código
    switch (mode)
    {
    case 0:
        break;
    case 1:
        break;

    case 2:
        break;
    
    case 3:
        break;
    
    default:
        break;
    }
    return;
}