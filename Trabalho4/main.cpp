#include <locale.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <iostream>

using namespace std;

class name_Vector {
    public:
        int size = 100000;
        int index = 0;
        string* data = new string[size];

        void add_name(string nome){
            if(index == size)
                resize();

            data[index] = nome;
            
            index++;
        }

        void resize(){
            string* new_vector = new string[size*2];
            string* old_data = data;

            for(int i = 0; i<size;i++)
                new_vector[i] = old_data[i];

            data = new_vector;
            delete[] old_data;
            size *= 2;
        }
        
        void show_names(){
            for (int i = 0; i<index; i++)
                cout<<data[i]<<"\n";
        }

        ~name_Vector() {
            delete[] data;
        }

        
    
};




int main()
{
    name_Vector vector;
    
    ifstream arquivo("nomes.txt");

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