'''
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
'''


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        dict={}
        for pairs in dislikes:
            if pairs[0] in dict:
                dict[pairs[0]].add(pairs[1])
            else:
                dict[pairs[0]]=set([pairs[1]])
            if pairs[1] in dict:
                dict[pairs[1]].add(pairs[0])
            else:
                dict[pairs[1]]=set([pairs[0]])
                
        seen={}
        for i in range(1,N+1):
            if i not in seen:
                seen[i]=0
                stack = [i]
                while stack:
                    a=stack.pop()
                    if a in dict:
                        for b in dict[a]:
                            if b in seen:
                                if seen[a] ==  seen[b]:
                                    return False
                            else:
                                seen[b] = (seen[a]+1)%2
                                stack.append(b)
            
        return True       
        
