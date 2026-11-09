"""
RECORD CHECK  -  my version
===========================

Name  : Arham Farid
Lane  : IT  
Date  : 9 October 2026
"""

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("records_lab.csv")  # reads the csv file


df["percent"] = (df["used_gb"] / df["total_gb"]) * 100 # adds a percent column and calculates the percent

df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else ("WARNING" if p >= 90 else "OK")
) # adds a status column using .apply() and a lambda function


print(df)
fltrd_df = df[df["status"] != "OK"] # filters it to only show status of not ok
print(fltrd_df)
status_counts = df["status"].value_counts() # gorup by status and count how many each status appear
print(status_counts)
df.to_csv("records_lab_report.csv", index=False) # saves it into a new csv file
status_counts.plot(kind="bar") # creates a bar chart for the status
plt.title("servers by status")
plt.xlabel("Status")
plt.ylabel("servers")
plt.tight_layout()
plt.savefig("status_counts.png") #saves the chart as a png
plt.show()


