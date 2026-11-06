# Practice Problem 2: Student Grade Calculator
Bangla_marks = int(input("Enter Bangla marks: "))
English_marks = int(input("Enter English marks: "))
Math_marks = int(input("Enter Math marks: "))

marks = [Bangla_marks, English_marks,Math_marks]
student_name = input("Enter student name: ")

if any(mark < 0 or mark > 100 for mark in marks):
    print("Invalid marks: each subject mark must be between 0 and 100.")
else:
    average = sum(marks) / len(marks)

    if average >= 80:
        grade = "A+"
    elif average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "A-"
    elif average >= 50:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "F"

    print(f"Student Name: {student_name}")
    print(f"Average Marks: {average:.2f}")
    print(f"Final Grade: {grade}")