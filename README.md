
## License

[MIT](https://choosealicense.com/licenses/mit/)
License

Copyright (c) [2023] [Zivar Hagverdiyeva]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction. 


# Digital Elevation Model Processing



## Introduction
A digital elevation model (DEM) is a digital illustration of the elevation of the ground surface considering any referencing datum (Balasubramanian, 2017). DEM is deemed the simplest form of digital terrain representation (Balasubramanian, 2017). DEM is frequently used to refer to any digital model of a topographic surface for various applications. In this project, DEM is used by the demand of the extreme sports holiday company to find suitable extreme gradients for sports activities by calculating the th maximum slope at each pixel (columns and rows) of the dataset. For this, a 2D raster data set of elevations above sea level of the area is given.

This project aims to develop a Python program that contains two scripts. The first script should calculate the maximum slope for each row and column (pixel) of the raster by considering all the slopes between the pixel and the eight nearest pixels and utilising an additional algorithm for edge pixels.
The second main script should provide a graphical user interface (GUI). It should allow the user to select any text file in a suitable format to illustrate the raster, calculate the maximum slope, provide locations with the maximum slope, and display them on the map. Additionally, it creates a new text file that saves the maximum slopes in the same format as the provided raster data.

## Implementation

The software is implemented by using Python and the following libraries:

- [NumPy](https://www.w3schools.com/python/numpy/default.asp): for loading and operating the raster data 
- [Matplotlib Pyplot](https://www.w3schools.com/python/matplotlib_pyplot.asp): for visualizing the maximum slope array
The implementation is divided into two main parts:

    1. Calculation of maximum slopes
    2. Visualization of raster, maximum slope map, locations of extremas

### Data Loading
The program provides a graphical user interface (GUI) that allows the user to select a text file containing the raster data. The GUI was implemented using the Tkinter library, which is a standard Python library for creating GUI applications. The __load_raster_data()__ function uses the filedialog module from Tkinter to open a file dialogue and allows the user to select a file. If the user selects a file, the function reads the data from the file using the __np.loadtxt()__ function from the NumPy library and returns it as a NumPy array. If the user doesn't select any file, the function returns None.

### Maximum Slope Calculation
The module slope_calculation.py defines a function calculate_max_slopes() that takes in a two-dimensional NumPy array representing a raster and returns a NumPy array of the same shape containing the maximum slope for each pixel of the input raster. The function uses a nested loop to iterate over each pixel in the raster and calculates the slope between that pixel and each of its eight nearest neighbours. For each pixel, calculate the slope between the pixel and its eight neighbours using the formula 

__slope = arctan(rise/run)__

where the ___rise___ is the difference in elevation between the pixel and its neighbour, and the ___run___ is the distance between the pixel and its neighbour (Humboldt State University, 2018) and save the obtained slope to "slopes" array. Then code calculates the maximum slope value from a list of slope values, which is stored in the "slopes" array.

The function __calculate_max_slopes()__ also considers edge pixels by calculating the maximum slope for them in a slightly different way. Specifically, suppose a pixel is on the edge of the raster (i.e. its row or column index is either 0 or equal to the maximum index). The maximum slope is calculated for its surrounding pixels within the raster bounds using the __max()__ function.
Maximum slope calculation for edge pixels is achieved by checking if the current pixel is on the edge of the raster. If so, the script calculates the maximum slope for the pixels in a 3x3 window around the current pixel, handling boundary conditions appropriately. The maximum of the slopes obtained from this operation  is compared to the maximum slope previously calculated for the current pixel, and the greater of the two values is assigned to max_slope. 
The maximum slope value is then stored in a new NumPy array that is returned at the end of the function.

### Data Visualization
The program uses the matplotlib library to visualize the raster data and the maximum slope map as an image. The __imshow()__ function displays the raster data and the maximum slope map, and the __colorbar()__ function displays a colour bar indicating the data values. The __title()__ function is used to set the plot title.
The program also allows displaying the locations with the maximum slope on the maximum slope map. The __np.where()__ function is used to find the indices of the pixels with the maximum slope, and the __plot()__ function is used to display the locations on the map.

In the code used 
- plt.plot(max_slope_indices[1], max_slope_indices[0], 'x', color='purple') 
instead of 
- plt.plot(max_slope_indices[0], max_slope_indices[1], 'x', color='purple')
The reason of this is the ___np.where___ function which returns the indices in a tuple with the first element representing the row indices (y) and the second element representing the column indices (x). 

So, _max_slope_indices[0]_ represents the y-coordinates (rows), while _max_slope_indices[1]_ represents the x-coordinates (columns). In the context of plotting the extreme locations on top of the maximum slope map, the locations should be plotted by using the (x, y) coordinate convention (where x represents the horizontal axis and y represents the vertical axis), so  _max_slope_indice[1]_ was used as the x-coordinates and _max_slope_indices[0]_ as the y-coordinates to plot the locations using ___plt.plot___.


### Graphical User Interface (GUI)
The program has a simple graphical user interface implemented using the [Tkinter library](https://docs.python.org/3/library/tkinter.html#module-tkinter). The program creates a root window using the Tk() function and hides it using the withdraw() function in order to avoid creating an extra, unnecessary window. The GUI consist of the main window with four buttons: "Show Raster", "Show slope of raster", "Show extreme locations", and "Exit". 


When the user clicks the _"Show Raster"_ button, a file dialog is displayed, that allows the user to select a text file containing the raster data. Once the user selects a file, the script loads the raster data and displays it as an image using matplotlib.


When the user clicks the _"Show slope of raster"_ button, the script loads the raster data, calculates the maximum slope for each pixel using the __calculate_max_slopes()__ function, and displays the resulting slope map using matplotlib.


When the user clicks the _"Show extreme locations"_ button, the script loads raster, calculates the maximum slope for each pixel, and finds the locations with the maximum slope. The script then prints the maximum slope value and the number of locations with maximum slope and plots the locations with maximum slope on top of the maximum slope map using matplotlib.

Finally, the script exits when the user clicks the _"Exit"_ button. The GUI interface also handles the case where the user closes the window by clicking the ___"x"___ button in the corner of the window. In this case, the script exits by calling the __exiting()__ function.

Overall, this script provides a simple and intuitive interface for users to interact with the __calculate_max_slopes()__ function and visualize the resulting slope map.



## Running Tests

In the test folder of the project, located slope_calculation_test.py file, which is used to test the function calculate_max_slopes() with [doctest](https://docs.python.org/3/library/doctest.html). Doctest is a Python module that searches for pieces of text that look like interactive Python sessions and then executes them to verify that they work exactly as shown. 

With this testing method were, two situations tested first one was    

    >>> test = ([1,2,3],[3,4,5],[4,5,7,],[1,2,3])
    >>> calculate_max_slopes(test)
The failure of this test was understandable as "test" was a tuple object with no shape attribute.

The second test was:

    >>> test = ([1,2,3],[3,4,5],[4,5,7,],[1,2,3])
    >>> calculate_max_slopes(np.array(test))
The result of this test was also a failure, but the reason for it is not understandable as the test does not give any errors
## Results
The software was tested using a DEM stored in a text file _(dem.txt)_. The dataset was called by clicking GUI's _"Show Raster"_ button. The raster was successfully loaded using NumPy and plotted with the Matplotlib library. Then by clicking the _"Show slope of raster"_ button, the maximum slope was calculated for each pixel in the DEM using the __calculate_max_slopes()__ function. The maximum slopes map was visualised using Matplotlib. Then by clicking the _"Show extreme locations"_ button slope map was visualised again, but this time also, the most extreme locations were visualised with the "x" markers on the map. In the end, by clicking the _"Exit"_ button the program was closed.
## Conclusion
The program described in this technical report demonstrates how to calculate the maximum slope for each pixel of a digital elevation model, selected manually by the user, and detect locations with extreme slopes using Python. The program uses numpy and matplotlib libraries for data manipulation and visualization. The program creates a simple graphical user interface with a tkinter module. The slope calculation is performed using a script named slope_calculation.py that uses a nested loop to calculate the slope for each raster pixel.
The resulting implementation can be used to analyze the slope of the earth's surface in any given area, which can be helpful for various applications, including geology and agriculture.
## References
- Balasubramanian, A. (2017) DIGITAL ELEVATION MODEL (DEM) IN GIS, researchgate. Available at: https://www.researchgate.net/profile/A-Balasubramanian/publication/319454004_DIGITAL_ELEVATION_MODEL_DEM_IN_GIS/links/59ab68fe0f7e9bdd114fbee7/DIGITAL-ELEVATION-MODEL-DEM-IN-GIS.pdf (Accessed: May 7, 2023). 
- Doctest - Test Interactive Python examples (2023) Python documentation. Available at: https://docs.python.org/3/library/doctest.html (Accessed: 10 May 2023). 
- Humboldt State University (2018) Calculating Slope, Geospatial Activities. Available at: https://gsp.humboldt.edu/olm/Lessons/GIS/09%20TerrainAnalsis/Calculating_Slope.html (Accessed: 10 May 2023). 
- Matplotlib Pyplot (2023) W3Schools Online Web Tutorials. Available at: https://www.w3schools.com/python/matplotlib_pyplot.asp (Accessed: 10 May 2023). 
- NumPy Tutorial (2023) W3Schools Online Web Tutorials. Available at: https://www.w3schools.com/python/numpy/default.asp (Accessed: 10 May 2023). 
- Tkinter - Python interface to TCL/TK (2023) Python documentation. Available at: https://docs.python.org/3/library/tkinter.html (Accessed: 10 May 2023). 
## Author

- [@zivarh](https://github.com/zivarh)


