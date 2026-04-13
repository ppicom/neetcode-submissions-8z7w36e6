class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Since the problem guarantees lowercase English letters, we can use a fixed-size array of length 26 to count character frequencies instead of a hash map."""
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True