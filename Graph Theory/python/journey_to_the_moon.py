'''
"HackerRank"
he member states of the UN are planning to send  people to the moon. They want them to be from different countries. You will be given a list of pairs of astronaut ID's. Each pair is made of astronauts from the same country. Determine how many pairs of astronauts from different countries they can choose from.

Example



There are  astronauts numbered  through . Astronauts grouped by country are  and . There are  pairs to choose from:  and .

Function Description

Complete the journeyToMoon function in the editor below.

journeyToMoon has the following parameter(s):

int n: the number of astronauts
int astronaut[p][2]: each element  is a  element array that represents the ID's of two astronauts from the same country
Returns
- int: the number of valid pairs

Input Format

The first line contains two integers  and , the number of astronauts and the number of pairs.
Each of the next  lines contains  space-separated integers denoting astronaut ID's of two who share the same nationality.

Constraints

Sample Input 0

5 3
0 1
2 3
0 4
Sample Output 0

6
Explanation 0

Persons numbered  belong to one country, and those numbered  belong to another. The UN has  ways of choosing a pair:


Sample Input 1

4 1
0 2
Sample Output 1

5
Explanation 1

Persons numbered  belong to the same country, but persons  and  don't share countries with anyone else. The UN has  ways of choosing a pair:

아래의 테스트케이스를 통과시키려면, 

입력:
100000 2
1 2
3 4

출력:
4999949998

'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#
'''
def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]
    
def union_parent(parent, a, b):
    x = find_parent(parent, a)
    y = find_parent(parent, b)
    
    if x < y:
        parent[y] = x
    else:
        parent[x] = y    
    

def journeyToMoon(n, astronaut):
    parent = [i for i in range(n)]
    
    for a, b in astronaut:
        union_parent(parent, a, b)
    
    parent_dict = dict()    
    for a in range(0, n):
        p = find_parent(parent, a)
        
        if p not in parent_dict:
            parent_dict[p] = 1
        else:
            parent_dict[p] += 1
    
    #print(parent)                
    #print(parent_dict)        
    
    count = []
    for v in parent_dict.values():
        count.append(v)
    
    ans = 0    
    for i in range(len(count)):
        for j in range(i + 1, len(count)):
           ans += count[i] * count[j]
        
    return ans
'''
def find_parent(parent, a):
    # For performence enhancement
    if a not in parent:
        parent[a] = a
    else:
        if parent[a] != a:
            parent[a] = find_parent(parent, parent[a])
    return parent[a]
    
def union_parent(parent, a, b):
    x = find_parent(parent, a)
    y = find_parent(parent, b)
    
    if x < y:
        parent[y] = x
    elif y < x:
        parent[x] = y    
    

def journeyToMoon(n, astronaut):
    parent = dict()    
    for a, b in astronaut:
        union_parent(parent, a, b)
    
    parent_cnt = dict()
    for key in parent.keys():
        p_key = find_parent(parent, key)
        
        if p_key not in parent_cnt:
            parent_cnt[p_key] = 1
        else:
            parent_cnt[p_key] += 1
        
    count = []
    for v in parent_cnt.values():        
        count.append(v)
    
    # For performence enhancement
    s = n - sum(parent_cnt.values())
    count.append(s)
        
    #print(count)
    ans = 0    
    for i in range(len(count)):
        for j in range(i + 1, len(count)):
           ans += count[i] * count[j]
    
    # For performence enhancement
    if s > 1:
        sub_ans = 0
        for i in range(1, s):
            sub_ans += i
        ans += sub_ans
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + '\n')

    fptr.close()