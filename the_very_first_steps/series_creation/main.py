import pandas as pd

even_numbers = [2, 4, 8, 16]
states  = ['New York', 'California', 'Chicago', 'Alaska']

# Write your code below
numbers_series = pd.Series(even_numbers)
states_series = pd.Series(states)

# Testing the result
print(numbers_series , states_series)