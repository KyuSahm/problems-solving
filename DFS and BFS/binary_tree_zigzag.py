'''
"leetcode"
103. Binary Tree Zigzag Level Order Traversal
Medium

4223

140

Add to List

Share
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
'''

from collections import deque

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution1:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        data = dict()        
        pre_level = -1
        q = deque()
        
        if root != None:
            q.append((root, 0))        
        while q:
            node, level = q.popleft()
            
            if level != pre_level:
                pre_level = level
                data[level] = [node]
            else:
                data[level].append(node)
                
            if node.left != None:
                q.append((node.left, level + 1))                    
            if node.right != None:
                q.append((node.right, level + 1))
                   
        ans = []
        forward = True
        for k in data.keys():
            ans.append([])
            if forward:
                for d in data[k]:
                    ans[k].append(d.val)
                forward = False
            else:
                for j in range(len(data[k]) - 1, -1, -1):
                    ans[k].append(data[k][j].val)
                forward = True
                
        return ans

class Solution2:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        to_right_stack = []
        to_left_stack = []
        
        ans = []
        if root != None:
            to_right_stack.append((root, 0))
        while to_right_stack or to_left_stack:
            if to_right_stack:
                ans.append([])
                
            while to_right_stack:
                node, level = to_right_stack.pop()
                ans[level].append(node.val)
                if node.left != None:
                    to_left_stack.append((node.left, level + 1))
                if node.right != None:
                    to_left_stack.append((node.right, level + 1))
            
            if to_left_stack:
                ans.append([])
            
            while to_left_stack:
                node, level = to_left_stack.pop()
                ans[level].append(node.val)
                if node.right != None:
                    to_right_stack.append((node.right, level + 1))
                if node.left != None:
                    to_right_stack.append((node.left, level + 1))
                    
        return ans        