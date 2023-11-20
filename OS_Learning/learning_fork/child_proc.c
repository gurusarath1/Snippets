#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

	printf("We are inside child process %s !!\n", argv[1]);

	for(int i=0; i<10; i++) {
		printf("child %s   i = %d\n", argv[1], i);
	}

	exit(69);

	return 3;
}
