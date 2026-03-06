import pandas as pd

csv_data = pd.read_csv("expenses.csv")
json_data = pd.read_json("expenses.json")

data = pd.concat([csv_data, json_data])

data = data.drop_duplicates()

data['date'] = pd.to_datetime(data['date'])

print(data)

result = data.groupby("category")["amount"].sum()

print(result)

result.to_csv("report.csv")

import matplotlib.pyplot as plt

result.plot(kind="bar")

plt.title("Expenses by Category")
plt.xlabel("Category")
plt.ylabel("Amount")

plt.show()

plt.figure()
result.plot(kind="pie", autopct="%1.1f%%")
plt.title("Expense Distribution")
plt.ylabel("")
plt.show()

data["month"] = data["date"].dt.month
monthly = data.groupby("month")["amount"].sum()

print(monthly)

monthly.to_csv("monthly_report.csv")