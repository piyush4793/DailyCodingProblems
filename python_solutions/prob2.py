# Problem 2
# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

import functools

def solve(arr):
	res = list()
	
	# get product of all the elements
	# prod_all = 1
	# for i in arr:
	# 	prod_all = prod_all * i

	prod_all = functools.reduce(lambda x,y : x*y, arr)

	length = len(arr)
	for i in range(length):
		res.append(prod_all//arr[i])
	
	return res

# solve without using division
def solve2(arr):
	res, left, right = list()
	left[0], left[1] = 1, arr[0]
	length = len(arr)
	right[-1], right[-2] = 1, arr[-1]
	for i, elem in enumerate(arr[2:]):
		left[i] = left[i-2] * left[i-1]

	for i, elem in enumerate(arr[:-3:-1]):
                        right[length-i-1] = right[length-i] * right[length-i+1]
	
	for i in range(length):
		res.append(left[i]*right[i])		
		

result1 = solve([1, 2, 3, 4, 5])
print(result1)
result2 = solve([3, 2, 1])
print(result2)
result3 = solve([1, 2, 3, 4, 5])
print(result3)
result4 = solve([3, 2, 1])
print(result4)
