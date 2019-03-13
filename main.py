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

import grid
import utils



#============================================
#                  main
#============================================
def main():
    # Read parameter file
    try:
        params = utils.read_parameter_file(sys.argv[1])
    except IndexError, IOError:
        print('Usage: python ./diffusion.py /path/to/param_file')
        sys.exit(1)
    # Create grid
    g = grid.Grid(params['ndims'], params['ncells'], params['boxSize'])
    # Create field
    g.init_field()
    # Set up the paths
    g.init_paths(params['npaths'], startingPoints)
    # Diffuse
    g.diffuse()



#============================================
#               Run Program
#============================================
if __name__ == '__main__':
    main()
