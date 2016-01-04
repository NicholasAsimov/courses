/* 
File: initials.c
Name: Nicholas Asimov
Date: 02/01/16 (dd/mm/yy)
Course: CS50: Introduction to Computer Science
Desc: Program prints out initials of given name.
Usage: The program asks user for an input and prints out uppercase letters
        of each word.
*/

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    string name = GetString();
    printf("%c", toupper(name[0]));
    
    for (int i = 0, n = strlen(name); i < n; i++)
    {
        if (name[i] == ' ')
        {
            printf("%c", toupper(name[i+1]));
        }
    }
    
    printf("\n");
}