'''
"HackerRank"
 is a chess piece that moves in an L shape. We define the possible moves of  as any movement from some position  to some  satisfying either of the following:

 and , or
 and 
Note that  and  allow for the same exact set of movements. For example, the diagram below depicts the possible locations that  or  can move to from its current location at the center of a  chessboard:

image

Observe that for each possible movement, the Knight moves  units in one direction (i.e., horizontal or vertical) and  unit in the perpendicular direction.

Given the value of  for an  chessboard, answer the following question for each  pair where :

What is the minimum number of moves it takes for  to get from position  to position ? If it's not possible for the Knight to reach that destination, the answer is -1 instead.
Then print the answer for each  according to the Output Format specified below.

Input Format

A single integer denoting .

Constraints

Output Format

Print exactly  lines of output in which each line  (where ) contains  space-separated integers describing the minimum number of moves  must make for each respective  (where ). If some  cannot reach position , print -1 instead.

For example, if , we organize the answers for all the  pairs in our output like this:

(1,1) (1,2)
(2,1) (2,2)
Sample Input 0

5
Sample Output 0

4 4 2 8
4 2 4 4
2 4 -1 -1
8 4 -1 1
Explanation 0

The diagram below depicts possible minimal paths for , , and :

image

One minimal path for  is:

We then print 4 4 2 8 as our first line of output because  took  moves,  took  moves,  took  moves, and  took  moves.

In some of the later rows of output, it's impossible for  to reach position . For example,  can only move back and forth between  and  so it will never reach .
'''
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'knightlOnAChessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def bfs(a, b, n):
    visited = [[False] * n for i in range(n)]
    offset = [(a, b), (a, -b), (-a, b), (-a, -b), (b, a), (b, -a), (-b, a), (-b, -a)]
    
    cnt = 0
    q = deque()
    q.append((0, 0, 0))    
    found = False
    while q:
        x, y, cnt = q.popleft()
        
        if visited[x][y]:
            continue
        
        if x == n - 1 and y == n - 1:
            found = True
            break
        
        visited[x][y] = True
        for dx, dy in offset:
            new_x = x + dx
            new_y = y + dy
            
            if 0 <= new_x < n and 0 <= new_y < n and not visited[new_x][new_y]:
                q.append((new_x, new_y, cnt + 1))

    if found:             
        return cnt
    else:
        return -1

def knightlOnAChessboard(n):
    result = [ [0] * (n - 1) for i in range(n - 1)]
    
    print(result)
    for a in range(1, n):
        for b in range(1, n):
            if a > b:
                result[a - 1][b - 1] = result[b - 1][a - 1]
            else:    
                result[a - 1][b - 1] = bfs(a, b, n)
    #print(result)    
    return result
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()