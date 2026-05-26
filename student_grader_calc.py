def get_marks(student_name):
    sub_names = ["Math", "Science", "English", "History", "computer"]
    marks={}
    print(f"Enter marks for {student_name} (out of 100):")
    for sub in sub_names:
        while True:
            try:
                mark = float(input(f"{sub}: "))
                if 0 <= mark <= 100:
                    marks[sub] = mark
                    break
                else:
                    print("Please enter a valid mark between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    return marks

def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"
    
def display_result(student_name, marks):
    total_marks = sum(marks.values())
    average = total_marks / len(marks)
    grade = calculate_grade(average)

    print("\n" + "="*40)
    print(f"      RESULTS CARD - {student_name.upper()}")
    print("="*40)

    for subject, mark in marks.items():
        print(f"{subject:<12}: {mark:.1f}")

    print("-"*40)
    print(f"{'Total Marks':<12}: {total_marks:.1f}")
    print(f"{'Average':<12}: {average:.2f}")
    print(f"{'Grade':<12}: {grade}")
    print("="*40)

    if grade == "F":
        print("Unfortunately, you have failed. Please work harder and try again.")
    else:
        print("Congratulations! You have passed. Keep up the good work!")
    print("="*40) 

print("===== Welcome to the Student Grader Calculator =====")
student_name = input("Enter the student's name: ")
marks = get_marks(student_name)
print(display_result(student_name, marks))