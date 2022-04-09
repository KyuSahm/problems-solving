'''
"leetcode"
Next Permutation
Medium

6870

2241

Add to List

Share
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
'''
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        right = len(nums) - 1
        left = 0
        
        found = False
        for i in range(right, left, -1):
            # find ascending order
            if nums[i] <= nums[i - 1]:
                continue
            else:
                # find swapping value
                for j in range(right, i - 1, -1):
                    if nums[j] > nums[i - 1]:
                        nums[i - 1], nums[j] = nums[j], nums[i - 1]
                        break
                # sort array in ranges        
                for j in range(i, right):
                    if j < right - (j - i):
                        nums[j], nums[right - (j - i)] = nums[right - (j - i)], nums[j] 
                    else:
                        break
                found = True        
                break
                
        if not found:
            nums.sort()
            
        """
        Do not return anything, modify nums in-place instead.
        """       