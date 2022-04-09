'''
"leet code" medium level
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''
class Solution:
    def dfs(self, head, l_cnt, r_cnt):
        if l_cnt == 0 and r_cnt == 0:
            self.ans.append(head)
        
        if l_cnt > 0:
            self.dfs(head + '(', l_cnt - 1, r_cnt)
            
        if l_cnt < r_cnt:
            self.dfs(head + ')', l_cnt, r_cnt - 1) 
        return        
        
    def generateParenthesis(self, n: int) -> list[str]:
        self.ans = []
        
        l_cnt = r_cnt = n
        self.dfs('', l_cnt, r_cnt)
        print(n)
        
        return self.ans