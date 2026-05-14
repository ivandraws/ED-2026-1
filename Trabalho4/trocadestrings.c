#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct{
    char* data;
}String;

/*void exch(char* a, char* b){

}

*/
void exch(String** vec, int i, int j){
    String* aux = vec[i];
    vec[i] = vec[j];
    vec[j] = aux;
}
void string_init(String* self, const char* data){
   self->data = malloc(strlen(data)+1);
   strcpy(self->data, data); 
}

String* new_string(const char* str){
    int len = strlen(str);
    String* s = malloc(sizeof(String));
    string_init(s,str);
    return s;
}

void delete_string(String* str){
    if(str == NULL) return;
    free(str->data);
    str->data = NULL;
    free(str);
    str = NULL;
}

int string_compare(String* a, String* b){
    return strcmp(a->data, b->data);
}

int string_compare_greater(String* a, String* b){
    return string_compare(a,b) > 0; 
}

int string_compare_lower(String* a, String* b){
    return string_compare(a,b) < 0; 
}

// void string_switch(String** a, String** b){
//     String* aux = a;
//     *a = *b;
//     *b = aux;
// }
int main(){
    // char* strA = malloc(6*sizeof(char));
    // strcpy(strA, "amigo");
    
    // char* strB = malloc(6*sizeof(char));
    // strcpy(strB, "feliz");

    // char* aux = strA;
    // strA = strB;
    // strB = aux;

    // String* teste = new_string("abacate");
    // String* teste2 = new_string("banana");
    String* vec[3];
    vec[0] = new_string("abacate");
    vec[1] = new_string("banana");
    vec[2] = new_string("uva");

    exch(vec,0,1);
    for(int i = 0; i<3; i++)
        printf("%s\n", vec[i]->data);
    //printf("%d\n", string_compare(teste, teste2));
    //printf("%s %s\n", strA, strB);

    return 0;
}