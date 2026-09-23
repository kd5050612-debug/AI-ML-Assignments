import math
import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Math Library")
print("Square root of 25:", math.sqrt(25))
print("5 factorial:", math.factorial(5))

numbers = np.array([10, 20, 30, 40, 50])

print("\nNumPy")
print("Mean:", np.mean(numbers))
print("Standard Deviation:", np.std(numbers))

data = [10, 20, 20, 30, 40, 50]

print("\nSciPy")
print("Median:", np.median(data))
print("Mode:", stats.mode(data, keepdims=True).mode[0])

student_data = {
    "Name": ["Aarav", "Rahul", "Priya", "Sneha", "Krishna"],
    "Marks": [85, 78, 92, 88, 95]
}

df = pd.DataFrame(student_data)

print("\nPandas DataFrame")
print(df)

print("\nAverage Marks:", df["Marks"].mean())

plt.bar(df["Name"], df["Marks"])
plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()

sns.histplot(df["Marks"], bins=5, kde=True)
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
