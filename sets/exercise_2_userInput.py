students = {}
num = int(input("How many students?: "))
for i in range(num):
    k = input("Enter key(roll no): ")
    v = input("Enter value(student name): ")
    students.update({k: v})
print("\nNo of students")
for i in students:
    print(i, students[i])
students.update({7: "raghav"})
print("\nAdding other student ..")
for i in students:
    print(i, students[i])
print("\nreplacing other student ...")
students["3"] = "daksh"
for i in students:
    print(i, students[i])

