'''
"leetcode"
113. Path Sum II
Medium

3605

95

Add to List

Share
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import copy
class Solution:
   def dfs(self, parent, v_list, cur_sum, target_sum):
        if parent.left == None and parent.right == None:
            if cur_sum == target_sum:
                self.ans.append(v_list)
        else:        
            if parent.left != None:
                self.dfs(parent.left, v_list + [parent.left.val], cur_sum + parent.left.val, target_sum)
            if parent.right != None:
                self.dfs(parent.right, v_list + [parent.right.val], cur_sum + parent.right.val, target_sum)

    def dfs1(self, parent, v_list, cur_sum, target_sum):
        if parent.left == None and parent.right == None:
            if cur_sum == target_sum:
                self.ans.append(copy.deepcopy(v_list))
        else:        
            if parent.left != None:
                v_list.append(parent.left.val)
                self.dfs(parent.left, v_list, cur_sum + parent.left.val, target_sum)
                v_list.pop()
            if parent.right != None:
                v_list.append(parent.right.val)
                self.dfs(parent.right, v_list, cur_sum + parent.right.val, target_sum)
                v_list.pop()    

    def pathSum(self, root: TreeNode, targetSum: int) -> list[list[int]]:
        self.ans = []
        
        if root != None:
            self.dfs(root, [root.val], root.val, targetSum)
        
        return self.ans        