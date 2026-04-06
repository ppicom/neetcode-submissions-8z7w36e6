class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        m = (l+r) // 2
        best_guess = l

        while l<=r:
            m = (l+r)//2
            if self._is_correct(piles, m, h):
                best_guess = m
                r = m -1
            else:
                l = m + 1
        
        return best_guess
    
    def _is_correct(self, piles: List[int], k: int, h: int) -> int:
        return sum((p + k - 1) // k for p in piles) <= h
        