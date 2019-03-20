"""
Title:   user_fields.py
Author:  Jared Coughlin
Date:    3/13/19
Purpose: All custom fields go here
Notes:
"""
import numpy as np

import field



#============================================
#             OceanCurrent Class
#============================================
class OceanCurrent(field.Field):
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
    def random_vel(self, grid, ndims, index):
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
        vel = np.random.normal(size=ndims)
        return vel
