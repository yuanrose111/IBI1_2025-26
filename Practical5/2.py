import matplotlib.pyplot as plt

# 1. Define heart rate dataset (unit: bpm)
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

# Calculate total number of patients (length of the list)
patient_count = len(heart_rates)

# Calculate average heart rate (sum / count)
average_hr = sum(heart_rates) / patient_count

# Print basic statistics (1 decimal place for average, scientific norm)
print(f"Total number of patients: {patient_count}")
print(f"Average resting heart rate: {average_hr:.1f} bpm")

# Initialize counters for each category
low_hr = 0    # < 60 bpm
normal_hr = 0 # 60 ≤ hr ≤ 120 bpm
high_hr = 0   # > 120 bpm

# Loop through each heart rate to count categories
for hr in heart_rates:
    if hr < 60:
        low_hr += 1 
    elif 60 <= hr <= 120:
        normal_hr += 1  
    else:
        high_hr += 1  

# Print category statistics
print(f"Low heart rate (< 60 bpm): {low_hr} patient(s)")
print(f"Normal heart rate (60-120 bpm): {normal_hr} patient(s)")
print(f"High heart rate (> 120 bpm): {high_hr} patient(s)")

# Find the most frequent category (max value in counter dictionary)
hr_categories = {'Low heart rate': low_hr, 'Normal heart rate': normal_hr, 'High heart rate': high_hr}
most_frequent_cat = max(hr_categories, key=hr_categories.get)
print(f"Most frequent category: {most_frequent_cat} ({hr_categories[most_frequent_cat]} patient(s))")

# Plot pie chart (visualize category distribution)
# Set chart style (square canvas for pie chart)
plt.figure(figsize=(7, 7)) 
plt.rcParams['font.sans-serif'] = ['Arial']  

# Prepare data for pie chart
labels = ['Low (<60 bpm)', 'Normal (60-120 bpm)', 'High (>120 bpm)'] 
sizes = [low_hr, normal_hr, high_hr]  
colors = ['lightcoral', 'lightgreen', 'lightskyblue']  

# Draw pie chart with percentage labels
plt.pie(
    x=sizes,
    labels=labels,
    colors=colors,
    autopct='%1.1f%%',  # Show percentage with 1 decimal place
    shadow=True,        # Add shadow for 3D effect
    startangle=90       # Start pie chart at 90 degrees (top position)
)

# Add title and ensure pie is a perfect circle
plt.title('Distribution of Resting Heart Rate Categories', fontsize=14, pad=20)
plt.axis('equal')  # Critical: make pie chart a circle (not oval)

# Display the pie chart
plt.tight_layout()  
plt.show()