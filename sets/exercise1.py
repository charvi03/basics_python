students = {
    1: "jasleen",
    2: "ishita",
    3: "nandni",
    4: "charvi",
    5: "yamini",
    6: "aaryan",
}
print(students)
print("no. of students in class are :", len(students))
print("\nAdding other student ...")
students.update({7: "raghav"})
print(students)
print("\nreplacing other student ...")
students[3] = "daksh"
print(students)
# sorted dictionry
print("\nsorting student...")
students_sort = sorted(students.items())
print(students_sort)
