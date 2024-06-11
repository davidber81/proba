grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

def get_stud_grad(students: set, grades: list) -> dict:
    grades_of_students = {}
    students = sorted(students)
    for i in range(len(students)):
        grades_of_students[students[i]] = sum(grades[i]) / len(grades[i])
    return grades_of_students

res = get_stud_grad(students, grades)
print(res)