"""
Title:   grid.py
Author:  Jared Coughlin
Date:    3/13/19
Purpose: Contains the grid class
Notes:
"""
import numpy as np

import cell
import path



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
        self.paths     = None

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

    #-----
    # init_paths
    #-----
    def init_paths(self, npaths, startingPoints):
        """
        This function creates the path objects.

        Parameters:
        -----------
            npaths : int
                The number of path objects to use

            startingPoints: list
                A list of coordinate tuples specifying where each path should begin

        Returns:
        --------
            None
        """
        self.paths = []
        for i in range(npaths):
            self.paths[i] = path.Path(startingPoints[i])

    #-----
    # diffuse
    #-----
    def diffuse(self, field, nsteps, stepSize):
        """
        This function simply "kicks" each of the path starting points around the volume
        according to the values of field in the cells. That is, the paths don't accumulate
        or even really track anything, they just get pushed around by the field.

        QUESTIONS: 
            1.) How long does the diffusion last?
                    a.) Should the user simply specify a number of steps?
                    b.) Should the exit be based on some condition?
                    c.) Is there a way to determine this dynamically?
            2.) How large is each "time" step? (it's not really time since the simulation
                is static, but rather, some path parameter tau)
                    a.) Should this be fixed or adaptive?

        ANSWERS?
            1.) The easiest thing to start with is definitely a fixed, user-specifed,
                number of steps.
            2.) The easiest thing is just a fixed step that's simply chosen a priori

        Parameters:
        -----------
            field : Field Class
                The field to do the "kicking"

        Returns:
        --------
            None
        """
        # Loop over each step
        for i in range(nsteps):
            # At each step, loop over each path
            for j in range(len(self.paths)):
                # Set the step size for the path
                self.paths[j].stepSize = stepSize
                # Figure out which cell the "tip" of the path is currently in
                cell_ind = self._get_cell_index(self.paths[j].curPos)
                # Update the path's tip position based on the field value in that cell.
                # This also archives the old current position and saves the field values
                # in case integration/accumulation happens later
                self.paths[j].curPos = self.paths[j].update(self.grid, cell_ind, field)

    #-----
    # _get_cell_index
    #-----
    def _get_cell_index(self, loc):
        """
        This function returns the index of grid corresponding to the given location.
        The conversions to and from tuple are probably unnecessary. It's probably easier
        to just work with a list from the get-go.

        Parameters:
        -----------
            loc : tuple
                The coordinates of the point we want to find the corresponding cell for

        Returns:
        --------
            cell_ind : tuple
                The multi-index of grid corresponding to the cell that loc lies in
        """
        # Make loc a list since tuples are immutable
        if isinstance(loc, tuple):
            loc = list(loc)
        # Since the cell width in each dimension is known, all that needs to be done is
        # to divide the point's position in each dimension by the cell width and floor
        # the result to get the appropriate index. This implicitly assumes that the cell
        # width is the same in all dimensions as well as the same for every cell
        for i in range(len(loc)):
            loc[i] = int(loc[i] / self.grid[0].cellWidth)
        return tuple(loc)
