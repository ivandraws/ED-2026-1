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
        
       
        bool validateOrdered(){
            for(int i = 1; i < index; i++)
                if(lessthan(i,i-1)) return false;
            return true;
        }

        void show_names(){
            for (int i = 0; i<index; i++)
                cout<<data[i]<<"\n";
        }

        ~name_Vector() {
            delete[] data;
        }
//===============Bubble Sort Geeks for geeks=================================
        float bubbleSort() {

            clock_t timeReq = clock();

            int n = index;
            bool swapped;

            for (int i = 0; i < n - 1; i++) {

                swapped = false;

                for (int j = 0; j < n - i - 1; j++) {

                    if (data[j] > data[j + 1]) {
                        swap(data[j], data[j + 1]);
                        swapped = true;
                    }
                }

                if (!swapped)
                    break;
            }

            timeReq = clock() - timeReq;

            printf("Programa demorou %f segundos para organizar em bubbleSort\n",
                (float)timeReq / CLOCKS_PER_SEC);

            return (float)timeReq / CLOCKS_PER_SEC;
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
        float heapsort()
        {
            clock_t timeReq = clock();

            int size = index - 1;

            for(int k = (size - 1) / 2; k >= 0; k--)
                heapfy(k, size);

            int k = size;

            while(k > 0){
                exch(0, k--);
                heapfy(0, k);
            }

            timeReq = clock() - timeReq;

            printf("Programa demorou %f segundos para organizar em heapsort\n",
                (float)timeReq / CLOCKS_PER_SEC);

            return (float)timeReq / CLOCKS_PER_SEC;
        }
//================ ShellSort do geeks for geeks ==================================================
        float shellsort()
        {
            clock_t timeReq = clock();

            for(int gap = get_gap(index); gap > 0; gap = (gap - 1) / 3){

                for(int i = gap; i < index; i++){

                    string key = data[i];
                    int j = i;

                    while(j >= gap && data[j-gap] > key){
                        data[j] = data[j-gap];
                        j -= gap;
                    }

                    data[j] = key;
                }
            }

            timeReq = clock() - timeReq;

            printf("Programa demorou %f segundos para organizar em shellsort\n",
                (float)timeReq / CLOCKS_PER_SEC);

            return (float)timeReq / CLOCKS_PER_SEC;
        }
//============== SelectionSort do IME USP=======
        float selection()
        {
            clock_t timeReq = clock();

            int interact = 0;

            while(interact < index){

                int min = interact;

                for(int i = interact + 1; i < index; i++){

                    if(lessthan(i, min)){
                        min = i;
                    }
                }

                exch(min, interact);

                interact++;
            }

            timeReq = clock() - timeReq;

            printf("Programa demorou %f segundos para organizar em selection\n",
                (float)timeReq / CLOCKS_PER_SEC);

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

        float mergesort()
            {
                clock_t timeReq = clock();

                int n = index;

                string* aux = new string[index];

                for(int len = 1; len < n; len *= 2){

                    for(int lo = 0; lo < n - len; lo += len + len){

                        int mid = lo + len - 1;
                        int hi = min(lo + len + len - 1, n - 1);

                        merge(aux, lo, mid, hi);
                    }
                }

                delete[] aux;

                timeReq = clock() - timeReq;

                printf("Programa demorou %f segundos para organizar em mergesort\n",
                    (float)timeReq / CLOCKS_PER_SEC);

                return (float)timeReq / CLOCKS_PER_SEC;
            }

//=========Quick do Geeks for geeks usando o particionamento de lomuto ==================
        float quickSort()
            {
                clock_t timeReq = clock();

                quick(0, index - 1);

                timeReq = clock() - timeReq;

                printf("Programa demorou %f segundos para organizar em quicksort\n",
                    (float)timeReq / CLOCKS_PER_SEC);

                return (float)timeReq / CLOCKS_PER_SEC;
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
            int random = low + rand() % (high-low+1);

            exch(random,high);
            return partition(low,high);
        }
//================= Insertion do IME USP =================
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

void writeCSV(float tempos[], int mode);

int main(int agrc, char* const argv[])
{   
    srand(time(NULL));

    if (agrc != 3){
        cout << "Usage ./main (nomedoarquivo.txt) (algoritmo)" << endl;
        return -1;
    }

    char* mode = argv[2];
    
    name_Vector original_vector = read_name_file(argv[1]);

    float results[5];

    int resPrint = -1;

    if(strcmp(mode, "sh") == 0){
        name_Vector vector = original_vector;
        for(int i = 0; i < 5; i++)
            results[i] = vector.shellsort();

        resPrint = 0;
    }

    else if(strcmp(mode, "he") == 0){
        name_Vector vector = original_vector;
        for(int i = 0; i < 5; i++)
            results[i] = vector.heapsort();

        resPrint = 1;
    }

    else if(strcmp(mode, "bu") == 0){
        name_Vector vector = original_vector;
        for(int i = 0; i < 5; i++)
            results[i] = vector.bubbleSort();

        resPrint = 2;
    }

    else if(strcmp(mode, "se") == 0){
        name_Vector vector = original_vector;
        for(int i = 0; i < 5; i++)
            results[i] = vector.selection();

        resPrint = 3;
    }

    else if(strcmp(mode, "in") == 0){
        name_Vector vector = original_vector;
        for(int i = 0; i < 5; i++)
            results[i] = vector.insertion();

        resPrint = 4;
    }

    else if(strcmp(mode, "me") == 0){
        name_Vector vector = original_vector;
        for(int i = 0; i < 5; i++)
            results[i] = vector.mergesort();

        resPrint = 5;
    }

    else if(strcmp(mode, "qu") == 0){
        name_Vector vector = original_vector;
        for(int i = 0; i < 5; i++)
            results[i] = vector.quickSort();

        resPrint = 6;
    }

    else{
        printf("Algoritmo inválido\n");
        return -1;
    }

    writeCSV(results, resPrint);
    return 0;
}


void writeCSV(float tempos[], int mode)
{   
    string filename;
    switch(mode){
        case 0:
            filename="resShell.txt"; break;
        case 1:
            filename="resHeap.txt"; break;
        case 2:
            filename="resBubble.txt"; break;
        case 3:
            filename="resSelectiontxt"; break;
        case 4:
            filename="resInsertion.txt"; break;
        case 5:
            filename="resMerge.txt"; break;
        case 6:
            filename="resQuick.txt"; break;
        default:
            printf("Não foi possível realizar a operação (numero de algoritmo inválido. Vide comentários)");
            return;
    }

    ofstream res(filename);
        if (!res.is_open()){
            return;
        }else{
            for (int i = 0; i < 5; i++){
                res << tempos[i] << endl;
            }
        }
        res.close();
        return;
    
}
