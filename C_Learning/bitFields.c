#include <stdio.h>
#include <stdint.h>

typedef struct bit_valus {

    unsigned int a:1;
    unsigned int b:2;
    unsigned int c:3;

} bit_vals;

struct bit_valus2 {

    unsigned int a:1;
    unsigned int b:2;
    unsigned int c:3;

} __attribute__((packed));

typedef struct bit_valus2 bit_valus2;

uint8_t bitArray;

#define SET_BIT(BF,N) (BF |= ((uint64_t)0x1 << N))
#define CLR_BIT(BF,N) (BF &= ~((uint64_t)0x1 << N))
#define IS_BIT_SET(BF,N) ((BF >> N) & 0x1)


int main() {

    bit_vals x;
    bit_valus2 x2;

    printf("Size of x = %d\n", sizeof(x));
    printf("Size of x2 = %d\n", sizeof(x2));

    

    x.a = 0;
    x.b = 0;
    x.c = 0;

    for(int i=0; i<15; i++) {

        printf("%d %d %d\n", x.a, x.b, x.c);
        x.a++;
        x.b++;
        x.c++;

    }

    /*
    0 0 0
    1 1 1
    0 2 2
    1 3 3
    0 0 4
    1 1 5
    0 2 6
    1 3 7
    0 0 0
    1 1 1
    0 2 2
    1 3 3
    0 0 4
    1 1 5
    0 2 6
    */

   SET_BIT(bitArray, 0);
   SET_BIT(bitArray, 1);
   SET_BIT(bitArray, 2);

   printf("\n%d", bitArray);

   CLR_BIT(bitArray, 2);

   printf("\n%d", bitArray);

    // ----------------------------------------------------

   int8_t varX;
   varX = 0b10000000; // -128

   printf("\n%d", varX);  // -128

   varX = varX >> 1;

   printf("\n%d", varX); //-64 or 0b11000000

   // ---------------------------------------------------

   uint8_t varX2;
   varX2 = 0b10000000; // 128

   printf("\n%d", varX2);  // 128

   varX2 = varX2 >> 1;

   printf("\n%d", varX2); //64 or 0b01000000


    return 0;
}