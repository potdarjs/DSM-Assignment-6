"""
Assignment 6
Data Science Masters

"""
"""
Write a function so that the columns of the output matrix are powers of the input vector.
The order of the powers is determined by the increasing boolean argument. Specifically,
when increasing is False, the i-th output column is the input vector raised element-wise
to the power of N - i - 1.
"""
import numpy as np
# Inputs
x = np.array([1,2,3,4,5])
n = 5

# Function to buit matrix as desired
np.column_stack([x**(n-1-i) for i in range(n)])

# with function vander

np.vander(x,5)