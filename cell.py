"""
Title:   cell.py
Author:  Jared Coughlin
Date:    3/13/19
Purpose: Contains the cell class
Notes:
"""



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
