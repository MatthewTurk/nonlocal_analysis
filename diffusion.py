"""
Title:   diffusion.py
Author:  Jared Coughlin
Date:    3/11/19
Purpose: Simple first implementation of modelling a matierial being moved by a random
            velocity field
Notes:
"""
import os
import sys

import numpy as np



#============================================
#                 Grid Class
#============================================
class Grid():
    """
    This is a container class for all of the cells in a single grid. It also holds
    meta-data about the grid. It's meant so that you never have to interact with
    individual cells.

    Parameters:
    -----------
        ndims : float
            The number of dimensions in the grid

        ncells : int
            The number of cells along each dimension. Assumed to be the same for each
            dimension.

        boxSize : float
            The length of each dimension of the simulation volume. Assumed to be the same
            for each dimension.

    Attributes:
    -----------
        pass

    Methods:
    --------
        pass
    """
    #-----
    # Constructor
    #-----
    def __init__(self, ndims, ncells, boxSize):
        self.ndims     = ndims
        self.ncells    = ncells
        self.boxSize   = boxSize
        self.parent    = None
        self.children  = None
        self.cellWidth = self.boxSize / self.ncells 
        self.grid      = self._create_grid()

    #-----
    # _create_grid
    #-----
    def _create_grid(self):
        """
        Instantiates a ndims array of Cell instances that hold the value of various
        quantities at certain locations in the simulation space.

        Parameters:
        -----------
            None

        Returns:
        --------
            grid : ndarray
                An ndims dimensional array of Cell instances
        """
        # Initialize empty array
        grid = np.empty([self.ncells]*self.ndims, dtype=object)
        # Initialize each cell in the grid. This is done using the nditer iterator in
        # order to loop over each element in the ndims dimensional grid. The multi_index
        # flag tells the iterator to yield the index for the current array element
        it = np.nditer(grid, flags=['multi_index'])
        while not it.finished:
            # Get location of cell center from cell index (x0,x1,x2,...,xn). This is just
            # the number of half deltas in each dimension, where delta is the width of the
            # cell. The number of half deltas is just 2k + 1, where k is the cell index
            # along a dimension.
            ind = np.array(it.multi_index)
            loc = (2 * ind + 1) * (self.cellWidth / 2.)
            grid[it.multi_index] = Cell(loc, self.cellWidth)
            # Go to the next element. Without this, it's an infinite loop
            it.iternext()
        return grid

    #-----
    # init_field
    #-----
    def init_field(self, field):
        """
        This is the driver function for initializing a field on the grid.

        Parameters:
        -----------
            field : Field Class
                An instance of the field class that contains useful info about the field

        Returns:
        --------
            None
        """
        # Loop over every cell and apply the field's cell assignemnt function
        it = np.nditer(self.grid, flags=['multi_index'])
        while not it.finished:
            self.grid[it.multi_index][field.name] = 
                field.assignmentFunc(self.grid, it.multi_index))
            it.iternext()



#============================================
#                Cell Class
#============================================
class Cell(dict):
    """
    This class is for an individual cell. Each cell contains a region in space and
    stores information about various quantities in that region.

    Parameters:
    -----------
        loc : ndarray
            This array contains the location of the cell's center

        cellWidth : float
            The width of the cell in each dimension. Assumed to be the same for each
            dimension.

    Attributes:
    -----------
        pass

    Methods:
    --------
        pass
    """
    #-----
    # Constructor
    #-----
    def __init__(self, loc, cellWidth):
        self.loc   = loc
        self.width = cellWidth



#============================================
#                Field Class
#============================================
class Field():
    """
    This class is meant to be the parent class for all other fields. It contains all of
    the infrastructure that the rest of the code interfaces with. Actual fields should
    subclass this.

    Parameters:
    -----------
        name : str
            The name of the field

        assignmentFunc : function
            The subclass' driver function for initializing itself in each cell of a grid.
            Each assignment function should have the same signature of taking in both the
            grid and current cell index, in case that information is needed.

    Attributes:
    -----------
        pass

    Methods:
    --------
        pass
    """
    #-----
    # Constructor
    #-----
    def __init__(self, name, assignmentFunc):
        self.name = name
        self.assignmentFunc = assignmentFunc



#============================================
#             OceanCurrent Class
#============================================
class OceanCurrent(Field):
    """
    This is a test field. It models the current of a patch of ocean as random velocity
    vectors in each cell.

    Parameters:
    -----------
        None

    Attributes:
    -----------
        pass

    Methods:
    --------
        pass
    """
    #-----
    # Constructor
    #-----
    def __init__(self):
        super().__init__('OceanCurrent', self.random_vel)

    #-----
    # random_vel
    #-----
    def random_vel(self, grid, index):
        """
        This function is the assignmentFunc for this field. It assigns a random vector
        to each cell.

        Parameters:
        -----------
            grid : Grid Class
                The current grid for which the field values are being initialized

            index : tuple
                The multi_index tuple returned by the np.nditer iterator. Gives the index
                of the current cell in the current grid

        Returns:
        --------
        """
        vel = np.random.normal(size=grid.shape)
        return vel



#============================================
#            read_parameter_file
#============================================
def read_parameter_file():
    pass



#============================================
#                setup_field
#============================================
def setup_field(grids, fields):
    """
    This function takes in a grid object and initializes the field values in each cell

    Parameters:
    -----------
        grids : list
            A list of instances of the grid class. Contains the cells to be initialized.

        fields : list
            A list of field class instances to initialze on each grid

    Returns:
    --------
        grids : list
            The same grid list, but with the field initialized in each cell
    """
    # For each grid, initialize each field
    for i in range(len(grids)):
        for f in fields:
            grids[i].init_field(f)
    return grids



#============================================
#                  diffuse
#============================================
def diffuse():
    pass



#============================================
#                  main
#============================================
def main():
    # Read parameter file
    try:
        params = read_parameter_file(sys.argv[1])
    except IndexError, IOError:
        print('Usage: python ./diffusion.py /path/to/param_file')
        sys.exit(1)
    # Create grid
    grid = Grid(params['ndims'], params['ncells'], params['boxSize'])
    # Create field
    grid = setup_field([grid], params['fields'])
    # Diffuse
    diffuse([grid], params['fields'])



#============================================
#               Run Program
#============================================
if __name__ == '__main__':
    main()
