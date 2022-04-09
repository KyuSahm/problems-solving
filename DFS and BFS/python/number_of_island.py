'''
"leetcode"
200. Number of Islands
Medium

10096

269

Add to List

Share
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
Accepted
'''
from collections import deque

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        
        visited = [[False] * m for _ in range(n)]
        #print(n, m)
        
        ans = 0
        offset = [(1, 0), (-1, 0), (0, 1), (0, -1)] 
        q = deque() 
        for i in range(n):
            for j in range(m):
                if visited[i][j] or grid[i][j] == '0':
                    continue
                
                #print(i, j)
                ans += 1
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    
                    if visited[x][y]:
                        continue
                    visited[x][y] = True
                    #print("visited: ", x, y)
                    for dx, dy in offset:
                        new_x = x + dx
                        new_y = y + dy
                        if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == '1':
                            q.append((new_x, new_y))
        #print(ans)
        return ans