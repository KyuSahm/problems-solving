'''
"leet code"
1054. Distant Barcodes
Medium

675

30

Add to List

Share
In a warehouse, there is a row of barcodes, where the ith barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer, and it is guaranteed an answer exists.

 

Example 1:

Input: barcodes = [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
Example 2:

Input: barcodes = [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,1,2,1,2]
 

Constraints:

1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000

'''
import heapq

class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        num_cnt = dict()
        
        for c in barcodes:
            if c not in num_cnt:
                num_cnt[c] = 1
            else:
                num_cnt[c] += 1
                
        q = []        
        for key in num_cnt.keys():
            heapq.heappush(q, (-num_cnt[key], key))
        
        ans = []
        b_cnt = 0
        b_key = None
        while q:
            a_cnt, a_key = heapq.heappop(q)
            ans.append(a_key)
            if b_key != None and b_cnt != -1:
                heapq.heappush(q, (b_cnt + 1, b_key))
                               
            if q:
                b_cnt, b_key = heapq.heappop(q)
                ans.append(b_key)                
            else:
                b_key = None
            
            if a_cnt != -1:
                heapq.heappush(q, (a_cnt + 1, a_key))                                   
        return ans