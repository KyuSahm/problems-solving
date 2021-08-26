'''
235. Lowest Common Ancestor of a Binary Search Tree
Easy

3866

147

Add to List

Share
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).” 

Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
Accepted
574,445
Submissions
1,061,704
Seen this question in a real interview before?
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def dfs(self, parent, node_dict):
        if parent.left != None:
            node_dict[parent.left.val] = (parent.left, parent)
            #print(parent.left.val, parent.left, parent)
            self.dfs(parent.left, node_dict)
        
        if parent.right != None:
            #print(parent.right.val, parent.right, parent)
            node_dict[parent.right.val] = (parent.right, parent)
            self.dfs(parent.right, node_dict)
        return    
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node_dict = {}        
        node_dict[root.val] = (root, None)
        #print(root.val, root, None)
        
        
        self.dfs(root, node_dict)       
        
        
        #print(len(node_dict))
        
        p_node, p_parent = node_dict[p.val]        
        q_node, q_parent = node_dict[q.val]
        
        while True:
            while True:
                if p_node.val == q_node.val:
                    return p_node
                else:
                    if q_parent == None:
                        break
                    else:
                        q_node, q_parent = node_dict[q_parent.val] 
            q_node, q_parent = node_dict[q.val]
            
            if p_parent == None:
                break
            else:
                p_node, p_parent = node_dict[p_parent.val]
                
        return None

from collections import deque

class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node_dict = {}        
        
        queue = deque()
        queue.append((1, root))
        node_dict[1] = root
                     
        p_index = 0
        q_index = 0
                     
        while queue:
            i, node = queue.popleft()
            node_dict[i] = node
                     
            if node.val == p.val:         
                p_index = i
            elif node.val == q.val:         
                q_index = i
                     
            left = 2 * i
            right = left + 1
           
            if node.left != None:
                queue.append((left, node.left))
           
            if node.right != None:
                queue.append((right, node.right))
        
        while True:
            if p_index == 0 or q_index == 0:
                break
            if p_index == q_index:
                return node_dict[p_index]
            elif p_index > q_index:
                 p_index = p_index // 2
            elif q_index > p_index:
                 q_index = q_index // 2
                    
        return None

class Solution3:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if root.val<p.val and root.val<q.val:
                root = root.right
            elif root.val>p.val and root.val>q.val:
                root = root.left
            else:
                return root

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (p.val <= root.val and q.val >= root.val) or (p.val >= root.val and q.val <= root.val):
            return root
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
