/**
 * helpers.c
 *
 * Computer Science 50
 * Problem Set 3
 *
 * Helper functions for Problem Set 3.
 */
       
#include <cs50.h>

#include "helpers.h"

//prototype
int binarySearch(int key, int array[], int min, int max);

/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int values[], int n)
{
    int isFound = binarySearch(value, values, 0, n-1);
    
    if (isFound != -1)
        return true;
    else
        return false;
}

/**
 * Returns index of value in array if found else -1.
 * int max - last index of array e.g. array with 5 elements: int max = 4
 */
int binarySearch(int key, int array[], int min, int max)
{
    if (max < min)
    {
        return -1;
    }
    else
    {
        int midpoint = (max + min) / 2;
    
        if (array[midpoint] < key)
        {
            return binarySearch(key, array, midpoint + 1, max);
        }
        else if (array[midpoint] > key)
        {
            return binarySearch(key, array, min, midpoint - 1);
        }
        else
            return midpoint;
    }
    
    return -1;
}

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    // bubble sort
    int temp;
    
    for (int j = 1; j < n; j++)
    {
        for (int i = 0; i < n-1; i++)
        {
            if (values[i] > values[i+1])
            {
                temp = values[i];
                values[i] = values[i+1];
                values[i+1] = temp;
            }
        }
    }
    
    return;
}