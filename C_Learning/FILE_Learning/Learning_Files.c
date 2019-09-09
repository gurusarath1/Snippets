// File created on 9th September 2019
// Created by Guru Sarath

#include <stdio.h>

int main()
{

    /*
    Different modes of opening a file

    “r” – Searches file. If the file is opened successfully fopen( ) loads it into memory and sets up a pointer which points to the first character in it. If the file cannot be opened fopen( ) returns NULL.
    “w” – Searches file. If the file exists, its contents are overwritten. If the file doesn’t exist, a new file is created. Returns NULL, if unable to open file.
    “a” – Searches file. If the file is opened successfully fopen( ) loads it into memory and sets up a pointer that points to the last character in it. If the file doesn’t exist, a new file is created. Returns NULL, if unable to open file.
    “r+” – Searches file. If is opened successfully fopen( ) loads it into memory and sets up a pointer which points to the first character in it. Returns NULL, if unable to open the file.
    “w+” – Searches file. If the file exists, its contents are overwritten. If the file doesn’t exist a new file is created. Returns NULL, if unable to open file.
    “a+” – Searches file. If the file is opened successfully fopen( ) loads it into memory and sets up a pointer which points to the last character in it. If the file doesn’t exist, a new file is created. Returns NULL, if unable to open file.
    */

    FILE *filePointer;
    char charX;
    char charBuffer[200]; // max size of a line possible is 200
    char TextToWrite[] = "Howdy !! Welcome, this text will be written to the file";
    char TextToAppend[] = "Howdy !! Welcome, this text will be appended to the file\nThanks and Gig \'em\n";

    if ( (filePointer = fopen("TestReadFile.txt", "r")) != NULL )
    {
        // Reading one character at a time till end of line is reached.
        while(fscanf(filePointer, "%c", &charX) != EOF) // fscanf returns EOF when end of line is reached
        {
            printf("%c", charX);
        }
        fclose(filePointer);

        printf("\n\nFile closed --------------------------\n\n");

    }


    if ( (filePointer = fopen("TestReadFile.txt", "r")) != NULL )
    {
        // Reading one line at time till end of file is reached
        while(fgets(charBuffer, 200, filePointer) != NULL) // fgets returns NULL when end of file is reached
        {
            printf("%s", charBuffer);
        }
        fclose(filePointer);
        printf("\n\nFile closed --------------------------\n\n");

    }


    if ( (filePointer = fopen("TestWriteFile.txt", "w")) != NULL )
    {
        fprintf(filePointer, "%s", TextToWrite);
        fclose(filePointer);
        printf("\n\nWrite Complete - File closed --------------------------\n\n");

    }


    if ( (filePointer = fopen("TestAppendFile.txt", "a")) != NULL )
    {
        fprintf(filePointer, "%s", TextToAppend);
        fclose(filePointer);
        printf("\n\nAppend Complete - File closed --------------------------\n\n");

    }



    return 0;
}
