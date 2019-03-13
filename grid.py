"""
Title:   grid.py
Author:  Jared Coughlin
Date:    3/13/19
Purpose: Contains the grid class
Notes:
"""
import numpy as np

import cell



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
            grid[it.multi_index] = cell.Cell(loc, self.cellWidth)
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
