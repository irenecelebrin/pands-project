# Analyse -- main program for the project

from read_dataset import read
from summary import independent_variables_summary as ind_var
from summary import dependent_variables_summary as dep_var


# print in the console some information about the dataset. Enter a key to explore the dataset.
# Exit the program entering a blank value 
read()

# Save a summary of independent and dependent variables to a txt file (variables.txt) 
ind_var()
dep_var()

# 