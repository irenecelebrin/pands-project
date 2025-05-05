# Heatmap 
# This script allows to calculate Pearson correlation coefficients between the features of the iris dataset and plot a heatmap.

# import required modules: sklearn.datasets, matplotlib.pyplot, numpy, os 
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np 
import pandas as pd

# load the iris dataset 
iris = load_iris()

# prepare feature labels 
feature_labels = iris.feature_names

# Calculate correlation coefficients: the results is a 4x4 matrix which shows the correlation between each pair of features
# Source: https://numpy.org/doc/2.2/reference/generated/numpy.corrcoef.html
correlation_matrix = np.corrcoef(iris.data, rowvar=False).round(decimals=2)

def heatmap():

    # Create subplot and plot 
    # About colormaps https://matplotlib.org/stable/users/explain/colors/colormaps.html#sphx-glr-users-explain-colors-colormaps-py
    fig, ax = plt.subplots()
    im = ax.imshow(correlation_matrix, vmin= -1, vmax = 1, cmap = 'RdPu')

    # Personalize the plot 
    ax.grid(False)
    # add feature names as tick labels
    ax.set_xticks(range(len(feature_labels)),labels=feature_labels, rotation = 45)
    ax.set_yticks(range(len(feature_labels)),labels=feature_labels)
    ax.set_title('Feature correlation\n',fontsize = 15, weight = 'bold')

    # create a for loop to add coefficient to each cell in the plot 
    for i in range(len(feature_labels)):
        for j in range(len(feature_labels)):
            text = ax.text(j, i, correlation_matrix[i, j],
                        ha="center", va="center", color="white", fontsize = 12)
            
    # add colorbar. Reference: https://realpython.com/numpy-scipy-pandas-correlation-python/#linear-correlation 
    cbar = ax.figure.colorbar(im, ax= ax, format='% .2f')
    cbar.set_label("Pearson's correlation coefficient", rotation=270, labelpad=20)

def save_heatmap(plot_path):
    heatmap()
    # save the plot as a png file in the 'plots' folder
    plt.savefig(f'{plot_path}_heatmap', dpi=300, bbox_inches='tight')

def save_correlation_matrix(plot_path):    
    # Create a pandas DataFrame from the correlation matrix
    df = pd.DataFrame(correlation_matrix, columns=feature_labels, index=feature_labels)

    # Save the DataFrame to a CSV file
    df.to_csv(f'{plot_path}_correlation', index=True)


if __name__ == "__main__":
    heatmap()
    plt.show()
