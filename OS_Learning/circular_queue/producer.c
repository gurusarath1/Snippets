#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/shm.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include "circular_buffer.h"

int main(int argc, char* argv[])
{
	int smem_fd = shm_open(CIRCULAR_BUF_NAME, O_RDWR, 0666);


	shared_mem_circular_buffer *smem_ptr = (shared_mem_circular_buffer*) mmap(0, sizeof(shared_mem_circular_buffer), PROT_READ | PROT_WRITE, MAP_SHARED, smem_fd, 0);

	for(int i=1; i<argc; i++) {
		while( ((smem_ptr->in + 1) % BUF_ARRAY_SIZE) == smem_ptr->out );

		int value = atoi(argv[i]);
		printf("Producer: {%d}Adding %d to the buffer\n", i, value);
		smem_ptr->circular_buffer[smem_ptr->in].value = value;
		smem_ptr->in = (smem_ptr->in + 1) % BUF_ARRAY_SIZE;
	}


	return 0;
}
