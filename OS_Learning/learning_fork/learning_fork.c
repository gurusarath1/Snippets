#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>


int main()
{

	pid_t pid;
	int child_exit_status;

	for(int child_idx=0; child_idx<5; child_idx++) {

		pid = fork();

		if(pid < 0) {
			fprintf(stderr, "Fork Failed !!");
		} else if(pid == 0) {

			char child_name[3] = {'c','0' + child_idx, '\0'};

			execl("./chd_p", "chd_p", child_name, (char*)0);
			printf("\n%s Child process exit ..\n", child_name);
			exit(2);
		}

	}

	while(pid > 0) { // Wait for all the child processes to exit

		printf("\nThis is form parent process child pid = %d", pid);
		printf("\nParent waiting ... ");
		pid = wait(&child_exit_status);
		printf("\nChild exit detected - pid %d status %d\n", pid, WEXITSTATUS(child_exit_status) );
	}

	return 0;
}
