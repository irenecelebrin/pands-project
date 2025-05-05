# Scatter plots 
# This script allow to create scatter plots analysing the relationships between the features of the iris dataset: 
# sepal length vs sepal width, petal length vs petal width.

# import required modules: sklearn.datasets, matplotlib.pyplot, numpy, os 
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np 
import pandas as pd
import os 




iris = load_iris()

print(type(iris.DESCR))