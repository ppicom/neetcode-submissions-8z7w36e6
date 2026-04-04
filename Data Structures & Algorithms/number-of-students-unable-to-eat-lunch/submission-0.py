class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students:
            next_student = students.pop(0)
            if next_student == sandwiches[0]:
                sandwiches.pop(0)
            else:
                students.append(next_student)

            if not sandwiches:
                continue
            
            next_sandwich = sandwiches[0]
            someone_wants_it = False
            for remaining_student in students:
                if remaining_student == next_sandwich:
                    someone_wants_it = True
            
            if not someone_wants_it:
                break
        
        return len(students)