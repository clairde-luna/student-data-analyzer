import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
students = pd.read_csv("students.csv")

# Remove rows with missing values
students = students.dropna()

# Convert columns to numeric values
students["student_hours"] = pd.to_numeric(
  students["study_hours"], errors="coerce"
)

students["exam_score"] = pd.tonumeric(
  students["exam_score"], errors="corerce"
)

# Remove rows that became missing after conversion
students = students.dropna()

# Keep only valid records
students = students[
  (students["name"].str.strip() != "") &
  (students["study_hours"] >= 0)
  & (students["exam_score"] >= 0)
  & (students["exam_score"] <= 100)
]

# Creating a bar chart
plt.bar(students["name"], students["exam_score"])

plt.title("Exam Score by Student")
plt.xlabel("Student")
plt.ylabel("Exam Score (%)")

plt.ylim(0, 100)

average_score = students["exam_score"].mean()
plt.axhline(average_score, linestyle="--", label="Class Average")
plt.tight_layout()

plt.savefig("exam_scores.png")
plt.show()
