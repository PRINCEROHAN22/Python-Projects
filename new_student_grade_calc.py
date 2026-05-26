def get_marks(student):
    subjects = ["Math", "Science", "English", "History", "computer"]
    marks = {}
    print(f"Enter marks for {student} out of 100: ")
    for subject in subjects:
        while True:
            try:
                mark = float(input(f"{subject}: "))
                if 0<= mark <=100:
                    marks[subject] = mark
                    break
                else:
                    print("Please enter a valid mark between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    return marks

def calculate_grade(average_marks):
    if average_marks >=90:
        return "A+"
    elif average_marks >=80:
        return "A"
    elif average_marks >=70:
        return "B"
    elif average_marks >=60:
        return "C"
    elif average_marks >=50:
        return "D"
    else:
        return "F"
    
def display_result(student, marks):
    total_marks = sum(marks.values())
    average_marks = total_marks / len(marks)
    grade = calculate_grade(average_marks)
    print("\n"+"-"*40)
    print(f"        RESULT CARD FOR {student.upper()}       ")
    print("-"*40)
    for subject, mark in marks.items():
        print(f"{subject:<10}: {mark:.1f}")

    print("-"*40)
    print(f"{'Total Marks':<10}: {total_marks:.1f}")
    print(f"{'Average Marks':<10}: {average_marks:.2f}")
    print(f"{'Grade':<10}: {grade}")
    print("-"*40)

    if grade == "F":
        print("Unfortunately, you have failed. Please try again.")
    elif grade == "A+":
        print("Excellent work! You have achieved an A+ grade!")
    else:
        print("Congratulations! You have passed, keep up the good work!")

    print("-"*40)


print("========welcome to the Student Grade Calculator!========")
student_name = input("Enter the student's name: ")
marks = get_marks(student_name)
display_result(student_name, marks)

