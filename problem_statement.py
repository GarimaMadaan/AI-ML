info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Charlie", "English"),
    ("Alice", "English")

]

# Unique courses offered
course = set()
for info_tuple in info:
    course.add(info_tuple[1])
print("Offered courses:", list(course)) 

# Students enrolled in English course
english_students = []
for info_tuple in info:
    if info_tuple[1] == "English":
        english_students.append(info_tuple[0])
print("Students enrolled in English course:", english_students)


dict = {}
for name,course in info:
    if(dict.get(name) == None):
        dict.update({name : set()})
    dict[name].add(course)

print("Student enrollments:", dict)
