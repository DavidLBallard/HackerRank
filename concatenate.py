# Task
#
# You are given two integer arrays of size X and X ( &  are rows, and  is the column). Your task is to concatenate the arrays along axis .
#
# Input Format
#
# The first line contains space separated integers, and .
# The next  lines contains the space separated elements of the  columns.
# After that, the next  lines contains the space separated elements of the  columns.
#
# Output Format
#
# Print the concatenated array of size X.

import numpy as np
a, b, c = map(int, input().split())
arrA = np.array([input().split() for _ in range(a)], int)
arrB = np.array([input().split() for _ in range(b)], int)
print(np.concatenate((arrA, arrB), axis=0))
