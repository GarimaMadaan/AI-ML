class Student:
    college_name = "ABC College"
    pi = 3.1

    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa
        self.pi = 3.14

student1 = Student("Garima", 8.67)
student2 = Student("Aditya", 9.2)

print(student1.name)
print(Student.college_name)
print(student1.college_name)

print(student1.pi)
print(Student.pi)