class Student:
    def __init__(self, name,cgpa):
        self.name = name
        print("Constructor was called")

    def get_cgpa(self):
        return self.cgpa    

student1 = Student("Garima", 8.67)
student2 = Student("Aditya", 9.2)

print(student1.name)
print(student2.name)

print(student1.get_cgpa())
print(student2.get_cgpa())
