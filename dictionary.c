// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;
unsigned int wordcounter = 0;
// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // to get hash value
    int hashnumber = hash(word);

    node *iterate;

    iterate = table[hashnumber];

    while (iterate != NULL)
    {
        if (strcmp(iterate -> word, word) == 0)
        {
            return true;
        }

        iterate = iterate -> next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // To open the dictionary file
    FILE *wordfile = fopen(dictionary, "r");

    if (wordfile == NULL)
    {
        return 0;
    }

    // To scan the dictionary and making a hash table
    char txt[LENGTH + 1];
    while (fscanf(wordfile, "%s", txt) != EOF)
    {
        node *tmp = malloc(sizeof(node));

        if (tmp == NULL)
        {
            return 0;
        }

        strcpy(tmp -> word, txt);

        int hashnumber = hash(txt);

        tmp -> next = table[hashnumber];
        table[hashnumber] = tmp;

        wordcounter ++;

    }


    fclose(wordfile);
    return true;

}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // return total number of words in dictionary
    return wordcounter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *iterate = table[i];
        
        while (iterate != NULL)
        {
            node *tmp = iterate;
            iterate = iterate -> next;
            free(tmp);
        }
        
        if (iterate == NULL && i == N - 1)
        {
            return true;
        }
    }
    return false;
}
