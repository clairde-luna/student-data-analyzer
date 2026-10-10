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
    total = 0
    for student in students:
        total += student[field]

    average = total / len(students)

    if field == "exam_score":
        label = "exam score"
    elif field == "study_hours":
        label == "study hours"
    print(f"Average {field}: {average:.2f}")

def greet(name):
    print(f"Hello, {name}!")

calculate_average_score()
calculate_average_study_hours()
