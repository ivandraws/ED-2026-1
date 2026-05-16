#include <locale.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <iostream>
#include <fstream>

using namespace std;

class name_Vector {
    public:
        int size;
        int index;
        string* data;

        name_Vector(int n=100000){
            size = n;
            index = 0;
            data = new string[size];
        }

        name_Vector(const name_Vector& other) {

            size = other.size;
            index = other.index;

            data = new string[size];

            for(int i = 0; i < index; i++) {
                data[i] = other.data[i];
            }
        }
        
        void add_name(string nome){
            if(index == size)
                resize();

            data[index] = nome;
            
            index++;
        }

        void resize(){
            string* new_vector = new string[size*2];
            string* old_data = data;

            for(int i = 0; i<index;i++)
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

//====================== Heap sort tirado do princeton. ===============================
        void heapfy(int k, int n){
            while (2*k+1 <=n){
                int j = 2*k+1;
                if (j<n && lessthan(j, j+1)) j++;
                if(!lessthan(k,j))break;
                exch(k,j);
                k = j;
            }
        }
        void heapsort()
        { 
            int size = index-1;

            for(int k = (size-1)/2;k>=0; k--)
                heapfy(k,size);
            int k = size;
            while(k>0){
                exch(0,k--);
                heapfy(0,k);
            }
            return;
        }   
//================ ShellSort do geeks for geeks ==================================================
void shellsort()
{ 
    for(int gap = get_gap(index);gap>0; gap = (gap-1)/3){ //sequencia de knut
        for(int i = gap; i<index;i++){
            string key = data[i];
            int j = i;

            while(j>=gap && data[j-gap]>key){
                data[j]=data[j-gap];
                j-=gap;
                
            }
            data[j]=key;

        }
    }
    
}
//============== SelectionSort do IME USP=======
float selection()
        {
            int interact = 0;
            clock_t timeReq;
            timeReq = clock();
            int min;
            while (interact < index)
            {
                printf("Interacao %i\n", interact);
                min = interact;
                for (int i = interact + 1; i < index ; i++)
                {   
                    if (lessthan(i, min))
                    {
                        min = i;
                    }
                }
                exch(min, interact);

                interact++;
            }
    timeReq = clock() - timeReq;

    printf("Programa demorou %.3f segundos para organizar em selection\n", (float)timeReq / CLOCKS_PER_SEC);
    
    return (float)timeReq / CLOCKS_PER_SEC;
    }

//================ MegeSort Bottom Up do princeton =======================
void merge(string* aux, int lo, int mid, int hi)
{ 
    
    for(int k=lo; k<= hi; k++){
        aux[k] = data[k];
    }

    int i = lo, j = mid+1;
    for(int k=lo; k<=hi; k++){
        if      (i > mid)              data[k] = aux[j++];  
        else if (j > hi)               data[k] = aux[i++];
        else if (aux[j]<aux[i]) data[k] = aux[j++];
        else                           data[k] = aux[i++];
    }
}

void mergesort(){
    int n = index;
    string* aux = new string[index]; //criando cópia auxiliar
    for(int len=1;len<n;len*=2){
        for(int lo = 0 ; lo < n-len ; lo += len+len){
            int mid = lo+len-1;
            int hi = min(lo+len+len-1,n-1);
            merge(aux,lo,mid,hi);
        }
    }

    delete[] aux;
}

//=========Quick do Geeks for geeks usando o particionamento de lomuto ==================
void quickSort()
{ 
    quick(0,index-1);
}

void quick(int low, int high){
    if (low<high){
        int pi = aleatoriza_pivot(low,high);
        quick(low,pi-1);
        quick(pi+1,high);
    }
}

int partition(int low, int high){ //função que faz o particionamento usando o ultimo elemento como pivot
    string pivot = data[high];
    
    int i = (low-1);

    for(int j = low; j <= high-1; j++){
        if(data[j] <= pivot){
            i++;
            exch(i,j);
        }
    }
    exch(i+1,high);
    return (i+1);
}

int aleatoriza_pivot(int low, int high){ //função que pega um elemento aleatorio do vetor e o coloca na ultima posição
    srand(time(NULL));
    int random = low + rand() % (high-low);

    exch(random,high);
    return partition(low,high);
}
//================= Insertion 
float insertion()
{ 
    // FIXME - O tempo estava em 0.0000067 segundos. Fui testar e Não Está Ordenando.
    
    clock_t timeReq = clock();
    for (int i = 1; i < index; i++){
        string key = data[i];
        int j; 
        for(j= i-1; j >= 0 && data[j] > key ; j--)
            data[j+1]=data[j];

        data[j+1]=key;
    }
    timeReq = clock() - timeReq;
    printf("Progama demorou %f segundos para organizar em insertion\n",(float)timeReq/CLOCKS_PER_SEC);
    return (float)timeReq / CLOCKS_PER_SEC;
}
//==============================================================================
    private:
        bool lessthan(int i, int j)
        {
            return data[i]<data[j] ? true : false;
        }

        void exch(int i, int j)
        {
            string aux = data[i];
            data[i] = data[j];
            data[j] = aux;
        }
        
        int get_gap(int n){
            int h = 1;
            while(h<n/3){
                h = 3*h+1;
            }
            return h;
        }
};


name_Vector read_name_file(string name){
    name_Vector vector;
    
    ifstream arquivo(name);
    if(!arquivo.is_open()){
        throw runtime_error("Erro ao abrir arquivo\n");
    }
    string linha;
    while(getline(arquivo,linha)){
        vector.add_name(linha);
    }

    return vector;
}

int main(int agrc, char* const argv[])
{
    //apenas testes, remover depois
    name_Vector vector = read_name_file("nomes20k.txt");
    clock_t timeReq;
    timeReq = clock();
    vector.insertion();
    timeReq = clock() - timeReq;
    vector.show_names();
    printf("Progama demorou %f segundos para organizar em quicksort\n",(float)timeReq/CLOCKS_PER_SEC);
    
    return 0;
}









