'''
"leet code"
11. Container With Most Water
Medium

11390

773

Add to List

Share
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
Example 3:

Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2
 

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''
'''
timeout solution
class Solution:    
    def maxArea(self, height: list[int]) -> int:
        s_c = []
        e_c = []
        
        mh = 0
        for i in range(len(height) - 1):
            if height[i] > mh:
                s_c.append((i, height[i]))
                mh = height[i]
        mh = 0
        for i in range(len(height) - 1, 0, -1):
            if height[i] > mh:
                e_c.append((i, height[i]))
                mh = height[i]
        
        #print(s_c, e_c)
        
        s_c.reverse()
        e_c.reverse()
        
        #print(s_c, e_c)
        ans = 0
        
        for s, s_h in s_c:
            for e, e_h in e_c:
                if e <= s:
                    continue
                hv = min(s_h, e_h)
                if hv * (e - s) > ans:
                    ans = hv * (e - s)
        return ans
'''
class Solution:
    def maxArea(self, height: list[int]) -> int:
        ans = 0        
        left = 0
        right = len(height) -1 
        while left < right:
            while left < right and height[right] < height[left]:                
                ans = max((right - left) * min(height[left], height[right]), ans)
                right -= 1
            ans = max((right - left) * min(height[left], height[right]), ans)
            left += 1
                    
        return ans