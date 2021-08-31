'''
HackerRank's problem
Lauren has a chart of distinct projected prices for a house over the next several years. She must buy the house in one year and sell it in another, and she must do so at a loss. She wants to minimize her financial loss.

Example

Her minimum loss is incurred by purchasing in year  at  and reselling in year  at . Return .

Function Description

Complete the minimumLoss function in the editor below.

minimumLoss has the following parameter(s):

int price[n]: home prices at each year
Returns

int: the minimum loss possible
Input Format

The first line contains an integer , the number of years of house data.
The second line contains  space-separated long integers that describe each .

Constraints

All the prices are distinct.
A valid answer exists.
Subtasks

 for  of the maximum score.
Sample Input 0

3
5 10 3
Sample Output 0

2
Explanation 0

Lauren buys the house in year  at  and sells it in year  at  for a minimal loss of .

Sample Input 1

5
20 7 8 2 5
Sample Output 1

2
Explanation 1

Lauren buys the house in year  at  and sells it in year  at  for a minimal loss of .
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#
def minimumLoss(price):
    data = []
    for i in range(len(price)):
        data.append((price[i], i))
    
    # reverse sort with price
    data.sort(key = lambda x:x[0], reverse=True)

    INF = int(1e9)
    min_loss = INF
    
    for i in range(len(data)):
        s_price, s_year = data[i]
        for j in range(i + 1, len(data)):
            e_price, e_year = data[j]
            # if first output with the codition,
            # calculate min_loss and break loop for performance
            if e_year > s_year and s_price > e_price:
                min_loss = min(min_loss, s_price - e_price)
                break
    
    return min_loss

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()