"""
Title:   field.py
Author:  Jared Coughlin
Date:    3/13/19
Purpose: Contains the field class
Notes:
"""



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
