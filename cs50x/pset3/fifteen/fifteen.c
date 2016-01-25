/**
 * fifteen.c
 *
 * Computer Science 50
 * Problem Set 3
 *
 * Implements Game of Fifteen (generalized to d x d).
 *
 * Usage: fifteen d
 *
 * whereby the board's dimensions are to be d x d,
 * where d must be in [DIM_MIN,DIM_MAX]
 *
 * Note that usleep is obsolete, but it offers more granularity than
 * sleep and is simpler to use than nanosleep; `man usleep` for more.
 */
 
#define _XOPEN_SOURCE 500

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

// constants
#define DIM_MIN 3
#define DIM_MAX 9

// board
int board[DIM_MAX][DIM_MAX];

// dimensions
int d;

// global vars for user chosen tile and blank tile coordinates
int tile_row;
int tile_col;
int blank_row;
int blank_col;

// prototypes
void clear(void);
void greet(void);
void init(void);
void draw(void);
bool move(int tile);
bool won(void);
bool tile_search(int tile);
bool legal_move(void);

int main(int argc, string argv[])
{
    // ensure proper usage
    if (argc != 2)
    {
        printf("Usage: fifteen d\n");
        return 1;
    }

    // ensure valid dimensions
    d = atoi(argv[1]);
    if (d < DIM_MIN || d > DIM_MAX)
    {
        printf("Board must be between %i x %i and %i x %i, inclusive.\n",
            DIM_MIN, DIM_MIN, DIM_MAX, DIM_MAX);
        return 2;
    }
    else
    {
        blank_row = d - 1;
        blank_col = d - 1;
    }

    // open log
    FILE* file = fopen("log.txt", "w");
    if (file == NULL)
    {
        return 3;
    }

    // greet user with instructions
    greet();

    // initialize the board
    init();

    // accept moves until game is won
    while (true)
    {
        // clear the screen
        clear();

        // draw the current state of the board
        draw();

        // log the current state of the board (for testing)
        for (int i = 0; i < d; i++)
        {
            for (int j = 0; j < d; j++)
            {
                fprintf(file, "%i", board[i][j]);
                if (j < d - 1)
                {
                    fprintf(file, "|");
                }
            }
            fprintf(file, "\n");
        }
        fflush(file);

        // check for win
        if (won())
        {
            printf("ftw!\n");
            break;
        }

        // prompt for move
        printf("Tile to move: ");
        int tile = GetInt();
        
        // quit if user inputs 0 (for testing)
        if (tile == 0)
        {
            break;
        }

        // log move (for testing)
        fprintf(file, "%i\n", tile);
        fflush(file);

        // move if possible, else report illegality
        if (!move(tile))
        {
            printf("\nIllegal move.\n");
            usleep(500000);
        }

        // sleep thread for animation's sake
        usleep(500000);
    }
    
    // close log
    fclose(file);

    // success
    return 0;
}

/**
 * Clears screen using ANSI escape sequences.
 */
void clear(void)
{
    printf("\033[2J");
    printf("\033[%d;%dH", 0, 0);
}

/**
 * Greets player.
 */
void greet(void)
{
    clear();
    printf("WELCOME TO GAME OF FIFTEEN\n");
    usleep(200); // old: 2000000
}

/**
 * Initializes the game's board with tiles numbered 1 through d*d - 1
 * (i.e., fills 2D array with values but does not actually print them).  
 */
void init(void)
{
    int c = 1;
    for (int row = 0; row < d; row++)
    {
        for (int col = 0; col < d; col++)
        {
            board[row][col] = d*d - c;
            c++;
        }
    }
    
    // swap 1 and 2 tile if the board contains an odd number of tiles
    if (d % 2 == 0)
    {
        int temp = board[d - 1][d - 2];
        board[d - 1][d - 2] = board[d - 1][d - 3];
        board[d - 1][d - 3] = temp; 
    }
}

/**
 * Prints the board in its current state.
 */
void draw(void)
{
    for (int row = 0; row < d; row++)
    {
        for (int col = 0; col < d; col++)
        {
            // print the board except the 0 tile
            if (board[row][col] > 0)
            {
                // different formatting for double and single digit numbers 
                // for proper alignment
                if (board[row][col] < 10)
                    printf("|  %i ", board[row][col]);
                else
                    printf("| %i ", board[row][col]);
            }
            
            // print underscore instead of 0
            if (board[row][col] == 0)
                printf("|  _ ");
        }
        
        printf("|\n\n");
    }
    
}

/**
 * If tile borders empty space, moves tile and returns true, else
 * returns false. 
 */
bool move(int tile)
{
    if (tile_search(tile) && legal_move())
    {
        // swap user chosen tile and blank tile
        int temp_row = tile_row;
        int temp_col = tile_col;
        int temp = board[tile_row][tile_col];
        
        board[tile_row][tile_col] = board[blank_row][blank_col];
        board[blank_row][blank_col] = temp;
        
        blank_row = temp_row;
        blank_col = temp_col;

        return true;
    }
    
    return false;
}

/**
 * Returns true if game is won (i.e., board is in winning configuration), 
 * else false.
 */
bool won(void)
{
    int n = 1;
    
    for (int row = 0; row < d; row++)
    {
        for (int col = 0; col < d; col++)
        { 
            if (board[row][col] == n)
            {
                n++;
                if (n == d*d && board[d-1][d-1] == 0)
                {
                    return true;
                }
            }
        }
    }
    
    return false;
}

/**
 * Returns true if tile is found, 
 * else false.
 */
bool tile_search(int tile)
{
    // search for the tile
    for (int row = 0; row < d; row++)
    {
        for (int col = 0; col < d; col++)
        { 
            if (board[row][col] == tile)
            {
                tile_row = row;
                tile_col = col;
                
                return true;
            }
        }
    }
    
    return false;
}

/**
 * Returns true if the move is legal (i.e., there's a blank space around the tile), 
 * else false.
 */
bool legal_move(void)
{
    if (tile_row > 0 && board[tile_row - 1][tile_col] == 0) // check up
        return true;
    else if (tile_col < d-1 && board[tile_row][tile_col + 1] == 0) // check right
        return true;
    else if (tile_row < d-1 && board[tile_row + 1][tile_col] == 0) // check down
        return true;
    else if (tile_col > 0 && board[tile_row][tile_col - 1] == 0) // check left
        return true;
    
    return false;
}