# Summary 
# Get the summary of the variables in the iris dataset and save the data to a text file.

import numpy as np 
import pandas as pd
from sklearn.datasets import load_iris

# load the iris dataset 
iris = load_iris()

# store feature names in a variable  
feature_names = iris.feature_names
# store numpy functions in a list 
funct = [min, max, np.mean, np.std, np.median]

# create functions for every mathematical operation
# Get frature size 
def samples(i): 
    return np.size(iris.data[:, i])
# Get feature unique values 
def unique(i): 
    return len(np.unique(iris.data[:, i]))
# Get feature min, max, mean, std, median
funct = [min, max, np.mean, np.std, np.median]
def maths(function,i): 
    return function(iris.data[:, i])
        
# Create a loop to iterate the feature names, apply the functions and print the result to a text file 
i = 0
with open('variables.txt', 'w') as variable: 
    for name in iris.feature_names: 
        variable.write(f'Feature name:\t{name.capitalize()}\n')
        variable.write(f'Samples:\t\t{samples(i)}\n')
        variable.write(f'Unique:\t\t\t{unique(i)}\n')
        for function in funct: 
            variable.write(f'{function.__name__.capitalize()}:\t\t\t{maths(function,i)}\n')
        variable.write('\n')
        i += 1





