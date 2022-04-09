'''
"leetcode"
74. Search a 2D Matrix
Medium

4291

214

Add to List

Share
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        print(matrix, target)
        row_s = 0
        row_e = len(matrix) - 1
        
        col_s = 0
        col_e = len(matrix[0]) - 1
        
        while row_s <= row_e:
            row_m = (row_s + row_e) // 2
            
            if target < matrix[row_m][0]:
                row_e = row_m - 1
            elif target > matrix[row_m][col_e]:
                row_s = row_m + 1
            else:                
                while col_s <= col_e:
                    col_m = (col_s + col_e) // 2
                    if target > matrix[row_m][col_m]:
                        col_s = col_m + 1
                    elif target < matrix[row_m][col_m]:
                        col_e = col_m - 1
                    else:
                        return True
                return False
        return False