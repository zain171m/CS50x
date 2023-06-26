#include "helpers.h"
#include <math.h>
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int r = 0; r < width; r++)
    {
        for (int c = 0; c < height; c++)
        {   
            // Calculate Average 
            float average = (image[r][c].rgbtRed + image[r][c].rgbtGreen + image[r][c].rgbtBlue) / 3.00;
            int ave = round(average);
            // Assigning color values to pixels
            image[r][c].rgbtRed = ave;
            image[r][c].rgbtGreen = ave;
            image[r][c].rgbtBlue = ave;
        }
    }
    return;
}

// Swap Function to Reflect image
void swap(RGBTRIPLE *pixel1, RGBTRIPLE *pixel2)
{
    RGBTRIPLE temp = *pixel1;
    *pixel1 = *pixel2;
    *pixel2 = temp;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int temp[3];
    for (int r = 0; r < height; r++)
    {
        for (int c = 0; c < (width / 2); c++)
        {
            swap(&image[r][c], &image[r][width - 1 - c]);
        }
        
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    //temporary image to implement blur
    RGBTRIPLE temp[height][width];
    
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int totalred, totalgreen, totalblue;
            totalred = totalgreen = totalblue = 0;
            float counter = 0.00;
            
            //Get the Neighbhouring pixels
            for (int di = -1; di < 2; di++)
            {
                for (int dj = -1; dj < 2; dj++)
                {
                    int I = i + di;
                    int J = j + dj;
                    
                    //Check the valid pixel
                    if (I < 0 || I > (height - 1) || J < 0 || J > (width - 1))
                    {
                        continue;
                    }

                    //Get value of the image
                    totalred += image[I][J].rgbtRed;
                    totalgreen += image[I][J].rgbtGreen;
                    totalblue += image[I][J].rgbtBlue;
                    
                    counter ++;
                }
                /* Average the all possible pixel,s values 
                and Calculate color values for blurred pixel */
                temp[i][j].rgbtRed = round(totalred / counter);
                temp[i][j].rgbtGreen = round(totalgreen / counter);
                temp[i][j].rgbtBlue = round(totalblue / counter);
            }
        }
        
    }
    //copy blur image to the original one
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = temp[i][j].rgbtRed;
            image[i][j].rgbtGreen = temp[i][j].rgbtGreen;
            image[i][j].rgbtBlue = temp[i][j].rgbtBlue;
        } 
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    //temporary image to implement Detect Edges filter
    RGBTRIPLE temp[height][width];
    
    // Initialise Sobel arrays
    int gx[3][3] = {{-1, 0, 1}, {-2, 0, 2}, {-1, 0, 1}};
    int gy[3][3] = {{-1, -2, -1}, {0, 0, 0}, {1, 2, 1}};

    
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int gxRed = 0;
            int gxGreen = 0;
            int gxBlue = 0;
            int gyRed = 0;
            int gyGreen = 0;
            int gyBlue = 0;
            //Get the Neighbhouring pixels
            for (int r = -1; r < 2; r++)
            {
                for (int c = -1; c < 2; c++)
                {
                    
                    //Check the valid pixel
                    if (i + r < 0 || i + r > height - 1)
                    {
                        continue;
                    }
                    if (j + c < 0 || j + c > width - 1)
                    {
                        continue;
                    }

                    // Otherwise add to sums
                    gxBlue += image[i + r][j + c].rgbtBlue * gx[r + 1][c + 1];
                    gyBlue += image[i + r][j + c].rgbtBlue * gy[r + 1][c + 1];
                    gxGreen += image[i + r][j + c].rgbtGreen * gx[r + 1][c + 1];
                    gyGreen += image[i + r][j + c].rgbtGreen * gy[r + 1][c + 1];
                    gxRed += image[i + r][j + c].rgbtRed * gx[r + 1][c + 1];
                    gyRed += image[i + r][j + c].rgbtRed * gy[r + 1][c + 1];
                   
                }
              
            }
            // Calculate Sobel operator
            int blue = round(sqrt(gxBlue * gxBlue + gyBlue * gyBlue));
            int green = round(sqrt(gxGreen * gxGreen + gyGreen * gyGreen));
            int red = round(sqrt(gxRed * gxRed + gyRed * gyRed));
            
            // Assign new values to pixels
            temp[i][j].rgbtBlue = (blue > 255) ? 255 : blue;
            temp[i][j].rgbtGreen = (green > 255) ? 255 : green;
            temp[i][j].rgbtRed = (red > 255) ? 255 : red;
        }    
         
    }
    //copy Edge highlited image to the original one
    for (int x = 0; x < height; x++)
    {
        for (int y = 0; y < width; y++)
        {
            image[x][y].rgbtRed = temp[x][y].rgbtRed;
            image[x][y].rgbtGreen = temp[x][y].rgbtGreen;
            image[x][y].rgbtBlue = temp[x][y].rgbtBlue;
        } 
    }
    
    return;
}

