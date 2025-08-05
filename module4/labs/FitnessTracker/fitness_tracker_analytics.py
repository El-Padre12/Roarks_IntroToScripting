# Angel Chavez
# Aug 4th, 2025
# Python 3.13.5
# program that analyzes fitness tracker data using Numpy and Pandas
# "Min-Max/Normalize" 0-1 means the min value in a data set will be set to 0, the max value set to 1 -
# and all other values in between will be scaled proportionally to decimal value between 0-1

# just realized i forgot to use numpy and did everything with pandas will fix l8r

import pandas as pd

with open('module4/labs/FitnessTracker/fitness_data.csv', 'r', encoding='utf-8') as file:
    df = pd.read_csv(file)

    # initial data
    print('Initial data: ')
    print(f'{df.head()}\n')

    # average steps and calories
    average_steps = df['Steps'].mean()
    average_calories = df['Calories'].mean()

    print(f'Average steps: {round(average_steps):.2f}')
    print(f'Average calories: {round(average_calories):.2f}')

    # highest and lowest steps data
    lowest_steps = df['Steps'].min()
    highest_steps = df['Steps'].max()

    print(f'Lowest step count: {lowest_steps}')
    print(f'Highest step count: {highest_steps}\n')

    # normalize duration data
    lowest_duration = df['Duration'].min()
    highest_duration = df['Duration'].max()
    normalized_duration_df = (df['Duration'] - lowest_duration) / (highest_duration - lowest_duration)

    print('Normalized Duration data: ')
    print(f'{normalized_duration_df}\n')

    # adding new column to dataframe
    df['Steps_per_minute'] = round((df['Steps'] / df['Duration']), 2)
    print('Dataframe with added column: ')
    print(f'{df.head()}\n')

    # filters and displays users who burned more than 350cal
    filtered_calories_df = df[df['Calories'] > 350]
    print('Users who burned more than 350cals: ')
    print(filtered_calories_df)

    # save update dataframe to a new csv called "fitness_summary.csv"
    df.to_csv('module4/labs/FitnessTracker/fitness_summary.csv', index=False)