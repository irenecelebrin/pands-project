# Summary 
# Get the summary of the variables in the iris dataset and save the data to a text file.

# import require libraries 
import numpy as np 
from sklearn.datasets import load_iris


# load the iris dataset 
iris = load_iris()

# create function to get the summary of the variables in the iris dataset and save it a text file 
def independent_variables_summary(summary_path):

    # store feature names in a variable  
    feature_names = iris.feature_names
    # store numpy functions in a list 
    funct = [min, max, np.mean, np.std, np.median]

    # create functions for every mathematical operation
    # Get feature size 
    def samples(i): 
        return np.size(iris.data[:, i])
    # Get feature unique values. Source: https://numpy.org/doc/stable/reference/generated/numpy.unique.html
    def unique(i): 
        return len(np.unique(iris.data[:, i]))
    # Get feature min, max, mean, std, median. Source: https://numpy.org/doc/stable/reference/generated/numpy.mean.html, https://numpy.org/doc/stable/reference/generated/numpy.std.html, https://numpy.org/doc/stable/reference/generated/numpy.median.html, https://numpy.org/doc/stable/reference/generated/numpy.min.html, https://numpy.org/doc/stable/reference/generated/numpy.max.html
    functions = [min, max, np.mean, np.std, np.median]
    def maths(function,i): 
        return function(iris.data[:, i])
    # Get 1st quartile and 3rd quartile. Source: https://numpy.org/doc/stable/reference/generated/numpy.quantile.html
    quantiles = [0.25, 0.75]
    def quartiles(i): 
        return np.quantile(iris.data[:, i], quantile)

            
    # Create a text file to save the summary of the independent variables
    # Create a loop to iterate the feature names, apply the functions created above and save the results to a text file 
    i = 0
    with open(summary_path, 'w') as variable: 
        variable.write('Independent Variables:\n')
        for name in iris.feature_names: 
            variable.write(f'Feature name:\t{name.capitalize()}\n')
            variable.write(f'Samples:\t\t{samples(i)}\n')
            variable.write(f'Unique:\t\t\t{unique(i)}\n')
            for function in functions: 
                variable.write(f'{function.__name__.capitalize()}:\t\t\t{maths(function,i)}\n')
            for quantile in quantiles: 
                variable.write(f'{int(quantile * 100)}%:\t\t\t{quartiles(i)}\n')
            variable.write('\n')
            i += 1


def dependent_variables_summary(summary_path): 

    # store target names in a variable
    target_names = iris.target_names 

    # store target size in a variable 
    target_size = np.size(iris.target)

    # store target uique values in a variable 
    target_unique = len(np.unique(iris.target))

    # store target values in a variable 
    target_values = np.unique(iris.target)

    # append to the text a summary of the dependent variables (targets)
    with open(summary_path, 'a') as variable: 
        variable.write('Dependent Variables:\n')
        variable.write(f'Samples:\t\t{target_size}\n')
        variable.write(f'Unique:\t\t\t{target_unique}\n')
        variable.write(f'Target names:\t{target_names}\n')
        variable.write(f'Target values:\t{target_values}\n')
        variable.write('\n')

# execute both functions together 
def summary(summary_path): 
    independent_variables_summary(summary_path)
    dependent_variables_summary(summary_path)

# run the script and save test in the directory 
if __name__ == '__main__':  
    summary('test_summary.txt')
