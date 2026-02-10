import pandas as pd

# load dataset into a DataFrame
data = pd.read_csv("crime.csv", delimiter=",")

# add a new column based on the violent crimes per population
data["risk"] = data["ViolentCrimesPerPop"].apply(lambda x: "High-Crime" if x >= 0.50 else "Low-Crime")

# group by risk and calculate the average of percentage unemployed for each group
averageUnemployment = data.groupby("risk")["PctUnemployed"].mean()

# print the average unemployment rate for both risk categories
print("Average Unemployment Rate for High-Crime populations: ", averageUnemployment["High-Crime"])
print("Average Unemployment Rate for Low-Crime populations: ", averageUnemployment["Low-Crime"])