"""
Title:   utils.py
Author:  Jared Coughlin
Date:    3/13/19
Purpose: Contains helper functions
Notes:
"""



#============================================
#               get_registers
#============================================
def get_registers():
    int_register = [
                    'nsteps',
                    'npaths',
                    'ndims'
                    ]
    float_register = [
                        'boxSize',
                        'stepSize'
                    ]
    return int_register, float_register



#============================================
#            read_parameter_file
#============================================
def read_parameter_file(fname):
    params = {}
    int_register, float_register = get_registers()
    with open(fname, 'r') as f:
        for line in f:
            key, value = line.split(':')
            key = key.strip()
            value = value.strip()
            if key in int_register():
                value = int(value)
            elif key in float_register():
                value = float(value)
            params[key] = value
    return params
