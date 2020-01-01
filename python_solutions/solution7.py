# Problem 7:
# This problem was asked by Facebook

"""
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

# Author: Piyush Agarwal
# Written on: 31-12-2019

# Solution

def helper(data, k):
	
	# base cases:
	# if empty string then 1 way
	if k == 0:
		return 1

	# starting index
	s = len(data) - k
	if data[s] == '0':
		return 0
	
	result = helper(data, k-1)
	if k>=2 and int(data[s:s+2]) < 27:
		result += helper(data, k-2)

	return result
	
def num_ways(data):
	return helper(data, len(data))

def helper_dp(data, k, memo):

        # base cases:
        # if empty string then 1 way
        if k == 0:
                return 1

        # starting index
        s = len(data) - k
        if data[s] == '0':
                return 0

	if memo[k[ is not None:
		reutrn memo[k]

        result = helper(data, k-1, memo)
        if k>=2 and int(data[s:s+2]) < 27:
                result += helper(data, k-2, memo)
	memo[k] = result

        return result

def num_ways_dp(data):
	memo = [ None ] * (len(data) + 1)
        return helper_dp(data, len(data), memo)

print(num_ways('12345'))
print(num_ways('111'))
print(num_ways('11223'))
print(num_ways('123456'))
print(num_ways('10301')
print(num_ways_dp('12345'))
print(num_ways_dp('111'))
print(num_ways_dp('11223'))
print(num_ways_dp('123456'))
print(num_ways_dp('10301')))
