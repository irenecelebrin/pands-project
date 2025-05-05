# Line fitting 
# This script calculates linear regression for both scatter plots (Petal, Sepal). It uses Scipy to find the slope and intercept of a line that best fits the data. It then plots the data points and the fitted line.
# Official documentation on SciPy: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import scipy as sp
import numpy as np 


# import the dataset 
iris = load_iris()

# store features in different variables 
sepal_length = iris.data[:, 0]
sepal_width = iris.data[:, 1]   
petal_length = iris.data[:, 2]
petal_width = iris.data[:, 3]

# Prepare class colors for both plots. In each plots, classes (iris species) will be represented by different colors. 
# Colors need to be arrays. Reference: https://jamesmccaffrey.wordpress.com/2020/10/22/making-a-python-scatter-plot-with-different-colors-for-different-labels/ 
# reference: https://matplotlib.org/stable/gallery/color/named_colors.html
colormap_sepal = np.array(['palegreen', 'limegreen', 'green'])
colormap_petal = np.array(['orchid', 'mediumvioletred', 'pink'])

def sepal_regression():

    # Calculate linear regression for sepal length vs sepal width. From there, extract slope and intercept.
    sepal_res = sp.stats.linregress(sepal_length, sepal_width)
    slope_sepal = sepal_res.slope
    intercept_sepal = sepal_res.intercept

    # Get line equation: y = mx + c, where m is the slope and c is the intercept.
    sepal_equation = f'W = {slope_sepal:.2f}L + {intercept_sepal:.2f}'
    
    # Re-create the scatter plot from 5. Source: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
    fig, ax = plt.subplots()
    # SEPAL LENGTH vs SEPAL WIDTH
    plot = ax.scatter(sepal_length, sepal_width, c=colormap_sepal[iris.target], marker='8')

    # Create legend using feature_names 
    # from chatGPT https://chatgpt.com/share/67f2c42b-a108-800f-9b47-c15d529b5264 
    legend_elements = [Line2D([0], [0], marker='8', color='w', label=label,
                            markerfacecolor=color, markersize=10)
                    for label, color in zip(iris.target_names, colormap_sepal)]
    ax.legend(handles=legend_elements, loc="upper left", title="Iris variety")


    # Personalise grid and ticks
    # Grid: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html
    # Ticks: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html
    ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    ax.set_xticks(np.arange(4.25,8.25,0.5), minor=True)
    ax.set_yticks(np.arange(2.25,4.75,0.5), minor=True)
    ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.25, alpha=0.5)


    # Add line to the plot 
    sepal_regression = ax.plot(sepal_length, slope_sepal * sepal_length + intercept_sepal, color='blue',label=sepal_equation)

    # Set new legend, title and axes labels 
    ax.legend()
    ax.set_xlabel('Sepal length (L)')
    ax.set_ylabel('Sepal width (W)')
    ax.set_title('Iris Sepal: regression line')

    # save the plot to a png file 
    #plt.savefig(f'{path_plot}_sepal_regression.png')


def petal_regression(): 

    # Calculate linear regression for petal length vs petal width. From there, extract slope and intercept.
    petal_res = sp.stats.linregress(petal_length, petal_width)
    slope_petal = petal_res.slope
    intercept_petal = petal_res.intercept

    # Get line equation: y = mx + c, where m is the slope and c is the intercept.
    petal_equation = f'W = {slope_petal:.2f}L + {intercept_petal:.2f}'

    # Recreate the scatter plot from 5. 
    fig, ax = plt.subplots()
    # PETAL LENGTH vs PETAL WIDTH   

    # Repeat the same steps, but using for ax x petal length, for ax y petal width, as as colormapa colormap_petal
    plot = ax.scatter(petal_length,petal_width, c=colormap_petal[iris.target], marker='8')

    # Create legend using feature_names 
    legend_elements = [Line2D([0], [0], marker='8', color='w', label=label,
                            markerfacecolor=color, markersize=10)
                    for label, color in zip(iris.target_names, colormap_petal)]
    ax.legend(handles=legend_elements, loc="upper left", title="Iris variety")

    # personalise grid and ticks 
    ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    ax.set_xticks(np.arange(0.5,7.5,1), minor=True)
    ax.set_yticks(np.arange(0.25,2.75,0.5), minor=True)
    ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.25, alpha=0.5)


    # Derive the fitted line using the slope and intercept, following the foruma y = mx + c, where m is the slope and c is the intercept.
    petal_regression = ax.plot(petal_length, slope_petal * petal_length + intercept_petal, color='blue',label=petal_equation)
    
    # Add new legend, title and axes labels
    ax.legend()
    ax.set_xlabel('Petal length (L)')
    ax.set_ylabel('Petal width (W)')
    ax.set_title('Iris Petal: regression line') 

def save_regression(path_plot):
    sepal_regression()
    plt.savefig(f'{path_plot}_sepal_regression.png', dpi=300, bbox_inches='tight')
    petal_regression()
    plt.savefig(f'{path_plot}_petal_regression.png', dpi=300, bbox_inches='tight')



