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
import plot
import user_fields as uf
import utils



#============================================
#                  main
#============================================
def main():
    # Read parameter file
    try:
        params = utils.read_parameter_file(sys.argv[1])
    except (IndexError, IOError):
        print('Usage: python ./diffusion.py /path/to/param_file')
        sys.exit(1)
    # Create grid
    g = grid.Grid(params['ndims'], params['ncells'], params['boxSize'])
    import pdb;pdb.set_trace()
    # Create field
    field = uf.OceanCurrent()
    # Initialize the field on the grid
    g.init_field(field)
    # Just for now, have it start in the middle of the box
    #startingPoints = [params['boxSize'] / 2. for _ in range(params['ndims'])]
    startingPoints = [tuple([params['boxSize'] / 2. for _ in range(params['ndims'])])] * params['npaths']

    # Set up the paths
    g.init_paths(params['npaths'], startingPoints)
    # Diffuse
    g.diffuse(field, params['nsteps'], params['stepSize'])
    # Accumulate a quantity along the path
    #g.path_accumulation(field)
    # Plot (just to test). Have an arrow in each cell representing the direction
    # and magnitude of the field in that cell. Then have another set of arrows showing
    # the path of the test particle
    plots.test_plot(g, field)



#============================================
#               Run Program
#============================================
if __name__ == '__main__':
    main()
