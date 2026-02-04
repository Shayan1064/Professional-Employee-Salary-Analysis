import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# np.random.seed(42)

# num_employees = 1000

# # Generate random data
# employee_names = [f"Employee_{i+1}" for i in range(num_employees)]
# ages = np.random.randint(22, 60, size=num_employees)
# departments = np.random.choice(['HR', 'IT', 'Sales', 'Marketing', 'Finance', 'Operations'], size=num_employees)
# experience = np.random.randint(0, 35, size=num_employees)

# # Salary depends on experience + department variation
# base_salary = np.random.randint(30000, 50000, size=num_employees)
# dept_bonus = {
#     'HR': 5000, 'IT': 15000, 'Sales': 20000, 
#     'Marketing': 12000, 'Finance': 10000, 'Operations': 8000
# }
# salary = [base_salary[i] + experience[i]*1000 + dept_bonus[departments[i]] for i in range(num_employees)]

# # Create DataFrame
# df = pd.DataFrame({
#     'Employee_Name': employee_names,
#     'Age': ages,
#     'Department': departments,
#     'Experience_Years': experience,
#     'Salary': salary
# })

# # Save to CSV
# df.to_csv("salary_data.csv", index=False)
# print("Dataset created successfully!")



df=pd.read_csv("salary_data.csv")
print(df)

dept_salary=df.groupby('Department')['Salary'].mean()
print(dept_salary)

plt.figure(figsize=(8,5))
bars = plt.bar(dept_salary.index, dept_salary.values, color='skyblue', edgecolor='black')

# Add values on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 500, int(yval), ha='center', va='bottom', fontsize=10)

plt.title("Total Salary by Department", fontsize=14)
plt.xlabel("Department", fontsize=12)
plt.ylabel("Total Salary ($)", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# Sort by Salary descending
sorted_by_salary = df.sort_values(by='Salary', ascending=False)

# Take top 10
top10 = sorted_by_salary.head(10)

# # Display top 10
print("Top 10 Salaries:\n")
print(top10[['Employee_Name', 'Salary', 'Experience_Years', 'Department']])


plt.figure(figsize=(10,6))

# # Create bar chart: x = Employee Names, y = Salaries
bars = plt.bar(top10['Employee_Name'], top10['Salary'], color='skyblue', edgecolor='black')

# # Add values on top of bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1000, int(yval), ha='center', va='bottom', fontsize=10)

plt.title("Top 10 Salaries", fontsize=16)
plt.xlabel("Employee Name", fontsize=12)
plt.ylabel("Salary (PKR)", fontsize=12)
plt.xticks(rotation=45)  # rotate x-axis labels to fit better
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

dept_salary = df.groupby('Department')['Salary'].agg(['max', 'min']).reset_index()
print(dept_salary)

# # Plotting
plt.figure(figsize=(8,5))
bar_width = 0.35
x = range(len(dept_salary))

# # Bars for Max and Min
plt.bar(x, dept_salary['max'], width=bar_width, label='Max Salary', color='skyblue', edgecolor='black')
plt.bar([i + bar_width for i in x], dept_salary['min'], width=bar_width, label='Min Salary', color='salmon', edgecolor='black')

# Labels and Titles
plt.xticks([i + bar_width/2 for i in x], dept_salary['Department'])
plt.xlabel('Department')
plt.ylabel('Salary')
plt.title('Min and Max Salaries by Department')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

experience_salary = df.groupby('Experience_Years')['Salary'].mean().reset_index()
print(experience_salary.sort_values(by='Experience_Years'))

min_max_experince=df.groupby('Department')['Experience_Years'].agg(['max', 'min']).reset_index()
print(min_max_experince)


plt.figure(figsize=(10,6))
plt.plot(experience_salary['Experience_Years'], experience_salary['Salary'], marker='o', color='green')
plt.title("Average Salary vs Experience", fontsize=16)
plt.xlabel("Experience (Years)", fontsize=12)
plt.ylabel("Average Salary (PKR)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(experience_salary['Experience_Years'])
plt.tight_layout()
plt.show()

# Min and Max Experience per Department
min_max_experience = df.groupby('Department')['Experience_Years'].agg(['max', 'min']).reset_index()

plt.figure(figsize=(10,6))
bar_width = 0.35
index = range(len(min_max_experience))

plt.bar(index, min_max_experience['min'], width=bar_width, label='Min Experience', color='skyblue', edgecolor='black')
plt.bar([i + bar_width for i in index], min_max_experience['max'], width=bar_width, label='Max Experience', color='orange', edgecolor='black')

plt.title("Min and Max Experience per Department", fontsize=16)
plt.xlabel("Department", fontsize=12)
plt.ylabel("Experience (Years)", fontsize=12)
plt.xticks([i + bar_width/2 for i in index], min_max_experience['Department'])
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()