# Student Marks Analyzer
students = [
    ("Aman", 78),
    ("Riya", 92),
    ("Aman", 85),
    ("Kiran", 92),
    ("Riya", 92),
    ("Dev", 70)
]
#1
unique_name = set()
for name, marks in students:
    unique_name.add(name)
print(unique_name)
#2
highest_marks = []
for name,marks in students:
    if marks>80:
        highest_marks.append(name)
print(highest_marks)
#3
visited = set()
duplicate = set()
for name,marks in students:
    if name in visited:
        duplicate.add(name)
    else:
        visited.add(name)
print(duplicate)
#4
Topper = max(students)
print(Topper)
