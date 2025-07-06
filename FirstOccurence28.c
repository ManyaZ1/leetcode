#include <string.h>
int strStr(char* haystack, char* needle) {
    char*pos_ptr;
    pos_ptr=strstr(haystack, needle);
    if (pos_ptr == NULL){
        return -1;}
    //printf("%p",haystack);
    else{
            return (pos_ptr-haystack);
    }
}
