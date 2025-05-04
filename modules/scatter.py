# Scatter plots 
# This script allows to create scatter plots analysing the relationships between the features of the iris dataset: 
# sepal length vs sepal width, petal length vs petal width.

# import required modules: sklearn.datasets, matplotlib.pyplot, numpy, os 
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np 
import os 

def plot_scatter():
    # create directory to save the plots 
    if not os.path.exists('plots'):
        os.makedirs('plots')

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

    # Plotting the data 
    # reference: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html

    # Create subplot for sepal length vs sepal width
    fig, ax = plt.subplots()

    # SEPAL LENGTH vs SEPAL WIDTH

    plot = ax.scatter(sepal_length, sepal_width, c=colormap_sepal[iris.target], marker='8')

    # Create legend using feature_names 
    # from chatGPT https://chatgpt.com/share/67f2c42b-a108-800f-9b47-c15d529b5264 
    legend_elements = [Line2D([0], [0], marker='8', color='w', label=label,
                            markerfacecolor=color, markersize=10)
                    for label, color in zip(iris.target_names, colormap_sepal)]
    ax.legend(handles=legend_elements, loc="upper left", title="Iris variety")

    # Add labels and title 
    ax.set_xlabel('Sepal length (cm)')
    ax.set_ylabel('Sepal width (cm)')
    ax.set_title('Sepal length vs Sepal width')

    # Personalise grid and ticks
    # Grid: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html
    # Ticks: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html
    ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    ax.set_xticks(np.arange(4.25,8.25,0.5), minor=True)
    ax.set_yticks(np.arange(2.25,4.75,0.5), minor=True)
    ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.25, alpha=0.5)

    # uncomment to print the plot 
    # plt.show()

    # save the plot to a .png file in the 'scatter_plots' folder
    plt.savefig('./plots/5_sepal.png')


    # PETAL LENGTH vs PETAL WIDTH   

    # Repeat the same steps, but using for ax x petal length, for ax y petal width, as as colormapa colormap_petal
    fig, ax = plt.subplots()

    plot = ax.scatter(petal_length,petal_width, c=colormap_petal[iris.target], marker='8')

    # Create legend using feature_names 
    legend_elements = [Line2D([0], [0], marker='8', color='w', label=label,
                            markerfacecolor=color, markersize=10)
                    for label, color in zip(iris.target_names, colormap_petal)]
    ax.legend(handles=legend_elements, loc="upper left", title="Iris variety")

    # Add labels and title 
    ax.set_xlabel('Petal length (cm)')
    ax.set_ylabel('Petal width (cm)')
    ax.set_title('Petal length vs Petal width')

    # personalise grid and ticks 
    ax.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    ax.set_xticks(np.arange(0.5,7.5,1), minor=True)
    ax.set_yticks(np.arange(0.25,2.75,0.5), minor=True)
    ax.grid(which='minor', color='gray', linestyle='--', linewidth=0.25, alpha=0.5)

    # uncomment to print the plot 
    # plt.show()

    # save the plot to a .png file in the 'scatter_plots' folder
    plt.savefig('./plots/5_petal.png')


if __name__ == '__main__':
    plot_scatter()
