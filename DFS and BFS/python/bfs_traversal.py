'''
"leet code"
102. Binary Tree Level Order Traversal
Medium

5575

117

Add to List

Share
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: [] 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''
# Definition for a binary tree node.
from collections import deque

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution1:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        q = deque()        
        if root != None:
            q.append((0, root))
        
        temp_answer = [[] for _ in range(2000)]
        level = -1
        
        while q:
            level, node = q.popleft()
            
            temp_answer[level].append(node.val)
            
            if node.left != None:
                q.append((level + 1, node.left))            
            if node.right != None:
                q.append((level + 1, node.right))
        
        answer = temp_answer[0:level + 1]
        
        return answer

class Solution2:
    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        ans = []
        q = deque()
        
        if root != None:
            q.append((0, root))            
        
        prev_level = -1        
        while q:
            level, node = q.popleft()
            
            if level > prev_level:
                ans.append([])
                prev_level = level
            
            ans[level].append(node.val)
            
            if node.left != None:
                q.append((level + 1, node.left))            
            if node.right != None:
                q.append((level + 1, node.right))
        
        return ans