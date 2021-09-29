'''
"HackerRank"
Consider an undirected graph where each edge weighs 6 units. Each of the nodes is labeled consecutively from 1 to n.

You will be given a number of queries. For each query, you will be given a list of edges describing an undirected graph. After you create a representation of the graph, you must determine and report the shortest distance to each of the other nodes from a given starting position using the breadth-first search algorithm (BFS). Return an array of distances from the start node in node number order. If a node is unreachable, return  for that node.

Example
The following graph is based on the listed inputs:

image
 // number of nodes
 // number of edges

 // starting node

All distances are from the start node . Outputs are calculated for distances to nodes  through : . Each edge is  units, and the unreachable node  has the required return distance of .

Function Description

Complete the bfs function in the editor below. If a node is unreachable, its distance is .

bfs has the following parameter(s):

int n: the number of nodes
int m: the number of edges
int edges[m][2]: start and end nodes for edges
int s: the node to start traversals from
Returns
int[n-1]: the distances to nodes in increasing node number order, not including the start node (-1 if a node is not reachable)

Input Format

The first line contains an integer , the number of queries. Each of the following  sets of lines has the following format:

The first line contains two space-separated integers  and , the number of nodes and edges in the graph.
Each line  of the  subsequent lines contains two space-separated integers,  and , that describe an edge between nodes  and .
The last line contains a single integer, , the node number to start from.
Constraints

Sample Input

2
4 2
1 2
1 3
1
3 1
2 3
2
Sample Output

6 6 -1
-1 6
Explanation

We perform the following two queries:

The given graph can be represented as:
image
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#
from collections import deque

def bfs(n, m, edges, s):
    dist = [-1 for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    
    # create connection info
    # cycle exists
    for f, t in edges:
        if t not in graph[f]:
            graph[f].append(t)
        if f not in graph[t]:
            graph[t].append(f)
        
    #print(graph)    
    q = deque()
    q.append((0, s))
    
    while q:
        d, v = q.popleft()
        
        # first visit means shorted distance
        if not visited[v]:
            dist[v] = d
            visited[v] = True
        
        for c in graph[v]:
            # prevent cycle visit
            if not visited[c]:
                q.append((d + 1, c))
    
    ans = []
    
    for i in range(1, n + 1):
        if dist[i] != 0:
            if dist[i] != -1:
                ans.append(dist[i] * 6)
            else:
                ans.append(dist[i])    
    
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()