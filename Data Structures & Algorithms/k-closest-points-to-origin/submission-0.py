class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts_dst = []
        for p in points:
            dst = math.sqrt((p[0] - 0)**2 + (p[1] - 0)**2)
            pts_dst.append((dst, p))
        
        heapq.heapify(pts_dst)
        res = [pt_dst[1] for pt_dst in heapq.nsmallest(k, pts_dst, key=lambda x: x[0])]
        return res