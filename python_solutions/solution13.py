# Problem 13:
# This problem was asked by Amazon

"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

# Author: Piyush Agarwal
# Written on: 06-01-2020

# Solution

# Assumtion string only contains lowercase characters

"""
Explanation:

k = 2
s = abacb

We will keep a dictionary to keep track of the characters and making sure that size of dictionary doesn't exceed k

taking two pointers start and end, both starting from index 0, means here both of them are at a
step 1: start -> 0  and end -> 0   d = {'a': 1}  ==> meaning dictionary now have character 'a' with count as 1, we increase end pointer to 1                       max_length = 1
step 2: start -> 0 and end -> 1    d = {'a': 1, 'b': 1}  ==> meaning dictionary now also have character 'b' with count as 1, we increase end pointer to 2          max_length = 2
step 3: start -> 0 and end -> 2    d = {'a': 2, 'b': 1}  ==> meaning dictionary now have character 'a' with count as 2, we increase end pointer to 3               max_length = 3

Point to note is size of dictionary is still less than k, that is 2 is in this case, which suggests there are only 2 distinct character present in our selected window from start to end index

step 4 - 1: start -> 0 and end -> 3    d = {'a': 2, 'b': 1, 'c': 1}  ==> meaning dictionary now have character 'c' with count as 1

Here we can see that dictionary size is 3
So, we will keep on evicting characters from start till we reduce dictionary size to k

step 4 - 2:  d = {'a': 1, 'b': 1, 'c': 1}  first evict current start character, then increment value of start by 1      start -> 1 and end -> 3
step 4 - 3:  d = {'a': 1, 'b': 0, 'c': 1} => delete b from dictionary => d = {'a': 1, 'c': 1}                           start -> 2 and end -> 3

Now size is 2 which is equal to k
current length of window is 2 ==> end - start + 1 = 3-2+1 = 2
Now we compare max_length with current window length ===> we assign maximum of those two values to max_length variable
then we increase end pointer to 4
so, we can say still max_length = 3

step 5 - 1: start -> 2 and end -> 4       d = {'a': 1, 'b': 1, 'c': 1}  ==> meaning dictionary now have character 'b' with count as 1, we increase end pointer to 5

step 5 - 2: d = {'a': 0, 'b': 1, 'c': 1} => delete a from dictionary => d = {'b': 1, 'c': 1}                           start -> 3

we came out of deletion loop
current length of window is 2 ==> end - start + 1 = 4-3+1 = 2
Now we compare max_length with current window length ===> we assign maximum of those two values to max_length variable
then we increase end pointer to 5
so, we can say still max_length = 3

Since, end pointer is greater than length of string. So we get out of the loop

return max_length which is 3 in this case

"""


def solve(k, s):
	tracker = {}
	start = 0
	end = 0
	max_length = 0
	while end < len(s):
		ch = s[end]
		if ch not in tracker:
			tracker[ch] = 1
		else:
			tracker[ch] += 1

		while len(tracker) > k:
			tracker[s[start]] -= 1
			if tracker[s[start]] == 0:
				del tracker[s[start]]
			start += 1
			
		max_length = max(max_length, end - start + 1)
		end += 1

	return max_length
		

print(solve(2, 'abcbbbbcccbdddadacb'))
print(solve(2, 'abacb'))
