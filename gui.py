import numpy as np # importing numpy library as np for easily working with provided data
import matplotlib.pyplot as plt # importing matplotlib.pyplot  library as plt for plotting
from tkinter import * #import all modules libraries from tkinter
from tkinter import filedialog, Tk
'''
filedialog module was imported from tkinter library for File dialogs help you open, save files or directories. 
This is the type of dialog you get when you click file,open. 
This dialog comes out of the module, there is no need to write all the code manually.

Tk provides a independent windowing toolkit, that is available to Python programmers using the tkinter package
'''
import slope_calculation  # import custom module for slope calculation
# function to load raster data from file
def load_raster_data():
    # create Tkinter root object and hide it
    root = Tk() # It helps to display the root window and manages all the other components of the tkinter application
    root.withdraw()
    '''
    root. withdraw used to prevent an additional, empty window from appearing on the user's screen when the program starts.
    By default, when a new Tk object is created, it also creates an empty window (a "root" window) on the user's screen. 
    By calling the withdraw() method on the root window, can avoid creating an extra, unnecessary window.

    '''

    # prompt user to select a file using a file dialog
    file_path = filedialog.askopenfilename(title='Select Raster Data File', filetypes=[('Text Files', '*.txt')])

    # check if user selected a file
    if file_path:
        # load data from file and return it as a numpy array
        data = np.loadtxt(file_path)
        return data
    #if nothing selected returns nothing
    else:
        return None

# on_select() function is a function which demonstrates the raster
def on_select():
    global raster
    '''
    global variable is used to allow function to access data that has been loaded or calculated in other parts of the program.
    '''
    raster = load_raster_data()
    #check whether the variable "raster" has a value other than None. 
    #If the condition is true, then the raster will be visualised.
    if raster is not None:
        #displays loaded raster data with given color, colorbar and title
        plt.imshow(raster, cmap='GnBu_r')
        plt.colorbar()
        plt.title('Digital Elevation Model')
        plt.show()

# calculate_slopes() function is a function which demonstrates the maximum slopes of raster
def calculate_slopes():
    # load raster data
    raster = load_raster_data()

    # saves calculated aximum slopes to max_slopes.txt file
    np.savetxt('max_slopes.txt', slope_calculation.calculate_max_slopes(raster))

    # calculated maximum slopes assigned to max_slopes
    max_slopes = slope_calculation.calculate_max_slopes(raster)

    # display maximum slope map with given color, color bar and title
    plt.imshow(max_slopes, cmap='winter')
    plt.colorbar()
    plt.title('Maximum Slopes')
    plt.show()

# maximum_locations() function is a function which demonstrates the maximum slopes of raster with extreme locations, 
# prints the maximum slope value and the number of locations where it occurs. 
def extreme_locations():
    # load raster data using load_raster_data() function
    raster = load_raster_data()

    #assign the result of calculate_max_slopes() function from slope_calculation script to max_slopes variable
    max_slopes = slope_calculation.calculate_max_slopes(raster)

    #find the value of the maximum slope from the max_slopes array
    max_slope_value = np.max(max_slopes)

    #find the indices of the locations where the maximum slope occurs in the max_slopes array
    max_slope_indices = np.where(max_slopes == max_slope_value)
    
    #find the number of locations where the maximum slope occurs by counting the number of indices in the first dimension
    num_max_slope_locations = len(max_slope_indices[0])

    #print the value of slope at extreme locations and number of extreme locations
    print('Maximum slope value:', max_slope_value)
    print('Number of locations with maximum slope:', num_max_slope_locations)

    # plot extreme locations on top of maximum slope map
    plt.imshow(max_slopes)
    plt.colorbar()
    plt.title('Extreme Locations')
    plt.plot(max_slope_indices[1], max_slope_indices[0], 'x', color='purple')
    '''
    The reason for using plt.plot(max_slope_indices[1], max_slope_indices[0], 'x', color='purple') instead of plt.plot(max_slope_indices[0], max_slope_indices[1], 'x', color='purple')
    is because the np.where function returns the indices in a tuple with the first element representing the row indices (y) and the second element representing the column indices (x).
    So, max_slope_indices[0] represents the y-coordinates (rows), while max_slope_indices[1] represents the x-coordinates (columns).
    In the context of plotting the extreme locations on top of the maximum slope map, we want to plot the locations using the (x, y) coordinate convention (where x represents the horizontal 
    axis and y represents the vertical axis), so we use max_slope_indices[1] as the x-coordinates and max_slope_indices[0] as the y-coordinates to plot the locations using plt.plot.
    '''
    plt.show()   

# exiting() function closes the program  
def exiting():
    """
    Exit the program.
    """
    root.quit() #quits the main event loop of the tkinter window
    root.destroy() #destroys the tkinter window

# create tkinter windiw
root = Tk()

# create buttons in tkinter window 
button_raster = Button(root, text="Show Raster", command=on_select)
button_slope = Button(root, text="Show slope of raster", command=calculate_slopes)
button_maximum = Button(root, text="Show extreme locations", command=extreme_locations)
exit_button = Button(root, text="Exit", command=exiting)
'''
By clicking "Show raster" button on tkinter window, on_select() function activates and enables for user to choose txt file for demonstrating raster
By clicking "Show slope of raster" button, calculate_slopes() function activates and user by selecting txt file can see slope of raster
BY clicking "Show extreme locations" button, extreme_locations() function activates and by selecting again dem file, user can see slope map
but this time with extreme locations demonstrated on it with "x" marks
and finally by clicking "Exit" button user can close tkinter dialog window
'''

# Pack method used to display each button on tkinter window
button_raster.pack()
button_slope.pack()
button_maximum.pack()
exit_button.pack()

# Exit if the user closes the window by clicking the "x" button in the corner of the window by activating exiting function.
root.protocol('WM_DELETE_WINDOW', exiting)
root.mainloop() 
'''
The root.mainloop() function is needed to start the Tkinter event loop. 
This function listens for events like mouse clicks and key presses and dispatches them to the appropriate widgets. 
Without this function, the GUI would be unresponsive to user input.
The mainloop() function runs indefinitely, continuously processing events until the program is terminated or the window is closed.
the event loop must be started after the widgets have been created and added to the window, so that the program can respond to user
input and events. In this script, the event loop is started at the end of the script, after all the buttons have been added to the 
window and their functionality has been defined. This ensures that the program is ready to respond to user input before entering the event loop.
'''