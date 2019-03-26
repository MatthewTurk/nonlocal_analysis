"""
Title:   plot.py
Author:  Jared Coughlin
Date:    3/202/19
Purpose: Contains functions used for making plots from grid quantities
Notes:
"""
import matplotlib.pyplot as plt
import numpy as np



#============================================
#                 test_plot
#============================================
def test_plot(g, field):
    """
    This function plots an arrow showing the magnitude and direction of the field for
    each cell in the grid, stemming from the center of the cell. It then uses a different
    set of arrows to display the path of the test particle. This is to serve as a sanity
    check on what I'm doing. It inherently assumes the data is 2D.

    Parameteters:
    -------------
        g : grid class object
            The grid containing the cells to plot in

        field : field class object
            The name of the field to plot in the cells

    Returns:
    --------
        None
    """
    # Set up figure
    fix, ax = plt.subplots()
    # Set plot limits
    ax.set_xlim(0, g.boxSize)
    ax.set_ylim(0, g.boxSize)
    # Ensure the plot ticks are at the cell boundaries
    tickLocs = [i * g.cellWidth for i in range(g.ncells)]
    # Ensure ticks are in the right place (this is because the grid gets plotted where
    # the ticks are)
    ax.set_yticks(ticLocs, minor=False)
    ax.set_xticks(ticLocs, minor=False)
    # Plot the grid
    ax.grid(linestyle='--', color='#B4C5E4')
    # Plot the field arrows in the cells (this doesn't really work units-wise...)
    for i, c in enumerate(g.grid):
        ax.arrow(c.loc[0], c.loc[1], c[field.name][0], c[field.name][1], color='#090C9B')
    # Plot the test particle path
    # Loop over every path
    for p in g.paths:
        # Loop over every segment of the path
        for i in range(len(p.locs)-1):
            x = p.locs[i][0]
            y = p.locs[i][1]
            dx = p.locs[i+1][0] - p.locs[i][0]
            dy = p.locs[i+1][1] - p.locs[i][1]
            ax.arrow(x, y, dx, dy, color='#3C3744')
    # Save the figure
    plt.savefig('diffusion.png')
