class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        A subsequence is a sequence derived by deleting some or no characters without changing the order of the remaining elements. 
        To find the longest common subsequence (LCS) of two strings, we compare characters one by one. 
        If the current characters match, they contribute to the LCS, and we move both pointers forward. 
        If they don't match, we try skipping a character from either string and take the best result. 
        This naturally leads to a recursive approach that explores all possibilities.

        The recursive solution recalculates the same subproblems many times. 
        For example, dfs(2, 3) might be called from multiple branches. 
        By storing results in a memo table, we avoid redundant work. 
        This transforms the exponential solution into a polynomial one.

        """

        memo = {}

        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + dfs(i+1, j+1)
            else:
                memo[(i, j)] = max(dfs(i+1, j), dfs(i, j+1))

            return memo[(i, j)]
        
        return dfs(0,0)