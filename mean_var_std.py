# You are given a 2-D array of size X.
# Your task is to find:
#
# The mean along axis
# The var along axis
# The std along axis
# Input Format
#
# The first line contains the space separated values of  and .
# The next  lines contains  space separated integers.
#
# Output Format
#
# First, print the mean.
# Second, print the var.
# Third, print the std.

import numpy as np

n, m = map(int, input().split())
b = []
for i in range(n):
    a = list(map(int, input().split()))
    b.append(a)

b = np.array(b)

np.set_printoptions(legacy='1.13')
print(np.mean(b, axis=1))
print(np.var(b, axis=0))
print(np.std(b))
