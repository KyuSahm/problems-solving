'''
"leetcode"
130. Surrounded Regions
Medium

3365

866

Add to List

Share
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
Example 2:

Input: board = [["X"]]
Output: [["X"]]
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
'''
# implementation with bfs
from collections import deque
class Solution:
    def bfs(self, board, visited, n, m, i, j):
        offset = [(0, 1), (0, -1), (1, 0), (-1, 0)]        
        b_faced = False
        
        flip = []
        q = deque()
        q.append((i, j))        
        while q:
            x, y = q.popleft()
            if visited[x][y]:
                continue
                
            if x == 0 or x == n - 1 or y == 0 or y == m - 1:
                b_faced = True
                
            #print(x, y)    
            visited[x][y] = True
            flip.append((x, y))
            
            for dx, dy in offset:
                new_x = x + dx
                new_y = y + dy
                
                #print(new_x, new_y, visited[new_x][new_y], board[new_x][new_y])    
                if (0 <= new_x < n and 0 <= new_y < m and
                    board[new_x][new_y] == 'O' and not visited[new_x][new_y]):
                    q.append((new_x, new_y))
                
        if not b_faced:
            for x, y in flip:
                board[x][y] = 'X'
        
    def solve(self, board: list[list[str]]) -> None:
        #print(board)
        
        n = len(board)
        m = len(board[0])
        
        visited = [[False] * m for _ in range(n)]
        
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and not visited[i][j]:
                    self.bfs(board, visited, n, m, i, j)
        
        #print(board)
        
        """
        Do not return anything, modify board in-place instead.
        """       