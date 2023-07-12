#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 12
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 0
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = -4
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = "4"
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 21
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 42
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 36
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 17
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 55
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 117
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 221995
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

n = 840810840
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))
