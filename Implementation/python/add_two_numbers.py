'''
2. Add Two Numbers
Medium

13473

3028

Add to List

Share
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''
# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = []
        prev_val = 0
        while l1 != None or l2 != None:
            r = prev_val
            if l1 != None:
                r += l1.val
            if l2 != None:
                r += l2.val
                
            a.append(r % 10)
            prev_val = r // 10
            
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
                
        if prev_val != 0:
            a.append(prev_val)
        
        answer = None
        for i in range(len(a) - 1, -1, -1):
            answer = ListNode(a[i], answer)
        
        return answer

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        answer = ListNode()
        node = answer
        carry = 0
        while True:
            r = carry
            if l1 != None:
                r += l1.val
            if l2 != None:
                r += l2.val
            
            node.val = r % 10
            carry = r // 10
            
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
                
            if l1 == None and l2 == None and carry == 0:
                break;
            node.next = ListNode()
            node = node.next
        
        return answer        