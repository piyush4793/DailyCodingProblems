# Problem 12:
# This problem was asked by Amazon

"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? 
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

# Author: Piyush Agarwal
# Written on: 06-01-2020

# Solution

def solve(n, x):

	ways = []
	min_step = min(x) or 0

	for i in range(min_step):
		ways.append(0)

	for i in range(min_step, n+1):
		ways.append(0)
		if i  in x:
                        ways[i] += 1
		for j in x:
			ways[i] += ways[i-j] if i > j else 0
		
	return ways[-1]

print('Results for N --> 1-5 and x = {1, 2}')
print(solve(1, {1, 2}))
print(solve(2, {1, 2}))
print(solve(3, {1, 2}))
print(solve(4, {1, 2}))
print(solve(5, {1, 2}))
print('----------------------')
print('Results for N --> 1, 3, 5-9 and x = {1, 3, 5}')
print(solve(1, {1, 3, 5}))
print(solve(3, {1, 3, 5}))
print(solve(5, {1, 3, 5}))
print(solve(6, {1, 3, 5}))
print(solve(7, {1, 3, 5}))
print(solve(8, {1, 3, 5}))
print(solve(9, {1, 3, 5}))
