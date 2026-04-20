import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("student_exam_data.csv")
df.columns = ["study_hours", "prev_score", "result"]

# Plot 1
plt.scatter(df["study_hours"], df["result"])
plt.xlabel("Study Hours")
plt.ylabel("Result")
plt.show()

# Plot 2
plt.scatter(df["prev_score"], df["result"])
plt.xlabel("Previous Score")
plt.ylabel("Result")
plt.show()

# Combined plot
plt.scatter(df["study_hours"], df["prev_score"], c=df["result"])
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.show()