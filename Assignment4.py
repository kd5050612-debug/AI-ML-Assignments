import numpy as np

numbers = [10, 20, 30, 40, 50]

a = 20
b = 10

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

mean = np.mean(numbers)
median = np.median(numbers)
standard_deviation = np.std(numbers)

print("\nStatistical Calculations")
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", standard_deviation)
