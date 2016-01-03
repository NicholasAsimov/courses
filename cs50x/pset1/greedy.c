#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    float dollars;
    do
    {
        printf("O hai! How much change is owed?\n");
        dollars = GetFloat();
    }
    while (dollars < 0.0);
    
    int cents = round(dollars * 100);
    int coins = 0;

    while (cents > 0)
    {
        if (cents / 25)
        {
            cents -= 25;
            coins++;
            continue;
        }
        else if (cents / 10)
        {
            cents -= 10;
            coins++;
            continue;
        }
        else if (cents / 5)
        {
            cents -= 5;
            coins++;
            continue;
        }
        else if (cents / 1)
        {
            cents -= 1;
            coins++;
        }
    }
    
    printf("%i\n", coins);
}