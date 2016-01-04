/* 
File: caesar.c
Name: Nicholas Asimov
Date: 03/01/16 (dd/mm/yy)
Course: CS50: Introduction to Computer Science
Desc: Program encrypts a message using caesar cipher with given key.
Usage: The program reads numerical key from a command-line argument, 
        then asks user for an input and prints out encrypted text.
*/

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s key\n", argv[0]);
        return 1;
    }
    
    int k = atoi(argv[1]);
    string p = GetString();
    
    for (int i = 0, n = strlen(p); i < n; i++)
    {
        if (isalpha(p[i]) && isupper(p[i]))
        {
            printf("%c", ((p[i] - 'A' + k) % 26) + 'A');
        }
        else if (isalpha(p[i]) && islower(p[i]))
        {
            printf("%c", ((p[i] - 'a' + k) % 26) + 'a');
        }
        else
        {
            printf("%c", p[i]);
        }
    }
    
    printf("\n");
    return 0;
}