#include <stdio.h>
#include <cs50.h>

int main(void)
{
    printf("minutes: ");
    int mins = GetInt();
    
    printf("bottles: %i\n", 192 * mins / 16);
}