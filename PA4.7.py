print("Jorkee0238")

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Store a classroom roster of 10 students in an array
students = [
    "Alice",
    "Bob",
    "Charlie",
    "Diana",
    "Ethan",
    "Fiona",
    "George",
    "Hannah",
    "Ian",
    "Julia",
]
subjects = ["Math", "Science"]

#Create a hierarchical MultiIndex combining students and subjects
multi_index = pd.MultiIndex.from_product(
    [students, subjects], names=["Student", "Subject"]
)

#Create a DataFrame containing random grades for each student-subject pair
np.random.seed(42)
grades = np.random.randint(
    70, 100, size=len(multi_index)
)
df = pd.DataFrame({"Grade": grades}, index=multi_index)

#Display the DataFrame
print("\n--- Student Grades DataFrame ---")
print(df)

#Group by the subject and calculate the mean grade for each subject
subject_means = df.groupby("Subject").mean()
print("\n--- Mean Grades by Subject ---")
print(subject_means)

#Display the vertical bar graph of the grouped subject means
subject_means.plot(kind="bar", color="skyblue", legend=False, rot=0)
plt.title("Average Grades by Subject - jorkee0238")
plt.xlabel("Subject")
plt.ylabel("Mean Grade")
plt.ylim(0, 100)
plt.tight_layout()
plt.show()
