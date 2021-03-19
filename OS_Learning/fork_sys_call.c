#include <stdio.h>
#include <unistd.h>

int main() {

        /*
         * Fork - Used to create a process
         *
         *  returns
         *  0 - return seen from child
         *  +ve - return value in parent process
         *  -ve - Error
         */

        int PID = fork();

        if(PID != 0) {

                printf("Parent Process !!\nChild Process ID = %d\n", PID);

        } else {

                printf("Child Process !! PID = %d\n", PID);
        }


        return 0;

}
