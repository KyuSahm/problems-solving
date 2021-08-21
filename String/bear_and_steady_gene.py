'''
HackerRank
A gene is represented as a string of length  (where  is divisible by ), composed of the letters , , , and . It is considered to be steady if each of the four letters occurs exactly  times. For example,  and  are both steady genes.

Bear Limak is a famous biotechnology scientist who specializes in modifying bear DNA to make it steady. Right now, he is examining a gene represented as a string . It is not necessarily steady. Fortunately, Limak can choose one (maybe empty) substring of  and replace it with any string of the same length.

Modifying a large substring of bear genes can be dangerous. Given a string , can you help Limak find the length of the smallest possible substring that he can replace to make  a steady gene?

Note: A substring of a string  is a subsequence made up of zero or more contiguous characters of .

As an example, consider . The substring  just before or after  can be replaced with  or . One selection would create .

Function Description

Complete the  function in the editor below. It should return an integer that represents the length of the smallest substring to replace.

steadyGene has the following parameter:

gene: a string
Input Format

The first line contains an interger  divisible by , that denotes the length of a string .
The second line contains a string  of length .

Constraints

 is divisible by 
Subtask

 in tests worth  points.
Output Format

Print the length of the minimum length substring that can be replaced to make  stable.

Sample Input

8  
GAAATAAA
Sample Output

5
Explanation

One optimal solution is to replace  with  resulting in .
The replaced substring has length .
'''
import math
import os
import random
import re
import sys

#
# Complete the 'steadyGene' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING gene as parameter.
#
def steadyGene(gene):
    INF = int(1e9)
    g_len = len(gene)
    s_cnt = g_len // 4
    
    total_cnt = {'C': 0, 'G': 0, 'A': 0, 'T':0}
    need_cnt  = {'C': 0, 'G': 0, 'A': 0, 'T':0}
    
    for c in gene:
        total_cnt[c] += 1
    
    found = False
    for key in total_cnt.keys():
        if total_cnt[key] > s_cnt:
            need_cnt[key] = total_cnt[key] - s_cnt
            found = True
    
    if not found:
        return 0
    
    #print(total_cnt, need_cnt)
        
    min_val = INF
    start = 0
    end = 0
    substr_cnt  = {'C': 0, 'G': 0, 'A': 0, 'T':0}
   
    # seek start position with character necessary removing
    while True:
        if need_cnt[gene[start]] != 0:
            break
        else:    
            start += 1
    
    # seek end position with contenting with condition        
    for i in range(start, g_len):
        substr_cnt[gene[i]] += 1
        if (substr_cnt['C'] >= need_cnt['C'] and substr_cnt['G'] >= need_cnt['G'] and
            substr_cnt['A'] >= need_cnt['A'] and substr_cnt['T'] >= need_cnt['T']):
            end = i
            min_val = min(min_val, end - start + 1)
            break
            
    #print(start, end, min_val)    
                
    while True:
        # seek next start position with character necessary removing        
        while start < end:        
            substr_cnt[gene[start]] -= 1
            start += 1
            if need_cnt[gene[start]] > 0:
                break
        
        # even if some characters at start positons is removed, can be content with condition         
        if (substr_cnt['C'] >= need_cnt['C'] and substr_cnt['G'] >= need_cnt['G'] and
            substr_cnt['A'] >= need_cnt['A'] and substr_cnt['T'] >= need_cnt['T']):
            min_val = min(min_val, end - start + 1)
            continue
                        
        found = False        
        for j in range(end + 1, g_len):
            substr_cnt[gene[j]] += 1
            if (substr_cnt['C'] >= need_cnt['C'] and substr_cnt['G'] >= need_cnt['G'] and
                substr_cnt['A'] >= need_cnt['A'] and substr_cnt['T'] >= need_cnt['T']):
                found = True
                end = j
                min_val = min(min_val, end - start + 1)
                break
        if not found:
            break
    return min_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gene = input()

    result = steadyGene(gene)

    fptr.write(str(result) + '\n')

    fptr.close()