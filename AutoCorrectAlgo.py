#!/usr/bin/env python3
import pprint # Used for debugging

'''
Author: Daniel Busuttil
Date: 03 June 2018 - 
Auto-correct algorithm written in Python, using the Levenshtein algo written previously and a text file of ~60k words
'''


def LevDistance(in_1, in_2):
    dim_1 = len(in_1) # == max j value
    dim_2 = len(in_2) # == max i value

    # Creates -@ run-time- an empty 2D list, sized ' dim_2 + 2 x dim_1 + 2 '
    lev_arr = [  [ ' ' for j in range(0, dim_1 + 2) ]  for i in range(0, dim_2 + 2) ]

    # Naming/initializing columns
    lev_arr[0][1] = '#'
    lev_arr[1][0] = '#'
    for j in range(0, dim_1):
        lev_arr[0][j+2] = in_1[j]
    for i in range(0, dim_2):
        lev_arr[i+2][0] = in_2[i]

    # Filling inital zero-cost cells
    for j in range(1, dim_1 + 2):
        lev_arr[1][j] = j - 1
    for i in range(1, dim_2 + 2):
        lev_arr[i][1] = i - 1

    # Calculating edit-distance
    for j in range(2, dim_1 + 2):
        for i in range(2, dim_2 + 2):
            # D(i, j) = min( insertion, deletion, substitution )
            lev_arr[i][j] = min( ( lev_arr[i][j - 1] + 1), ( lev_arr[i - 1][j] + 1), ( lev_arr[i - 1][j - 1] + ( 0 if in_1[j - 2] == in_2[i - 2] else 2 ) ) )

    # Visualization
    #print("Levenshtein distance is: " + str(lev_arr[dim_2 + 1][dim_1 + 1]))
    #pprint.pprint(lev_arr) if input("Would you like to see the Levenshtein-array? 'y' or 'n' ") == ('y' or 'n') else None
    return lev_arr[dim_2 + 1][dim_1 + 1]

def WordLibrary():
    




