students = {
    1: "jasleen",
    2: "ishita",
    3: "nandni",
    4: "charvi",
    5: "yamini",
    6: "aaryan",
}
for i in students:
    print(i, students[i])
print("\nNo of students")
print(len(students))
print("\nAdding other student ..")
students.update({7: "raghav"})
for i in students:
    print(i, students[i])

print("\nreplacing other student ...")
students[3] = "daksh"
for i in students:
    print(i, students[i])
# sorted dictionry
print("\nsorting student...")
students_sort = sorted(students.items())
for i in students_sort:
    print(i)
