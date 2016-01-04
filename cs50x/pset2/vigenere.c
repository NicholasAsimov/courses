/* 
File: vigenere.c
Name: Nicholas Asimov
Date: 04/01/16 (dd/mm/yy)
Course: CS50: Introduction to Computer Science
Desc: Program encrypts a message using vigenere cipher with given key.
Usage: The program reads alphabetical key from a command-line argument, 
        then asks user for an input and prints out encrypted text.
*/

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    
    string k = argv[1];
    
    // Making sure there's only 2 arguments (program name and key)
    if (argc != 2)
    {
        printf("Usage: %s key\n", argv[0]);
        return 1;
    }
    
    for (int i = 0, n = strlen(k); i < n; i++)
    {
        if (!isalpha(k[i]))
        {
            printf("Found non-alphabetical characters, aborting..\n");
            return 1;
        }
    }
    
    string p = GetString(); // Text to encrypt
    
    // Initializing loop to cycle through key word
    // ki = iterator for key
    // kn = length of key
    // kch = key character for current iteration
    for (int i = 0, n = strlen(p), kn = strlen(k), ki = 0; i < n; i++)
    {
        int kch = k[ki % kn] - 'a';
        
        if (isalpha(p[i]) && isupper(p[i]))
        {
            printf("%c", ((p[i] - 'A' + kch) % 26) + 'A');
            ki++;
        }
        else if (isalpha(p[i]) && islower(p[i]))
        {
            printf("%c", ((p[i] - 'a' + kch) % 26) + 'a');
            ki++;
        }
        else
        {
            printf("%c", p[i]);
        }
    }
    
    printf("\n");
    return 0;
}