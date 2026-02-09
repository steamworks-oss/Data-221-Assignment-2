import pandas as pd

# load dataset into a DataFrame
data = pd.read_csv("student.csv", delimiter=",")
# filter students where studytime>=3, internet=1, absecnes<=5
data = data[(data["studytime"] >= 3) & (data["internet"] == 1) & (data["absences"] <= 5)]
# save filtered data to new csv
data.to_csv("high_engagement.csv")

# print number of students in filtered dataframe along with the average grade of theirs
print("Number of students: ", len(data))
print("Average grade of students: ", data["grade"].mean())