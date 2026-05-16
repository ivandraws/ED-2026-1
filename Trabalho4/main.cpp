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
void selection()
        {
            int interact = 0;
            int min;
            while (interact < index)
            {
                //printf("Interacao %i\n", interact);
                min = interact;
                for (int i = interact + 1; i < size ; i++)
                {   
                    if (lessthan(i, min))
                    {
                        min = i;
                    }
                }
                exch(min, interact);

                interact++;
            }
    /*
    for (int i = 0; i < size; i++)
    {
        printf("%i\n", conj[i]);
    }
    */
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
    //apenas testes, remover depois
    
    if (agrc != 3)
    {
        cout << "Usage ./main (nomedoarquivo.txt) (algoritmo)" << endl;
        return -1;
    }
    char* mode = argv[2];
    float res[5];
    name_Vector vector[5] = {
        read_name_file("nomes100kmin.txt")
    };
    name_Vector vector5 = read_name_file("nomes100kmin.txt");

    
    int shellMode = strcmp(mode, "sh"); // 0
    int heapMode = strcmp(mode, "he"); // 1
    int bubbleMode = strcmp(mode, "bu"); // 2
    int selectionMode = strcmp(mode, "se"); // 3
    int insertionMode = strcmp(mode, "in"); // 4
    int mergeMode = strcmp(mode, "me"); // 5
    int quickMode = strcmp(mode, "qu"); // 6
    int resPrint;
    clock_t timeReq;
    timeReq = clock();
    if (shellMode == 0)
    {
        for (int i = 0; i < 5; i++)
        {
            timeReq = clock() - timeReq;
            vector[i].shellsort();
            timeReq = clock() - timeReq;
            float tempo = (float)timeReq/CLOCKS_PER_SEC;
            printf("Progama demorou %f segundos para organizar em shellsort\n",tempo);
            res[i] = tempo;
        }
        resPrint = 0;
    }
    else if (heapMode == 0) 
    {
        resPrint = 1;
    }
    else if (bubbleMode == 0)
    {
        resPrint = 2;
    }
    else if (selectionMode == 0)
    {
        for (int i = 0; i < 5; i++)
        {
            timeReq = clock() - timeReq;
            vector[i].selection();
            timeReq = clock() - timeReq;
            float tempo = (float)timeReq/CLOCKS_PER_SEC;
            printf("Progama demorou %f segundos para organizar em selection sort\n",tempo);
            res[i] = tempo;
        }
        resPrint = 3;
    }
    else if (insertionMode == 0)
    {
        resPrint = 4;
    }
    else if (mergeMode == 0)
    {
        resPrint = 5;
    }
    else if (quickMode == 0)
    {
        resPrint = 6;
    }
    else
    {
        printf("Nenhum algoritmo similar ao do argumento de linha de comando\n");
    }
    
    writeCSV(res, resPrint);
    return 0;
}


void writeCSV(float tempos[], int mode)
{
    
    if (mode == 0){
        ofstream res("resShell.txt");
        if (!res.is_open())
        {
            return;
        }
        else
        {
            for (int i = 0; i < 5; i++)
            {
                res << tempos[i] << endl;
            }
        }
        res.close();
        return;
    }
    else if (mode == 1){
        ofstream res("resHeap.txt");
        if (!res.is_open())
        {
            return;
        }
        else
        {
            for (int i = 0; i < 5; i++)
            {
                res << tempos[i] << endl;
            }
        }

        res.close();
        return;
    }
    else if (mode == 2){
        ofstream res("resBubble.txt");
        if (!res.is_open())
        {
            return;
        }
        else
        {
            for (int i = 0; i < 5; i++)
            {
                res << tempos[i] << endl;
            }
        }
        res.close();
        return;
    }
    else if (mode == 3){
        ofstream res("resSelect.txt");
        if (!res.is_open())
        {
            return;
        }
        else
         {
            for (int i = 0; i < 5; i++)
            {
                res << tempos[i] << endl;
            }
        }
        res.close();
        return;
    }
    else if(mode == 4){
        ofstream res("resInsert.txt"); 
        if (!res.is_open())
        {
            return;
        }
        else
        {
            for (int i = 0; i < 5; i++)
            {
                res << tempos[i] << endl;
            }
        }
        res.close();
        return;
    }
    else if (mode == 5){
        ofstream res("resMerge.txt");
        if (!res.is_open())
        {
            return;
        }
        else
        {
            for (int i = 0; i < 5; i++)
            {
                res << tempos[i] << endl;
            }
        }
        res.close();
        return;
    }
    else if (mode == 6){
        ofstream res("resQuick.txt");
        if (!res.is_open())
        {
            return;
        }
        else
        {
            for (int i = 0; i < 5; i++)
            {
                res << tempos[i] << endl;
            }
        }
        res.close();
        return;
    }
    else{
        printf("Não foi possível realizar a operação (numero de algoritmo inválido. Vide comentários)");
        return;
    }
    
}