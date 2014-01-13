#!/usr/bin/python
# -*- coding: utf-8 -*-
import algorithms


def solveIt(input_data):
    # Modify this code to run your optimization algorithm

    # Parse the input
    capacity, values, weights = parse_input(input_data)

    # Call algorithm to solve the problem
    SELECTED_ALGORITHM = algorithms.dynamic_programming
    item_selected = SELECTED_ALGORITHM(capacity=capacity, values=values, weights=weights)

    # Return solution as formatted output
    return generate_custom_output(item_selected=item_selected, capacity=capacity, values=values, weights=weights, is_optimal=0)


# UTILITY FUNCTIONS
def calculate_total_value(item_selected, values):
    """
    Given lists of item values and items selected, returns the achieved objective value.
    """
    total_value = 0
    for i in xrange(len(item_selected)):
        if item_selected[i]:
            total_value += values[i]
    return total_value

def calculate_total_weight(item_selected, weights):
    """
    Given lists of item values and items selected, returns the total weight used.
    """
    return sum(weights[i] * item_selected[i] for i in xrange(len(weights)))

def parse_input(input_data):
    """
    Given a string of data from an input file, returns:
        - Capacity of knapsack
        - List of item values
        - List of item weights
    """
    lines = input_data.split('\n')

    first_line = lines[0].split()
    number_of_items = int(first_line[0])
    capacity = int(first_line[1])
    values, weights = [], []

    for i in xrange(1, number_of_items + 1):
        line = lines[i]
        parts = line.split()

        values.append(int(parts[0]))
        weights.append(int(parts[1]))

    return capacity, values, weights

def generate_output(item_selected, capacity=0, values=None, weights=None, is_optimal=0):
    """
    Given a solution, returns a string of the solution formatted per problem specification.
    """
    output_data = str(calculate_total_value(item_selected, values)) + ' ' + str(is_optimal) + '\n'
    output_data += ' '.join(map(str, item_selected))
    return output_data

def generate_custom_output(item_selected, capacity, values, weights, is_optimal=0):
    """
    Given a solution, returns a string of the solution along with helpful information.
    Does not conform to the problem specification.
    """
    output_data = 'Total value:\t' + str(calculate_total_value(item_selected, values)) + '\n'
    output_data += 'Total weight:\t' + str(calculate_total_weight(item_selected, weights)) + '\tout of capacity:\t' + str(capacity) + '\n'
    output_data += 'Items selected:\t' + ' '.join(map(str, item_selected))
    return output_data



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

