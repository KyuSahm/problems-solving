'''
Hacker's rank
Given a set of distinct integers, print the size of a maximal subset of  where the sum of any  numbers in  is not evenly divisible by .

Example 

One of the arrays that can be created is . Another is . After testing all permutations, the maximum length solution array has  elements.

Function Description

Complete the nonDivisibleSubset function in the editor below.

nonDivisibleSubset has the following parameter(s):

int S[n]: an array of integers
int k: the divisor
Returns

int: the length of the longest subset of  meeting the criteria
Input Format

The first line contains  space-separated integers,  and , the number of values in  and the non factor.
The second line contains  space-separated integers, each an , the unique values of the set.

Constraints

All of the given numbers are distinct.
Sample Input

STDIN    Function
-----    --------
4 3      S[] size n = 4, k = 3
1 7 2 4  S = [1, 7, 2, 4]
Sample Output

3
Explanation

The sums of all permutations of two elements from  are:

1 + 7 = 8
1 + 2 = 3
1 + 4 = 5
7 + 2 = 9
7 + 4 = 11
2 + 4 = 6
Only  will not ever sum to a multiple of
'''
import math
import os
import random
import re
import sys
#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

# timeout
def nonDivisibleSubset1(k, s):
    #sequence = []
    
    while True:
        count = [[i, 0] for i in range(len(s))]
        
        found = False
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if (s[i] + s[j]) % k == 0:
                    count[i][1] += 1
                    count[j][1] += 1
                    found = True
                    #sequence.append((i, j))
        
        if found:            
            max_val = 0
            max_index = 0            
            for i in range(len(s)):
                if count[i][1] > max_val:
                    max_index = i
                    max_val = count[i][1]
            s.pop(max_index)
        else:
            break
        
    return len(s)

# timeout
def nonDivisibleSubset2(k, s):
    count = [[i, []] for i in range(len(s))]
    
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if (s[i] + s[j]) % k == 0:
                count[i][1].append(j)
                count[j][1].append(i)
                
    #print(count)            
    total_cnt = len(s)
    while True:
        max_value = 0
        max_index = 0
        
        for i in range(len(count)):
            if len(count[i][1]) > max_value:
                max_index = i
                max_value = len(count[i][1])
        
        #print(max_value)        
        if max_value == 0:
            break      
    
        for j in count[max_index][1]:
            count[j][1].remove(max_index)
            
        count[max_index][1] = []
        total_cnt -= 1
    
    return total_cnt

# 나머지가 1인 것은 (k-1)인 것을 더하면, 나머지가 0이됨.
# 둘 중 개수가 적은 것을 버리는 것이 유리.
def nonDivisibleSubset(k, s):
    count = [0] * k
    
    for a in s:
        r = a % k
        count[r] += 1
    
    num = len(s)
    
    if count[0] > 1:
        num = num - (count[0] - 1)
    
    if k % 2 == 0 and count[k // 2] > 0:
        num = num - (count[k // 2] - 1)
        last = k // 2 - 1
    else:
        last = k // 2
        
    for i in range(1, last + 1):
        if count[i] >= count[k - i]:
            num = num - (count[k - i])
        else:
            num = num - count[i]
            
    return num

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset2(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()