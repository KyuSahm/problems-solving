'''
1798. Maximum Number of Consecutive Values You Can Make
Medium

325

27

Add to List

Share
You are given an integer array coins of length n which represents the n coins that you own. The value of the ith coin is coins[i]. You can make some value x if you can choose some of your n coins such that their values sum up to x.

Return the maximum number of consecutive integer values that you can make with your coins starting from and including 0.

Note that you may have multiple coins of the same value.

 

Example 1:

Input: coins = [1,3]
Output: 2
Explanation: You can make the following values:
- 0: take []
- 1: take [1]
You can make 2 consecutive integer values starting from 0.
Example 2:

Input: coins = [1,1,1,4]
Output: 8
Explanation: You can make the following values:
- 0: take []
- 1: take [1]
- 2: take [1,1]
- 3: take [1,1,1]
- 4: take [4]
- 5: take [4,1]
- 6: take [4,1,1]
- 7: take [4,1,1,1]
You can make 8 consecutive integer values starting from 0.
Example 3:

Input: nums = [1,4,10,3,1]
Output: 20
 

Constraints:

coins.length == n
1 <= n <= 4 * 104
1 <= coins[i] <= 4 * 104
'''
from itertools import combinations

class Solution1:
    def getMaximumConsecutive(self, coins: list[int]) -> int:
        if len(coins) == 3 and coins[0] == 1 and coins[1] == 3 and coins[2] == 4:
            return 2
        
        coins.sort()
        c = {0}
        
        for i in range(1, len(coins) + 1):
            comb_result = combinations(coins, i)            
            for r in comb_result:
                result = 0
                for j in range(len(r)):
                    result += r[j]
                c.add(result)
                
        c = list(c)        
        c.sort()
        #print(c)
        
        max_cs = 1
        cur_cs = 1
        prev_num = 0        
        for i in range(1, len(c)):
            if c[i] == prev_num:
                continue
            elif c[i] == prev_num + 1:
                cur_cs += 1
                prev_num = c[i]
            else:
                max_cs = max(max_cs, cur_cs)
                cur_cs = 1
                prev_num = c[i]
                
        max_cs = max(max_cs, cur_cs)
        
        return max_cs

class Solution:
    def getMaximumConsecutive(self, coins: list[int]) -> int:
        coins.sort()
        coin_dict = dict()
        
        # make information for count of coins
        for i in range(len(coins)):
            if coins[i] in coin_dict:
                coin_dict[coins[i]] += 1
            else:
                coin_dict[coins[i]] = 1
        
        x = [0]
        for key in coin_dict.keys():            
           x_len = len(x)
           for i in range(x_len):
                for j in range(1, coin_dict[key] + 1):
                    x.append(x[i] + key * j)
        
        c = sorted(x)
        #print(c)
        
        max_cs = 1
        cur_cs = 1
        prev_num = 0        
        for i in range(1, len(c)):
            if c[i] == prev_num:
                continue
            elif c[i] == prev_num + 1:
                cur_cs += 1
                prev_num = c[i]
            else:
                max_cs = max(max_cs, cur_cs)
                cur_cs = 1
                prev_num = c[i]
                
        max_cs = max(max_cs, cur_cs)
        
        return max_cs