"""
Title:   path.py
Author:  Jared Coughlin
Date:    3/13/19
Purpose: Contains the path class
Notes:
"""



#============================================
#                Path Class
#============================================
class Path():
    """
    This class is used to represent a path through the simulation volume. The idea is
    that this path can be either pre-defined or dynamically defined (so it can change
    on the fly). Additionally, the object keeps track of where in the volume it has
    already traversed and can optionally hold information about various quantities at
    the points it's already visited. This is geared towards being able to integrate a
    quantity along the trajectory represented by the path in order to do accumulation.

    Parameters:
    -----------
        startingPoint : tuple
            This is a set of coordinates for where the path should originate

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
    def __init__(self, startingPoint):
        self.startingPoint = startingPoint
        self.curPos = self.startingPoint
        self.stepSize = None
        self.accumulator = {}
        self.locs = []

    #-----
    # update
    #-----
    def update(self, grid, ind, field):
        """
        This function advances the tip of the path to a new location based on the step
        size and magnitude and direction of the field at the current location. It then
        also archives the old position for later use.

        Parameters:
        -----------
            grid : Grid Class
                The grid of cells the path is moving through

            ind : tuple
                The index of grid corresponding to the cell the path's tip is currently in

            field : Field Class
                The field doing the "kicking"

        Returns:
        --------
            curPos : tuple
                The new current position of the path's tip
        """
        # Save the current position
        self.locs.append(self.curPos)
        # Update the current position
        # This should potentially change. Since the goal is to be able to dynamically
        # determine the path, instead of just grid[ind][field.name], there should be
        # a user-specified function here that calculates whichever vector field they
        # want to use to determine the path, such as direction of steepest density
        # increase or something
        self.curPos += self.stepSize * grid[ind][field.name]
        return self.curPos
