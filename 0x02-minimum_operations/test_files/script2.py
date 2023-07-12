#!/usr/bin/python3

from random import randint
from time import time
minOperations = __import__('0-minoperations').minOperations
minOpsStrict = __import__('0-minoperations-strict_primes').minOperations

n = 0
favor1 = 0
favor2 = 0
while n < 500:
    random_num = randint(0, 999999)
    start1 = time()
    result1 = minOperations(random_num)
    stop1 = time()
    print("n = " + str(random_num), end="\t-->\t")
    start2 = time()
    result2 = minOpsStrict(random_num)
    stop2 = time()
    if result1 != result2:
        print('we found a fail!')
        print("\nresult1: ", result1, "\tresult2: ", result2)
        break
    print(result1)
    time_diff1 = stop1 - start1
    time_diff2 = stop2 - start2
    print("time difference = ", time_diff1 - time_diff2)
    if time_diff1 - time_diff2 < 0:
        favor1 += 1
    elif time_diff1 - time_diff2 > 0:
        favor2 += 1
    if (n % 10) == 0:
        print("favor1: ", favor1, "\tfavor2: ", favor2)
    n += 1
if (favor1 == favor2):
    print("1 and 2 are even")
elif (favor1 > favor2):
    print("1 is better by ", favor1 - favor2)
else:
    print("2 is better by ", favor2 - favor1)
