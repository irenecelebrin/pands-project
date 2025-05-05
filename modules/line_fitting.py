# Line fitting 
# This script calculates linear regression for both scatter plots (Petal, Sepal). It uses Scipy to find the slope and intercept of a line that best fits the data. It then plots the data points and the fitted line.
# Official documentation on Matplotlib: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html 


from scatter import scatter_sepal, scatter_petal
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import scipy as sp
import numpy as np 
import os 

scatter_sepal()
plt.show()