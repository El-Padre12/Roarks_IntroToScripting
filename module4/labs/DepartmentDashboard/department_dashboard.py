# Angel Chavez
# Aug 4th, 2025
# Python 3.13.5
# program that visualizes CSV data using Matplotlib and Pandas

import pandas as pd
import matplotlib.pyplot as plt

# open file with context manager for best practices
with open('module4/labs/DepartmentDashboard/departments.csv', 'r', encoding='utf-8') as file:
    df = pd.read_csv(file)
    # adds color for each department bar respectfully
    colors = ['skyblue', 'salmon', 'lightgreen', 'gold', 'plum']

    plt.bar(df['Department'].str.title(), df['Avg_GPA'], color=colors)
    plt.xlabel('Departments')
    plt.ylabel('GPAs')
    plt.title('Average GPA per Department')
    plt.xticks(rotation=30)
    plt.grid(axis='y')

    plt.tight_layout()
    plt.show()