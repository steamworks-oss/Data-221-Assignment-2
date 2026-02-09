import pandas as pd

# load dataset into a DataFrame
data = pd.read_csv("student.csv", delimiter=",")

# add a new column determined by the grades of the students
data["grade_band"] = str()
data.loc[data["grade"] <= 9, "grade_band"] = "Low"
data.loc[(data["grade"] >= 10) & (data["grade"] <= 14), "grade_band"] = "Medium"
data.loc[data["grade"] >= 15, "grade_band"] = "High"

# create a grouped summary table with the number of students, average absences, and the percentage of students with internet access
groupedSummaryTable = data.groupby('grade_band').agg(
    numberOfStudents=('grade_band', 'count'),
    averageAbsences=('absences', 'mean'),
    internetAccessPercentaeg=('internet', 'mean')
)

# save the table as a data set
groupedSummaryTable.to_csv("student_bands.csv")