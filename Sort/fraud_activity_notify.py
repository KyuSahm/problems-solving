'''
"HackerRank"
HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. If the amount spent by a client on a particular day is greater than or equal to  the client's median spending for a trailing number of days, they send the client a notification about potential fraud. The bank doesn't send the client any notifications until they have at least that trailing number of prior days' transaction data.

Given the number of trailing days  and a client's total daily expenditures for a period of  days, determine the number of times the client will receive a notification over all  days.

Example


On the first three days, they just collect spending data. At day , trailing expenditures are . The median is  and the day's expenditure is . Because , there will be a notice. The next day, trailing expenditures are  and the expenditures are . This is less than  so no notice will be sent. Over the period, there was one notice sent.

Note: The median of a list of numbers can be found by first sorting the numbers ascending. If there is an odd number of values, the middle one is picked. If there is an even number of values, the median is then defined to be the average of the two middle values. (Wikipedia)

Function Description

Complete the function activityNotifications in the editor below.

activityNotifications has the following parameter(s):

int expenditure[n]: daily expenditures
int d: the lookback days for median spending
Returns

int: the number of notices sent
Input Format

The first line contains two space-separated integers  and , the number of days of transaction data, and the number of trailing days' data used to calculate median spending respectively.
The second line contains  space-separated non-negative integers where each integer  denotes .

Constraints

Output Format

Sample Input 0

STDIN               Function
-----               --------
9 5                 expenditure[] size n =9, d = 5
2 3 4 2 3 6 8 4 5   expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
Sample Output 0

2
Explanation 0

Determine the total number of  the client receives over a period of  days. For the first five days, the customer receives no notifications because the bank has insufficient transaction data: .

On the sixth day, the bank has  days of prior transaction data, , and  dollars. The client spends  dollars, which triggers a notification because : .

On the seventh day, the bank has  days of prior transaction data, , and  dollars. The client spends  dollars, which triggers a notification because : .

On the eighth day, the bank has  days of prior transaction data, , and  dollars. The client spends  dollars, which does not trigger a notification because : .

On the ninth day, the bank has  days of prior transaction data, , and a transaction median of  dollars. The client spends  dollars, which does not trigger a notification because : .

Sample Input 1

5 4
1 2 3 4 4
Sample Output 1

0
There are  days of data required so the first day a notice might go out is day . Our trailing expenditures
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#
'''
# insert sort version => timeout
def insert(a, pos, pos_dict, data):
    a[pos] = data    
    pos_dict[data[1]] = pos
    for i in range(pos, 0, -1):
        if a[i] < a[i - 1]:
            a[i], a[i - 1] = a[i - 1], a[i]
            pos_dict[a[i][1]] = i
            pos_dict[a[i - 1][1]] = i - 1
            break
            
def delete(a, pos, pos_dict, d):
    i = pos_dict[pos]
    del pos_dict[pos]
    
    for j in range(i + 1, d):
        a[j], a[j - 1] = a[j - 1], a[j]
        pos_dict[a[j][1]] = j
        pos_dict[a[j - 1][1]] = j - 1
            
            
def activityNotifications(expenditure, d):
    pos_dict = dict()
    
    a = [(0, 0) for _ in range(d)]
    
    # init
    for i in range(d):
        insert(a, i, pos_dict, (expenditure[i], i))
    
    n = 0    
    for i in range(d, len(expenditure)):
        if d % 2 == 1:
            m = a[d // 2][0]
        else:
            m = (a[d // 2 - 1][0] + a[d // 2][0]) / 2
        
        if expenditure[i] >= 2 * m:
            n += 1
        
        delete(a, i - d, pos_dict, d)
        if i + 1 < len(expenditure):
            insert(a, d - 1, pos_dict, (expenditure[i + 1], i + 1))
            
    return n
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#
def get_med(cnt, m, n):
    c = 0    
    med_low = 0
    med_high = 0
    m_found = False
    for j in range(len(cnt)):
        c += cnt[j]
        if c >= m and not m_found:
            med_low = j
            m_found = True
        if c >= n:
            med_high = j
            break
    med = (med_low + med_high) / 2.0
    return med        

# counting version because data is integer >= 0 and data range <= 200        
def activityNotifications(expenditure, d):
    MAX_LEN = int(201)
    
    cnt = [0] * MAX_LEN
    
    if d % 2 == 1:
        m = d // 2 + 1
        n = d // 2 + 1
    else:
        m = d // 2     
        n = d // 2 + 1
            
    for i in range(d):
        cnt[expenditure[i]] += 1
    
    ans = 0
    for i in range(d, len(expenditure)):
        med = get_med(cnt, m, n)
        if expenditure[i] >= 2 * med:
            ans += 1
            
        cnt[expenditure[i - d]] -= 1
        cnt[expenditure[i]] += 1
        
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()