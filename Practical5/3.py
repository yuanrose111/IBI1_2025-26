import matplotlib.pyplot as plt

# Task 3: Population Growth Rate Analysis

# Step 1: Define population data (2020 & 2024) 
# Define population dataset (unit: million)
# Structure: {Country: {'2020': value, '2024': value}}
population_data = {
    'UK': {'2020': 66.7, '2024': 69.2},
    'China': {'2020': 1426, '2024': 1410},
    'Italy': {'2020': 59.4, '2024': 58.9},
    'Brazil': {'2020': 208.6, '2024': 212.0},
    'USA': {'2020': 331.6, '2024': 340.1}
}

# Step 2: Calculate percentage change (2020-2024) 
# Initialize empty dictionary to store percentage change
pop_percent_change = {}

# Loop through each country to calculate percentage change
for country, year_data in population_data.items():
    # Extract 2020 and 2024 population values
    pop_2020 = year_data['2020']
    pop_2024 = year_data['2024']
    
    # Formula: ((2024 - 2020) / 2020) * 100 → percentage change
    percent_change = ((pop_2024 - pop_2020) / pop_2020) * 100
    
    # Round to 2 decimal places (scientific norm for percentage)
    pop_percent_change[country] = round(percent_change, 2)

# Print percentage change for each country
for country, pct in pop_percent_change.items():
    # Add '+' sign for increase, keep '-' for decrease (more readable)
    if pct > 0:
        print(f"{country}: +{pct}%")
    else:
        print(f"{country}: {pct}%")

# Step 3: Sort by percentage change (descending) & find extremes 
# Sort countries by percentage change (from highest increase to highest decrease)
sorted_countries = sorted(
    pop_percent_change.items(),
    key=lambda x: x[1],  # Sort by the percentage value (second element of tuple)
    reverse=True         # Descending order (highest first)
)

# Print sorted results
for country, pct in sorted_countries:
    if pct > 0:
        print(f"{country}: +{pct}%")
    else:
        print(f"{country}: {pct}%")

# Find country with maximum increase (first in sorted list) and maximum decrease (last in sorted list)
max_increase_country = sorted_countries[0]  # Highest percentage change (increase)
max_decrease_country = sorted_countries[-1] # Lowest percentage change (decrease)

print("\n--- Extreme Values ---")
print(f"Maximum population increase: {max_increase_country[0]} (+{max_increase_country[1]}%)")
print(f"Maximum population decrease: {max_decrease_country[0]} ({max_decrease_country[1]}%)")

# Step 4: Plot bar chart (visualize percentage change) 
# Set chart style
plt.figure(figsize=(9, 6))  # 9×6 inches (wide enough for 5 countries)
plt.rcParams['font.sans-serif'] = ['Arial']  # Ensure English display

# Prepare data for bar chart
countries = list(pop_percent_change.keys())  # X-axis: country names
changes = list(pop_percent_change.values())  # Y-axis: percentage change values

# Custom colors: green for increase (+), red for decrease (-)
bar_colors = ['green' if c > 0 else 'red' for c in changes]

# Draw bar chart
plt.bar(
    x=countries,
    height=changes,
    color=bar_colors,
    edgecolor='black'  # Add black border to bars for clarity
)

# Add labels and title (all English, meet assignment requirements)
plt.title('Population Percentage Change (2020-2024)', fontsize=14, pad=20)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Percentage Change (%)', fontsize=12)

# Add horizontal line at y=0 (baseline for increase/decrease)
plt.axhline(y=0, color='black', linewidth=1)  # Critical: distinguish increase/decrease

# Add grid for y-axis (easy to read values)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Auto-adjust layout to avoid label cutoff
plt.tight_layout()

# Display the bar chart
plt.show()