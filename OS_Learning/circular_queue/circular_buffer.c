#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/shm.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include "circular_buffer.h"
#include <string.h>
#include <sys/wait.h>

int main(int argc, char* argv[])
{

	int smem_fd;
	char buf_name[] = CIRCULAR_BUF_NAME;
	int child_status;

	smem_fd = shm_open(CIRCULAR_BUF_NAME, O_CREAT | O_RDWR, 0666);
	ftruncate(smem_fd, sizeof(shared_mem_circular_buffer));

	shared_mem_circular_buffer *smem_ptr = 
		(shared_mem_circular_buffer*) mmap(0, sizeof(shared_mem_circular_buffer), PROT_READ | PROT_WRITE, MAP_SHARED, smem_fd, 0);


	memset(smem_ptr, 0, sizeof(shared_mem_circular_buffer));

	int pid = fork();

	if(pid == 0) {
                char consmr_child_name[] = "consumer_0";
                execl("./cbuf_consmr", "cbuf_consmr", consmr_child_name, (char*)0);
	}

	while(wait(&child_status) > 0) {
		printf("Consumer Child Process Finished !!\n");
	}

	return 0;

}
