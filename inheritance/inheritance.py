class Employee:
    start_time = "10 am"
    end_time = "6 pm"

    def change_time(self, new_end_time):
        self.end_time = new_end_time

class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject

class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role

class Accountant(AdminStaff):
    def __init__(self, role, salary):
        super().__init__(role)
        self.salary = salary

t1  = Teacher("Math")
a1 = AdminStaff("HR Manager")
acc1 = Accountant("Accountant", 50000)

print(t1.subject, t1.start_time, t1.end_time) # Math 10 am 6 pm
print(a1.role, a1.start_time, a1.end_time) # HR Manager 10 am 6 pm
print(acc1.salary, acc1.start_time, acc1.end_time) # 50000 10 am 6 pm