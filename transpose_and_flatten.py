#!bin/usr/python3

# Task
#
# You are given a X integer array matrix with space separated elements ( = rows and  = columns).
# Your task is to print the transpose and flatten results.
#
# Input Format
#
# The first line contains the space separated values of  and .
# The next  lines contains the space separated elements of  columns.
#
# Output Format
#
# First, print the transpose array and then print the flatten.

import numpy

n, m = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)
print(array.transpose())
print(array.flatten())
