#!/usr/bin/python
# -*- coding: utf-8 -*-
from algorithms import *
from utilities import *

SELECTED_ALGORITHM = memory_efficient_dynamic_programming

def solveIt(input_data):
    # Modify this code to run your optimization algorithm

    # Parse the input
    capacity, values, weights = parse_input(input_data)

    # Call algorithm to solve the problem
    start = time.time()
    item_selected, is_optimal = SELECTED_ALGORITHM(capacity=capacity, values=values, weights=weights)
    end = time.time()

    # Return solution as formatted output
    return generate_custom_output(start_time=start, end_time=end, item_selected=item_selected, capacity=capacity, values=values, weights=weights, is_optimal=is_optimal)



import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        input_data_file = open(fileLocation, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solveIt(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)'

