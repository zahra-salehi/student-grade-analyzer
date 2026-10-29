def calculate_average(student):
    average = (student["mathematics"] + student["python"] + student["english"]) / 3
    return average

def validate_grades(student):
    for subject in ["mathematics", "python", "english"]:
        if student[subject] < 0 or student[subject] > 100:
            return False
    return True

def analyze_students(students):
    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
        if not validate_grades(student):
            print("Invalid grade for", student["name"])
            return
    
    total = 0
    highest_average = calculate_average(students[0])
    top_student = students[0]["name"]
    lowest_average = calculate_average(students[0])
    lowest_student = students[0]["name"]

    with open("student_report.txt", "w") as file:
        for student in students:
            average = calculate_average(student)
            total = average + total

            if average >= 60:
                status = "Passed"
            else:
                status = "Failed"

            file.write(student["name"] + ": " + str(round(average, 2)) + ", " + status + "\n")

            if average > highest_average:
                highest_average = average
                top_student = student["name"]

            if average < lowest_average:
                lowest_average = average
                lowest_student = student["name"]

        class_average = total / len(students)
            
        file.write("Class Average: " + str(round(class_average, 2)) + "\n")
        file.write("Top student: " + top_student + ", Highest average: " + str(round(highest_average, 2)) + "\n")
        file.write("Lowest student: " + lowest_student + ", Lowest average: " + str(round(lowest_average, 2)) + "\n")
            
students = [{"name": "Alice",
    "mathematics": 85,
    "python": 92,
    "english": 78},
    {"name": "Bob",
    "mathematics": 70,
    "python": 65,
    "english": 80},
    {"name": "Carol",
    "mathematics": 95,
    "python": 88,
    "english": 91},
    {"name": "David",
    "mathematics": 55,
    "python": 60,
    "english": 58}]         
                
analyze_students(students)
