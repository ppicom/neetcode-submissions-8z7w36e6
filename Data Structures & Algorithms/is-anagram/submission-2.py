class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        if len(s) != len(t):
            return False

        for c in s:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
        
        for c in t:
            if c not in chars:
                return False
            else:
                if chars[c] == 1:
                    del chars[c]
                else:
                    chars[c] -= 1
        
        return True