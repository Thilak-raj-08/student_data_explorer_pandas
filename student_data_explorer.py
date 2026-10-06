import pandas as pd

student_ids = ["S001", "S002", "S003", "S004", "S005"]
name = ["Arun", "Nila", "Kavin", "Meena", "Ravi"]
age = [20 , 21 , 19, 22, 20]
python_marks = [85, 72, 91, 45, 70]
ai_marks = [80, 76, 95, 60, 65]

name_series = pd.Series(name, index = student_ids)
print(name_series)

age_series = pd.Series(age, index = student_ids)
print(age_series)

python_marks_series = pd.Series(python_marks, index = student_ids)
print(python_marks_series)

ai_marks_series = pd.Series(ai_marks, index = student_ids)
print(ai_marks_series)

top_python_id = python_marks_series.idxmax()
print("Student ID :", top_python_id)
print("Name :", name_series.loc[top_python_id])
print("Python Marks :", python_marks_series.loc[top_python_id])

lowest_python_id = python_marks_series.idxmin()
print("Student ID :", lowest_python_id)
print("Name :", name_series.loc[lowest_python_id])
print("Python Marks :", python_marks_series.loc[lowest_python_id])

top_ai_id = ai_marks_series.idxmax()
print("Student ID :", top_ai_id)
print("Name :", name_series.loc[top_ai_id])
print("AI Marks :", ai_marks_series.loc[top_ai_id])

lowest_ai_id = ai_marks_series.idxmin()
print("Student ID :", lowest_ai_id)
print("Name :", name_series.loc[lowest_ai_id])
print("AI Marks :", ai_marks_series.loc[lowest_ai_id])

python_marks_average = python_marks_series.mean()
print("Python AVG :",python_marks_average)

ai_marks_average = ai_marks_series.mean()
print("AI AVG :",ai_marks_average)

python_mask = python_marks_series > 75
filtered_names = name_series[python_mask]
filtered_python_marks = python_marks_series[python_mask]
print(filtered_names, filtered_python_marks)

ai_mask = ai_marks_series > 75
filtered_ai_marks_name = name_series[ai_mask]
filtered_ai_marks = ai_marks_series[ai_mask]
print(filtered_ai_marks_name, filtered_ai_marks)


python_pass_mask = python_marks_series >=70
print(python_pass_mask.sum())

ai_pass_mask = ai_marks_series >=70
print(ai_pass_mask.sum())

print()

both_pass_mask = python_pass_mask & ai_pass_mask
filtered_both = name_series[both_pass_mask]
print(filtered_both)
print(both_pass_mask.sum())