'''
"Hacker Rank"
Consider a matrix where each cell contains either a  or a . Any cell containing a  is called a filled cell. Two cells are said to be connected if they are adjacent to each other horizontally, vertically, or diagonally. In the following grid, all cells marked X are connected to the cell marked Y.

XXX
XYX  
XXX    
If one or more filled cells are also connected, they form a region. Note that each cell in a region is connected to zero or more cells in the region but is not necessarily directly connected to all the other cells in the region.

Given an  matrix, find and print the number of cells in the largest region in the matrix. Note that there may be more than one region in the matrix.

For example, there are two regions in the following  matrix. The larger region at the top left contains  cells. The smaller one at the bottom right contains .

110
100
001
Function Description

Complete the connectedCell function in the editor below.

connectedCell has the following parameter(s):
- int matrix[n][m]:  represents the  row of the matrix

Returns
- int: the area of the largest region

Input Format

The first line contains an integer , the number of rows in the matrix.
The second line contains an integer , the number of columns in the matrix.
Each of the next  lines contains  space-separated integers .

Constraints

Sample Input

STDIN       Function
-----       --------
4           n = 4
4           m = 4
1 1 0 0     grid = [[1, 1, 1, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
0 1 1 0
0 0 1 0
1 0 0 0
Sample Output

5
Explanation

The diagram below depicts two regions of the matrix. Connected regions are filled with X or Y. Zeros are replaced with dots for clarity.

X X . .
. X X .
. . X .
Y . . .
The larger region has  cells, marked X.
'''

#!/bin/python3
import math
import os
import random
import re
import sys
from collections import deque
#
# Complete the 'connectedCell' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

'''
DFS Version with recursive call
'''
cnt = 0
def dfs(matrix, visited, offset, x, y):
    for dx, dy in offset:
        new_x = x + dx
        new_y = y + dy
        if (0 <= new_x < n and 0 <= new_y < m and
            matrix[new_x][new_y] == 1 and not visited[new_x][new_y]):
            visited[new_x][new_y] = True
            global cnt
            cnt += 1                
            dfs(matrix, visited, offset, new_x, new_y)
                               
def connectedCell_dfs_call(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    visited = [[False] * m for _ in range(n)]
    #print(visited)
    offset = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    max_cnt = 0
    for x in range(n):
        for y in range(m):
            if matrix[x][y] == 1 and not visited[x][y]:
                visited[x][y] = True
                global cnt
                cnt = 1                
                dfs(matrix, visited, offset, x, y)
                max_cnt = max(max_cnt, cnt)                
                
    return max_cnt

'''
DFS Version with stack
'''
def connectedCell_dfs_stack(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    visited = [[False] * m for _ in range(n)]
    offset = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    max_cnt = 0
    stack = []
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and not visited[i][j]:
                cnt = 1
                visited[i][j] = True  
                stack.append((i, j))
                while stack:
                    x, y = stack[-1]
                    
                    found = False
                    for dx, dy in offset:
                        new_x = x + dx
                        new_y = y + dy
                        if (0 <= new_x < n and 0 <= new_y < m and
                            matrix[new_x][new_y] == 1 and not visited[new_x][new_y]): 
                            cnt += 1
                            visited[new_x][new_y] = True
                            stack.append((new_x, new_y))
                            found = True
                            break
                    if not found:
                        stack.pop()
                        
                max_cnt = max(max_cnt, cnt)                
                
    return max_cnt

'''
BFS version with queue
'''
def connectedCell(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    visited = [[False] * m for _ in range(n)]
    #print(visited)
    offset = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    max_cnt = 0
    q = deque() 
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and not visited[i][j]:
                #q.clear() 
                q.append((i, j))                
                cnt = 0
                while q:
                    x, y = q.popleft()
                    if not visited[x][y]:
                        cnt += 1                    
                        max_cnt = max(max_cnt, cnt)                    
                        visited[x][y] = True                    
                        for dx, dy in offset:
                            new_x = x + dx
                            new_y = y + dy                            
                            if (0 <= new_x < n and 0 <= new_y < m and
                                matrix[new_x][new_y] == 1 and not visited[new_x][new_y]):
                                q.append((new_x, new_y))
    return max_cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)

    fptr.write(str(result) + '\n')

    fptr.close()