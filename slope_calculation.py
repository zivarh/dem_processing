
"""
This script calculates the maximum slope for each row and column (pixel) of the raster by considering all
the slopes between the pixel and the 8 nearest pixels. And use additional algorithm for edge pixels.
"""
import numpy as np # importing numpy library as np for easily working with provided data
def calculate_max_slopes(raster):
    #dimension calculatio of the input raster image.
    rows, cols = raster.shape
    '''
    rows - number of dimensions
    cols- number of elements in each dimension
    '''
    # new array initialisation for storing maximum slope values for each pixel
    max_slopes = np.zeros_like(raster)
    '''
    np.zeros_like(raster) return an array of zeros with the same shape and type as a given array in our case raster.
    '''
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            '''
            range(1, col-1) used to skip border rows anc cols as they dont have 8 neighbours
            '''
            # calculate slope between pixel and its 8 neighbors
            slopes = []
            for k in [-1, 0, 1]:
                for l in [-1, 0, 1]:
                    if k == 0 and l == 0:
                        continue
                    '''
                    For each pixel, the code calculates the slope between the pixel and its 8 neighboring pixels using the nested loops for 
                    k in [-1, 0, 1]: and for l in [-1, 0, 1] 
                    The if k == 0 and l == 0: continue statement skips the calculation of the slope between the pixel and itself.
                    '''
                    i_neighbor = i + k
                    j_neighbor = j + l
                    if i_neighbor < 0 or i_neighbor >= rows or \
                    j_neighbor < 0 or j_neighbor >= cols:
                        # neighbor is outside the map boundary
                        continue
                    '''
                    The other condition if i_neighbor < 0 or i_neighbor >= rows or j_neighbor < 0 or j_neighbor >= cols: checks if 
                    the neighboring pixel is outside the map boundary. In such cases, the slope calculation is also skipped
                    '''
                    rise = raster[i][j] - raster[i_neighbor][j_neighbor]
                    run = np.sqrt(k**2 + l**2)
                    if run == 0:
                        # avoid division by zero
                        continue
                    slope = np.arctan(rise / run)

                    '''
                    for each valid neighboring pixel, the rise and run are calculated, which are used to calculate the slope using the 
                    arctangent function np.arctan(rise / run).
                    '''
                    #and resut added to slopes array
                    slopes.append(slope)

            # calculate maximum slope
            max_slope = np.max(slopes) if slopes else 0
            
            '''
            For edge pixels, the code takes a slightly different approach to calculate the maximum slope value. 
            It finds the maximum slope value in a 3x3 neighborhood centered around the edge pixel 
            '''
            # calculation of the maximum slope for edge pixels
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                start_i = max(0, i-1)
                end_i = i+2
                start_j = max(0, j-1)
                end_j = j+2
                max_edge_slope = np.max(max_slopes[start_i:end_i, start_j:end_j])
                max_slope = max(max_slope, max_edge_slope)
            '''
            The if statement checks whether the current pixel is on the edge of the raster. If it is, then the maximum slope for 
            that pixel is potentially affected by the surrounding pixels outside of the raster, and the code takes that into account.

            The rest part of the code slices a 3x3 subarray from max_slopes that includes the current pixel and its 8 
            neighbors. The max function is used to ensure that the indices of the subarray are not negative.

            np.max() is then used to find the maximum slope within this subarray.

            Finally, the calculated maximum slope of the surrounding pixels is compared to the maximum slope previously calculated for the 
            current pixel, and the greater of the two values is assigned to max_slope. 
            '''
            # set the maximum slope for the current pixel in the max_slopes array and updates the max_slopes array with the new maximum slope value
            max_slopes[i][j] = max_slope 
    
    return max_slopes     

