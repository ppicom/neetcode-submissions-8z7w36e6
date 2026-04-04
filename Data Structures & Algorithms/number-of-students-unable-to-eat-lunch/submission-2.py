class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [0, 0]
        for s in students:
            count[s] += 1
        
        for sandwich in sandwiches:
            if count[sandwich] == 0:
                return count[1 - sandwich]
            count[sandwich] -= 1
        
        return 0