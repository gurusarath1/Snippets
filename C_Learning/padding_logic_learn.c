#include <stdio.h>

typedef struct {
    char x; //--> byte 1
    char x2; //--> byte 2
    // --> 2 bytes pad (byte 3,4)
    int y; //--> byte 5,6,7,8
    
} typea;

typedef struct {
    int x; // --> byte 1,2,3,4
    char y; // --> byte 5
    char y2; // --> byte 6
    // --> 2 byte pad (byte 7,8)
    
} typeb;

typedef struct {

    char y; // --> byte 1
    // --> byte 2,3,4
    int x; // --> byte 5,6,7,8
    char y2; // --> byte 9
    // --> pad 10,11,12
    
} typec;


typedef struct {

    char y; // --> byte 1
    // --> pad byte 2,3,4,5,6,7,8
    double x; // --> byte 9,10,11,12,13,14,15,16
    char y2; // --> byte 17
    // --> byte 18,19,20,21,22,23,24
    
} typed;


typedef struct {
    
    char x; // --> byte 1
    // --> pad byte 2,3,4,5,6,7
    typed y; // +24 = 32 bytes
    
} typee;


int main()
{
    printf("\n%d %d %d %d %d\n", sizeof(typea), sizeof(typeb),
                                 sizeof(typec), sizeof(typed), sizeof(typee));
    // 8 8 12 24 32

    return 0;
}
