# Import matplotlib
import matplotlib.pyplot as plt

#1. Define the heart rate dataset
heart_rates=[72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

#How many patients are in the dataset
print("The number of patients in the dataset: ",len(heart_rates))
#Calculate the mean heart rate
mean_heart_rate = sum(heart_rates) / len(heart_rates)
print("The mean heart rate is: ",mean_heart_rate)

#2. Categorize heart rates 
#Initialize the counters for each
low_counts = 0
normal_counts = 0
high_counts = 0

# Iterate through each heart rate value and assign to category
for i in heart_rates:
    if i < 60:
        low_counts += 1
    elif 60 <= i <= 120:
        normal_counts += 1
    else:
        high_counts += 1

# Store category counts in a dictionary
category_counts = {"Low":low_counts, "Normal":normal_counts, "High":high_counts}
print(category_counts)

# Find the category with the largest number of patients
largest_category = max(category_counts, key=category_counts.get)
print("The category with the largest number of patients is: ",largest_category)

#3. Create the pie chart
#Extract data for plotting
categories = list(category_counts.keys())
counts = list(category_counts.values())
#Plot size
plt.figure(figsize=(8, 6))

#Draw
plt.pie(counts,labels=categories,autopct="%1.1f%%",explode=(0.05, 0.05, 0.05))
# Ensure pie chart is a perfect circle
plt.axis("equal")

plt.show()


