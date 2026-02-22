courses = []
grades = []

course_count = int(input("How many courses will you enter: "))

for i in range(course_count):
    course_name = input(f"{i+1}. course name: ")

    grade = int(input("Enter grade (0-100): "))
    while grade < 0 or grade > 100:
        print("Invalid grade! Enter between 0-100.")
        grade = int(input("Enter grade (0-100): "))

    courses.append(course_name)
    grades.append(grade)

total = sum(grades)
average = total / course_count

print("Average:", average)

if 90 <= average <= 100:
    letter = "AA"
elif 85 <= average <= 89:
    letter = "BA"
elif 80 <= average <= 84:
    letter = "BB"
elif 75 <= average <= 79:
    letter = "CB"
elif 70 <= average <= 74:
    letter = "CC"
elif 65 <= average <= 69:
    letter = "DC"
elif 60 <= average <= 64:
    letter = "DD"
elif 50 <= average <= 59:
    letter = "FD"
else:
    letter = "FF"

print("Letter Grade:", letter)
print("Status:", "Passed" if average >= 50 else "Failed")


def find_highest_grade(courses, grades):
    highest = max(grades)
    index = grades.index(highest)
    print(f"Highest grade: {highest} ({courses[index]})")


def find_lowest_grade(courses, grades):
    lowest = min(grades)
    index = grades.index(lowest)
    print(f"Lowest grade: {lowest} ({courses[index]})")


find_highest_grade(courses, grades)
find_lowest_grade(courses, grades)