#!bin/usr/python3

# You are given the shape of the array in the form of space-separated integers, each integer representing the size of different dimensions, your task is to print an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.
#
# Input Format
#
# A single line containing the space-separated integers.
#
# Constraints
#
#
# Output Format
#
# First, print the array using the numpy.zeros tool and then print the array with the numpy.ones tool.
import numpy

nums = tuple(map(int, input().split()))
print(numpy.zeros(nums, dtype=numpy.int))
print(numpy.ones(nums, dtype=numpy.int))
