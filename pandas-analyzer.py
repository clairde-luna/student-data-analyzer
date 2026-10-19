import pandas as pd

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

print(students)
print("Average exam score:", students["exam_score"].mean())
print("Highest exam score:", students["exam_score"].max())
print("Lowest exam score:", students["exam_score"].min())
