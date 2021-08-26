'''
"leet code"
101. Symmetric Tree
Easy

7063

183

Add to List

Share
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
 

Follow up: Could you solve it both recursively and iteratively?
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def bfs_left(self, left_root):
        q = deque()
        q.append((1, left_root))
        
        left = []
        while q:
            seq, node = q.popleft()
            left.append((seq, node.val))            
            if node.left != None:
                q.append((seq * 2, node.left))
            if node.right != None:
                q.append((seq * 2 + 1, node.right))
        return left
    
    def bfs_right(self, right_root):
        q = deque()
        q.append((1, right_root))
        
        right = []
        while q:
            seq, node = q.popleft()
            right.append((seq, node.val))            
            if node.right != None:
                q.append((seq * 2, node.right))
            if node.left != None:
                q.append((seq * 2 + 1, node.left))
        return right
    
    def isSymmetric(self, root:TreeNode) -> bool:
        if root.left == None and root.right == None:
            return True
        
        if root.left == None and root.right != None:
            return False
        
        if root.left != None and root.right == None:
            return False
        
        left = self.bfs_left(root.left)
        right = self.bfs_right(root.right)
        
        if len(left) != len(right):
            return False
        else:
            for i in range(len(left)):
                if left[i][0] != right[i][0] or left[i][1] != right[i][1]:
                    return False
        
        return True
'''
class Solution {
    public boolean isSame(TreeNode p, TreeNode q){
        if(p == null && q == null)
            return true;
        
        if(p == null || q == null)
            return false;
        
        if(p.val != q.val)
            return false;
        
        return isSame(p.left, q.right) && isSame(p.right, q.left);
    }
    
    public boolean isSymmetric(TreeNode root) {
        return isSame(root, root);
    }
}
'''        