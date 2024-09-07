student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    new_mark = ""
    if student_scores[key] >= 91:
        new_mark = "Outstanding"
    elif student_scores[key] >= 81:
        new_mark = "Exceeds Expectations"
    elif student_scores[key] >= 71:
        new_mark = "Acceptable"
    else:
        new_mark = "Fail"

    student_grades[key] = new_mark

print(student_grades)
