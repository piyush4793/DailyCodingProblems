# Problem 5:
# This problem was asked by Jane Street

"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.
"""

# Author: Piyush Agarwal
# Written on: 31-12-2019



# Solution:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
	def first(a, b):
		return a
	return pair(first)

def cdr(pair):
    def last(a, b):
        return b
    return pair(last)




# Output:
print(car(cons(3, 'a')))
print(cdr(cons(3, 'a')))
