# DailyCodingProblems
This repository contains solution to different interview problems asked by renowned companies

### Questions:
Q1. Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
```For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.```

Q2. Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
```For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].```

Q3. Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

Q4. Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

Q5. cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair.
```For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.```
Given this implementation of cons:
```
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```
Implement car and cdr.

Q6. An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node.  
Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.  
If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

Q7. Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.  
```For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.```  
You can assume that the messages are decodable. For example, '001' is not allowed.

### Solutions (in python):
* [Solution 1](https://github.com/piyush4793/DailyCodingProblems/blob/master/python_solutions/solution1.py)
* [Solution 2](https://github.com/piyush4793/DailyCodingProblems/blob/master/python_solutions/solution2.py)
* [Solution 3](https://github.com/piyush4793/DailyCodingProblems/blob/master/python_solutions/solution3.py)
* [Solution 4](https://github.com/piyush4793/DailyCodingProblems/blob/master/python_solutions/solution4.py)
* [Solution 5](https://github.com/piyush4793/DailyCodingProblems/blob/master/python_solutions/solution5.py)
* [Solution 6](https://github.com/piyush4793/DailyCodingProblems/blob/master/python_solutions/solution6.py)
* [Solution 7](https://github.com/piyush4793/DailyCodingProblems/blob/master/python_solutions/solution7.py)
