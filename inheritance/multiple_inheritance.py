class Teacher:
    def __init__(self, salary):
        self.salary = salary

class Student:
    def __init__(self, gpa):
        self.gpa = gpa

class TA(Teacher, Student):
    def __init__(self, salary, gpa, name):
        super().__init__(salary)
        Student.__init__(self, gpa)
        self.name = name

ta1 = TA(30000, 3.8, "Alice")
print(ta1.name) # Alice
print(ta1.salary) # 30000  
print(ta1.gpa) # 3.8