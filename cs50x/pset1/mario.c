#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height;
    do
    {
        printf("height: ");
        height = GetInt();
    }
    while (height < 0 || height > 23);

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
