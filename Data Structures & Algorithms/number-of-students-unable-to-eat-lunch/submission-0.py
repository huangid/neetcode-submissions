class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches = deque(sandwiches)
        while sandwiches:
            if not (sandwiches[0] in students):
                break
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
            else:
                s = students.popleft()
                students.append(s)
        return len(students)