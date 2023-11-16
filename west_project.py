# -*- coding: utf-8 -*-
"""west_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15NjfMYk21gIOUI4iCkM4QNYIGIuUWfNV
"""

import pandas as pd
df = pd.read_csv("supermarket_sales.csv")

cities = [city for city in df['City']]
totals = [total for total in df['Total']]
cities_totals_icncome = [{cities[i]:totals[i]} for i in range(len(cities))]
cities_totals_icncome

"""d) Data Analysis and functions:
⦁	Perform at least 5 different data analyses on selected datasets using conditionals, loops, individually written functions and libraries.
⦁	Examples of analyses can include:
⦁	Calculating the average of specific columns.
⦁	Finding the minimum and maximum values of a column.
⦁	Counting the occurrences of a specific value in a column.
⦁	Grouping the data by a specific category and calculating summary statistics.
⦁	Plotting graphs or visualisations to represent the data.
⦁	Implement error handling to handle potential issues, such as missing or invalid data.
⦁	Implement a user interface that allows the user to interact with the program and perform various analyses.

For example being, we will take Tangon city's clients' total spent
"""

#Selecting all the yangons
yangon = []
income_per_unit = []
for city in cities_totals_icncome:
  if list(city.keys())[0] == "Yangon":
    yangon.append(city)
    income_per_unit.append(list(city.values())[0])
yangon

#In this part we will calculate maximum,average and minimum value
maximum = max(income_per_unit)
minmum = min(income_per_unit)
avg = sum(income_per_unit) / len(income_per_unit)
print("Max",maximum)
print("Min",minmum)
print("Average",avg)

import matplotlib.pyplot as plt

# Example list of numbers
my_list = income_per_unit

# Plotting the data
plt.plot(my_list, marker='o', linestyle='-')
plt.title('Yangon sales')
plt.xlabel('Yangon')
plt.ylabel('Income')
plt.grid(True)
plt.show()

#Statiscal Calculation
import statistics

# Example list of numbers
my_list = income_per_unit

# Calculate statistical measures
mean_value = statistics.mean(my_list)
median_value = statistics.median(my_list)
mode_value = statistics.mode(my_list)
variance_value = statistics.variance(my_list)
stdev_value = statistics.stdev(my_list)

# Print the results
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")
print(f"Variance: {variance_value}")
print(f"Standard Deviation: {stdev_value}")

"""In this part we will develop CLI based functionalities inorder for user check any branch of company. Using this option we can select any city of our wish!"""

def search_city(user_input):
  income_per_unit = []
  for city in cities_totals_icncome:
    if list(city.keys())[0] == user_input:
      yangon.append(city)
      income_per_unit.append(list(city.values())[0])
    else:
      return "Sorry wrong inpuc command was given try again."
  return income_per_unit

def ploting(plot_info,city_name):
  # Example list of numbers
  my_list = income_per_unit
  # Plotting the data
  plt.plot(my_list, marker='o', linestyle='-')
  plt.title('Yangon sales')
  plt.xlabel(city)
  plt.ylabel('Income')
  plt.grid(True)
  plt.show()

def stats_function(data):
  my_list = income_per_unit
  # Calculate statistical measures
  mean_value = statistics.mean(my_list)
  median_value = statistics.median(my_list)
  mode_value = statistics.mode(my_list)
  variance_value = statistics.variance(my_list)
  stdev_value = statistics.stdev(my_list)

  # Print the results
  print(f"Mean: {mean_value}")
  print(f"Median: {median_value}")
  print(f"Mode: {mode_value}")
  print(f"Variance: {variance_value}")
  print(f"Standard Deviation: {stdev_value}")


print("Which city are you intrested in?")
all_info_cities = df['City'].tolist()
print('Availabe options:',set(all_info_cities))
user_input = str(input("Your option: ")).capitalize()
data = search_city(user_input)
print("Here is a plot for")
ploting(data,user_input)
print("Satisical Analyzes")
stats_function(data)

