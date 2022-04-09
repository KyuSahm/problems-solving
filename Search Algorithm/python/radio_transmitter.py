'''
HackerRank
Hackerland is a one-dimensional city with houses aligned at integral locations along a road. The Mayor wants to install radio transmitters on the roofs of the city's houses. Each transmitter has a fixed range meaning it can transmit a signal to all houses within that number of units distance away.

Given a map of Hackerland and the transmission range, determine the minimum number of transmitters so that every house is within range of at least one transmitter. Each transmitter must be installed on top of an existing house.

Example



 antennae at houses  and  and  provide complete coverage. There is no house at location  to cover both  and . Ranges of coverage, are , , and .

Function Description

Complete the hackerlandRadioTransmitters function in the editor below.

hackerlandRadioTransmitters has the following parameter(s):

int x[n]: the locations of houses
int k: the effective range of a transmitter
Returns

int: the minimum number of transmitters to install
Input Format

The first line contains two space-separated integers  and , the number of houses in Hackerland and the range of each transmitter.
The second line contains  space-separated integers describing the respective locations of each house .

Constraints

There may be more than one house at the same location.
Subtasks

 for  of the maximum score.
Output Format

Print a single integer denoting the minimum number of transmitters needed to cover all of the houses.

Sample Input 0

STDIN       Function
-----       --------
5 1         x[] size n = 5, k = 1
1 2 3 4 5   x = [1, 2, 3, 4, 5]  
Sample Output 0

2
Explanation 0

The diagram below depicts our map of Hackerland:

k-nearest(2).png

We can cover the entire city by installing  transmitters on houses at locations  and .

Sample Input 1

8 2
7 2 4 6 5 9 12 11 
Sample Output 1

3
Explanation 1

The diagram below depicts our map of Hackerland:

k-nearest2(2).png

We can cover the entire city by installing  transmitters on houses at locations , , and .
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

def hackerlandRadioTransmitters(x, k):
    if (len(x) == 0):
        return 0
        
    x.sort()
    
    ans = 1
    s_pos = x[0]    
    s_index = 0
    i_pos = 0
    i_index = 0    
    
    found = True
    while found:
        for i in range(s_index, len(x)):
            if x[i] - s_pos <= k:
                ipos = x[i]
                i_index = i
            else:
                break
        
        e_pos = ipos + k
        #print(ipos, s_pos, e_pos)
        
        found = False
        for i in range(i_index + 1, len(x)):
            if x[i] > e_pos:
                s_pos = x[i]
                s_index = i
                ans += 1
                #print("inc: ", e_pos, s_pos, s_index, ans)
                found = True
                break
                
    return ans
        
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()