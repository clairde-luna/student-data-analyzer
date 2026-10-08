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

total_score = 0

for student in students:
    total_score += student["exam_score"]

average_score = ten_score / len(students)
print(f"Average exam score: {average_score:.2f}%")
