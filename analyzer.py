import csv

students = [
    {
        "name": "Alice",
        "study_hours": 12,
        "exam_score": 92
    },
    {
        "name": "Ben",
        "study_hours": 8,
        "exam_score": 84
    },
    {
        "name": "Claire",
        "study_hours": 15,
        "exam_score": 96
    }
]

# for loop that goes through each dictionary and finds the key "name"
for student in students:
    print(f"{student['name']}: {student['study_hours']} hours, {student['exam_score']}%")

def calculate_average_score():
    total_score = 0

    for student in students:
        total_score += student["exam_score"]

    average_score = total_score / len(students)
    print(f"Average exam score: {average_score:.2f}%")

def calculate_average_study_hours():
    total_hours = 0
    
    for student in students:
        total_hours += student["study_hours"]
    
    average_hours = total_hours / len(students)
    print(f"Average study hours: {average_study_hours:.2f} hours")

def calculate_average(field):
    if not students:
        return None

    total = 0

    for student in students:
        total += student[field]

    average = total / len(students)

    return average

def load_students():
    # empty list
    students = []
    # opens students.csv in read mode
    with open("students.csv", "r") as file:
        
        reads each row as a dictionary, column names are the keys
        reader = csv.DictReader(file)
        
        for row in reader:
            # adding students info to the list
            students = {
                "name": row["name"],
                "study_hours": int(row["study_hours"])
                "exam_score": int(row["exam_score"])
            }
            students.append(student)
    return students

def find_highest_score():
    if not students:
        return None
    highest_student = students[0]
    for student in students:
        if student["exam_score"] > highest_student["exam_score"]:
            highest_student = student
    return highest_student

def find_lowest_score():
    if not students:
        return None
    lowest_student = students[0]
    for student in students:
        if student["exam_score"] < lowest_student["exam_score"]:
            lowest_student = student
    return lowest_student
