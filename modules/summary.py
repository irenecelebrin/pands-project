# Summary 
# Get the summary of the variables in the iris dataset and save the data to a text file.

import numpy as np 
import pandas as pd
from sklearn.datasets import load_iris

# load the iris dataset 
iris = load_iris()

# create function to get the summary of the variables in the iris dataset and save it a text file 
def independent_variables_summary():

    # store feature names in a variable  
    feature_names = iris.feature_names
    # store numpy functions in a list 
    funct = [min, max, np.mean, np.std, np.median]

    # create functions for every mathematical operation
    # Get feature size 
    def samples(i): 
        return np.size(iris.data[:, i])
    # Get feature unique values 
    def unique(i): 
        return len(np.unique(iris.data[:, i]))
    # Get feature min, max, mean, std, median
    funct = [min, max, np.mean, np.std, np.median]
    def maths(function,i): 
        return function(iris.data[:, i])
            
    # Create a text file to save the summary of the independent variables
    # Create a loop to iterate the feature names, apply the functions created above and save the results to a text file 
    i = 0
    with open('variables.txt', 'w') as variable: 
        variable.write('Independent Variables:\n')
        for name in iris.feature_names: 
            variable.write(f'Feature name:\t{name.capitalize()}\n')
            variable.write(f'Samples:\t\t{samples(i)}\n')
            variable.write(f'Unique:\t\t\t{unique(i)}\n')
            for function in funct: 
                variable.write(f'{function.__name__.capitalize()}:\t\t\t{maths(function,i)}\n')
            variable.write('\n')
            i += 1


def dependent_variables_summary(): 

    # store target names in a variable
    target_names = iris.target_names 

    # store target size in a variable 
    target_size = np.size(iris.target)

    # store target uique values in a variable 
    target_unique = len(np.unique(iris.target))

    # store target values in a variable 
    target_values = np.unique(iris.target)

    # append to the text a summary of the dependent variables (targets)
    with open('variables.txt', 'a') as variable: 
        variable.write('Dependent Variables:\n')
        variable.write(f'Samples:\t\t{target_size}\n')
        variable.write(f'Unique:\t\t\t{target_unique}\n')
        variable.write(f'Target names:\t{target_names}\n')
        variable.write(f'Target values:\t{target_values}\n')
        variable.write('\n')

def summary(): 
    independent_variables_summary()
    dependent_variables_summary()