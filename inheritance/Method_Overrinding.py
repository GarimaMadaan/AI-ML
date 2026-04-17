class Employee:
    def get_deignation(self):
        print("Designation: Employee")
        
class Teacher(Employee):
    def get_deignation(self):
        print("Designation: Teacher")

t1 = Teacher()
t1.get_deignation() # Designation: Teacher

