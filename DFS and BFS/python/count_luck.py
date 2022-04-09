'''
"HackerRank"
on and Hermione are deep in the Forbidden Forest collecting potion ingredients, and they've managed to lose their way. The path out of the forest is blocked, so they must make their way to a portkey that will transport them back to Hogwarts.

Consider the forest as an  grid. Each cell is either empty (represented by .) or blocked by a tree (represented by ). Ron and Hermione can move (together inside a single cell) LEFT, RIGHT, UP, and DOWN through empty cells, but they cannot travel through a tree cell. Their starting cell is marked with the character , and the cell with the portkey is marked with a . The upper-left corner is indexed as .

.X.X......X
.X*.X.XXX.X
.XX.X.XM...
......XXXX.
In example above, Ron and Hermione are located at index  and the portkey is at . Each cell is indexed according to Matrix Conventions.

Hermione decides it's time to find the portkey and leave. They start along the path and each time they have to choose a direction, she waves her wand and it points to the correct direction. Ron is betting that she will have to wave her wand exactly  times. Can you determine if Ron's guesses are correct?

The map from above has been redrawn with the path indicated as a series where  is the starting point (no decision in this case),  indicates a decision point and  is just a step on the path:

.X.X.10000X
.X*0X0XXX0X
.XX0X0XM01.
...100XXXX.
There are three instances marked with  where Hermione must use her wand.

Note: It is guaranteed that there is only one path from the starting location to the portkey.

Function Description

Complete the countLuck function in the editor below. It should return a string, either  if Ron is correct or  if he is not.

countLuck has the following parameters:

matrix: a list of strings, each one represents a row of the matrix
k: an integer that represents Ron's guess
Input Format

The first line contains an integer , the number of test cases.

Each test case is described as follows:
The first line contains  space-separated integers  and , the number of forest matrix rows and columns.
Each of the next  lines contains a string of length  describing a row of the forest matrix.
The last line contains an integer , Ron's guess as to how many times Hermione will wave her wand.

Constraints

There will be exactly one  and one  in the forest.
Exactly one path exists between  and .
Output Format

On a new line for each test case, print  if Ron impresses Hermione by guessing correctly. Otherwise, print .

Sample Input

3
2 3
*.M
.X.
1
4 11
.X.X......X
.X*.X.XXX.X
.XX.X.XM...
......XXXX.
3
4 11
.X.X......X
.X*.X.XXX.X
.XX.X.XM...
......XXXX.
4
Sample Output

Impressed
Impressed
Oops!
Explanation

For each test case,  denotes the number of times Hermione waves her wand.

Case 0: Hermione waves her wand at , giving us . Because , we print  on a new line.
Case 1: Hermione waves her wand at , , and , giving us . Because , we print  on a new line.
Case 2: Hermione waves her wand at , , and , giving us . Because  and ,  and we print  on a new line.
'''
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'countLuck' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY matrix
#  2. INTEGER k
#
def countLuck(matrix, k):
    n = len(matrix)
    m = len(matrix[0])
    
    visited = [[False] * m for _ in range(n)]
    
    #print(matrix, k, n, m)    
    start = (0, 0)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'M':
                start = (i, j)
                
    #print(start, k)    
    offset = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque()
    
    # x, y, cnt
    q.append((start[0], start[1], 0))    
    ans = 0
    while q:
        x, y, cnt = q.popleft()
        visited[x][y] = True
        
        #print(x, y, cnt)
        found = False
        temp = []        
        for dx, dy in offset:
            new_x = x + dx
            new_y = y + dy
            
            if (0 <= new_x < n and 0 <= new_y < m and not visited[new_x][new_y]):
                #print("new: ", new_x, new_y, cnt)
                if matrix[new_x][new_y] == '.':
                    temp.append((new_x, new_y))
                elif matrix[new_x][new_y] == '*':
                    temp.append((new_x, new_y))
                    found = True
        
        if len(temp) >= 2:
            cnt += 1
                    
        if found:
            ans = cnt
            break        
        else:    
            for a, b in temp:
                q.append((a, b, cnt))
    
    if ans == k:
        return "Impressed"
    else:
        return "Oops!"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input().strip())

        result = countLuck(matrix, k)

        fptr.write(result + '\n')

    fptr.close()