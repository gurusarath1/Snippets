#include <stdio.h>


typedef struct {
        unsigned int two_bit_num:2;
        int three_bit_num:3;
} struct1;

struct struct1_packed {
        unsigned int two_bit_num:2;
        int three_bit_num:3;
} __attribute__((packed));

typedef struct struct1_packed struct1_packed;

int main() {

        struct1 a;
        struct1_packed b;

        printf("sizeof(int) = %ld\n", sizeof(int));
        printf("sizeof(struct1) = %ld\n", sizeof(struct1));
        printf("sizeof(struct1_packed) = %ld\n", sizeof(struct1_packed));

        // CANNOT TAKE ADDRESS OF BIT FIELD
        //printf("&a.two_bit_num = %p\n", &a.two_bit_num);
        //printf("&a.three_bit_num = %p\n", &a.three_bit_num);
        //printf("&b.two_bit_num = %p\n", &b.two_bit_num);
        //printf("&b.three_bit_num = %p\n", &b.three_bit_num);


        a.two_bit_num = 0;
        a.three_bit_num = 0;
        for(int i=0; i<10; i++) {
                printf("\nunsigned 2bit num = %d\n", a.two_bit_num);
                printf("3bit num = %d\n", a.three_bit_num);
                a.two_bit_num++;
                a.three_bit_num++;
        }

        return 0;
}

/*

sizeof(int) = 4
sizeof(struct1) = 4
sizeof(struct1_packed) = 1

unsigned 2bit num = 0
3bit num = 0

unsigned 2bit num = 1
3bit num = 1

unsigned 2bit num = 2
3bit num = 2

unsigned 2bit num = 3
3bit num = 3

unsigned 2bit num = 0
3bit num = -4

unsigned 2bit num = 1
3bit num = -3

unsigned 2bit num = 2
3bit num = -2

unsigned 2bit num = 3
3bit num = -1

unsigned 2bit num = 0
3bit num = 0

unsigned 2bit num = 1
3bit num = 1


*/
