'''
"HackerRank"
There is an undirected tree where each vertex is numbered from  to , and each contains a data value. The sum of a tree is the sum of all its nodes' data values. If an edge is cut, two smaller trees are formed. The difference between two trees is the absolute value of the difference in their sums.

Given a tree, determine which edge to cut so that the resulting trees have a minimal difference between them, then return that difference.

Example


In this case, node numbers match their weights for convenience. The graph is shown below.

image

The values are calculated as follows:

Edge    Tree 1  Tree 2  Absolute
Cut     Sum      Sum     Difference
1        8         13         5
2        9         12         3
3        6         15         9
4        4         17        13
5        5         16        11
The minimum absolute difference is .

Note: The given tree is always rooted at vertex .

Function Description

Complete the cutTheTree function in the editor below.

cutTheTree has the following parameter(s):

int data[n]: an array of integers that represent node values
int edges[n-1][2]: an 2 dimensional array of integer pairs where each pair represents nodes connected by the edge
Returns

int: the minimum achievable absolute difference of tree sums
Input Format

The first line contains an integer , the number of vertices in the tree.
The second line contains  space-separated integers, where each integer  denotes the  data value, .
Each of the  subsequent lines contains two space-separated integers  and  that describe edge  in tree .

Constraints

, where .
Sample Input

STDIN                       Function
-----                       --------
6                           data[] size n = 6
100 200 100 500 100 600     data = [100, 200, 100, 500, 100, 600]
1 2                         edges = [[1, 2], [2, 3], [2, 5], [4, 5], [5, 6]]
2 3
2 5
4 5
5 6
Sample Output

400
Explanation

We can visualize the initial, uncut tree as:

cut-the-tree.png

There are  edges we can cut:

Edge  results in 
Edge  results in 
Edge  results in 
Edge  results in 
Edge  results in 
The minimum difference is .
'''
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'cutTheTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY data
#  2. 2D_INTEGER_ARRAY edges
#
def find_root(root, a):
    if root[a] != a:
        root[a] = find_root(root, root[a])
    return root[a]    
    
def union_root(root, a, b):
    x = find_root(root, a)    
    y = find_root(root, b)
    
    if x < y:
        root[y] = x
    else:
        root[y] = x    

def calc_weight_diff(data, edges):
    root = [i for i in range(len(data) + 1)]    
    for a, b in edges:
        union_root(root, a, b)
    
    data_sum = dict()
    
    for i in range(1, len(data) + 1):
        r = find_root(root, i)
        #print('parent: ', i, r, data[r - 1])
        if r in data_sum:
            data_sum[r] += data[i - 1]
        else:
            data_sum[r] = data[i - 1]
    
    #print(data_sum)    
    k = list(data_sum.keys())    
    a = data_sum[k[0]]
    b = data_sum[k[1]]
    
    return abs(a - b)

# use disjoint set    
def cutTheTree_1(data, edges):
    ans = int(1e9)
    for i in range(len(edges)):
        new_edges = edges[0:i] + edges[i+1:len(edges)]
        ans = min(ans, calc_weight_diff(data, new_edges))
        
    return ans

# use BFS
def cutTheTree_2(data, edges):
    ans = int(1e9)
    e = [[] for i in range(len(data) + 1)]    
    
    for a, b in edges:
        e[a].append(b) 
        e[b].append(a)
    
    #print(e)
    ab_sum = sum(data)
    q = deque()
    for a, b in edges:
        v = [False for i in range(len(data) + 1)]
        #print(a, b, v)
        
        a_sum = 0        
        q.append(a)        
        while q:
            n = q.popleft()
            #print(n, v[n])
            if not v[n]:
                a_sum += data[n - 1]
                #print(a, a_sum, data[n-1])                
                v[n] = True
                for m in e[n]:
                    if not v[m] and m != b:
                        q.append(m)
                                    
        #print(a, a_sum)
        b_sum = ab_sum - a_sum
        ans = min(abs(a_sum - b_sum), ans)
        
    return ans

ans = int(1e9)
tot = 0

def dfs(data, e, v, parent):
    p_node = parent
    v[p_node] = True
    #print("visit: ", p_node)
    
    child = []
    for c_node in e[p_node]:
        if not v[c_node]:
            child.append(c_node)
    
    ac_sum = data[p_node -1]    
    for i in range(len(child)):
        ac_sum += dfs(data, e, v, child[i])
        
    global ans                        
    ans = min(ans, abs(tot - 2 * ac_sum))    
    return ac_sum            
            
# dfs with recursive call =>
# runtime error because of stack overflow       
def cutTheTree_3(data, edges):
    e = [[] for i in range(len(data) + 1)]    
    v = [False for i in range(len(data) + 1)]    
    
    for a, b in edges:
        e[a].append(b) 
        e[b].append(a)
    
    global tot
    tot = sum(data)
    
    #print(data, edges, e)    
    parent = 1    
    dfs(data, e, v, parent) 
    
    global ans    
    return ans

# dfs with stack => ok
def cutTheTree(data, edges):
    # edge information
    e = [[] for _ in range(len(data) + 1)]
    # decendant information
    d = [[] for _ in range(len(data) + 1)]
    # visited flag information
    v = [False for _ in range(len(data) + 1)]    
    
    for a, b in edges:
        e[a].append(b) 
        e[b].append(a)
    
    # total sum of data    
    tot = sum(data)
    ans = int(1e9)    

    root = 1
    stack = []
    v[root] = True    
    stack.append(root) # push root into stack
    while stack:
        p_node = stack[-1]
        
        found = False
        for c in e[p_node]:
            if not v[c]:
                v[c] = True
                # append decendent information
                d[p_node].append(c)
                stack.append(c)                
                found = True
                break
            
        if not found:
            # sum parent with children
            for a in d[p_node]:
                data[p_node - 1] += data[a - 1]            
            ans = min(ans, abs(tot - 2 * data[p_node - 1]))            
            stack.pop()    
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    edges = []

    for _ in range(n - 1):
        edges.append(list(map(int, input().rstrip().split())))

    result = cutTheTree(data, edges)

    fptr.write(str(result) + '\n')

    fptr.close()