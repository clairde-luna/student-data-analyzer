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
