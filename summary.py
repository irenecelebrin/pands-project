# summary 

import numpy as np 
import pandas as pd
from sklearn.datasets import load_iris

# load the iris dataset 
iris = load_iris()

name = iris.feature_names

def samples(i): 
    return np.size(iris.data[:, i])

def unique(i): 
    return len(np.unique(iris.data[:, i]))

funct = [min, max, np.mean, np.std, np.median]
def maths(function,i): 
    return function(iris.data[:, i])
        


i = 0
with open('test.txt', 'w') as test: 
    for name in iris.feature_names: 
        test.write(f'Feature name:\t{name.capitalize()}\n')
        test.write(f'Samples:\t\t{samples(i)}\n')
        test.write(f'Unique:\t\t\t{unique(i)}\n')
        for function in funct: 
            test.write(f'{function.__name__.capitalize()}:\t\t\t{maths(function,i)}\n')
        test.write('\n')
        i += 1





