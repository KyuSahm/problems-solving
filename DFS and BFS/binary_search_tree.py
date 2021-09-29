'''
98. Validate Binary Search Tree
Medium

7191

752

Add to List

Share
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 

Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# dfs with recursive call
class Solution:
    def dfs(self, node, min_val, max_val):
        if min_val < node.val < max_val:
            if node.left != None:
                if not self.dfs(node.left, min_val, node.val):
                    return False
                    
            if node.right != None:
                if not self.dfs(node.right, node.val, max_val):
                    return False
            return True    
        else:
            return False        
        
    def isValidBST(self, root: TreeNode) -> bool:        
        INF = int(2147483648)
        M_INF = int(-2147483649)
        
        ans = self.dfs(root, M_INF, INF)
        return ans

# Solution with dfs on stack. faster than recursive call
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        INF = int(2147483648)
        M_INF = int(-2147483649)
        
        stack = []
        visited = dict()
        visited[1] = True
        stack.append((root, 1, M_INF, INF))
        
        while stack:
            parent, n, min_val, max_val = stack[-1]
            
            left = n * 2
            right = left + 1            
            all_child_visited = True
            left_child = parent.left            
            if left_child != None and left not in visited:
                all_child_visited = False
                if min_val < left_child.val < parent.val:
                    visited[left] = True
                    stack.append((left_child, left, min_val, parent.val))                    
                    continue
                else:
                    return False
                
            right_child = parent.right    
            if right_child != None and right not in visited:                
                all_child_visited = False
                if parent.val < right_child.val < max_val:                    
                    visited[right] = True
                    stack.append((right_child, right, parent.val, max_val))
                    continue
                else:
                    return False 
                
            if all_child_visited:
                stack.pop()
        return True