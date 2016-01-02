#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height = -1;
    
    while (height < 0 || height > 23)
    {
        printf("height: ");
        height = GetInt();
    }
    
    for (int row = 0; row < height; row++)
    {
        for (int space = 1; space < height - row; space++)
        {
            printf(" ");
        }
        
        for (int hash = 0; hash < row; hash++)
        {
            printf("#");
        }
            
        printf("##\n");
    }
}