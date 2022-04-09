'''
"leetcode"
34. Find First and Last Position of Element in Sorted Array
Medium

6994

231

Add to List

Share
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) - 1
        
        mid = 0
        found = False
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                found = True
                break
        ans = []        
        if found:
            start = mid
            for i in range(mid - 1, -1, -1):
                if nums[i] == target:
                    start = i
                else:
                    break
            end = mid
            for i in range(mid + 1, len(nums)):
                if nums[i] == target:
                    end = i
                else:
                    break                    
            ans.append(start)
            ans.append(end)
        else:
            ans = [-1, -1]
        return ans