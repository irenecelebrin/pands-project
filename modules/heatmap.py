# Heatmap 
# This script allows to calculate Pearson correlation coefficients between the features of the iris dataset and plot a heatmap.

# import required modules: sklearn.datasets, matplotlib.pyplot, numpy, os 
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np 
import pandas as pd
import os 


# Create the directory to save the plots in pands-project. Source: https://chatgpt.com/share/68179c6d-cd20-800f-8473-58e28f06aa34
# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent directory of the script
parent_dir = os.path.dirname(script_dir)

# Define the path to the 'plots' folder inside the repo
plot_dir = os.path.join(parent_dir, 'plots')

# Create the folder if it doesn't exist
os.makedirs(plot_dir, exist_ok=True)

plot_path = os.path.join(plot_dir, '06')


# load the iris dataset 
iris = load_iris()

def correlation_heatmap():

    # prepare feature labels 
    feature_labels = iris.feature_names

    # Calculate correlation coefficients: the results is a 4x4 matrix which shows the correlation between each pair of features
    # Source: https://numpy.org/doc/2.2/reference/generated/numpy.corrcoef.html
    correlation_matrix = np.corrcoef(iris.data, rowvar=False).round(decimals=2)

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

    # uncomment to show the plot 
    # plt.show()

    # save the plot as a png file in the 'plots' folder
    plt.savefig(f'{plot_path}_heatmap', dpi=300, bbox_inches='tight')

    # Save correlation matrix to a .csv file 
    # Create a pandas DataFrame from the correlation matrix
    df = pd.DataFrame(correlation_matrix, columns=feature_labels, index=feature_labels)

    # Save the DataFrame to a CSV file
    df.to_csv(f'{plot_path}_correlation', index=True)


if __name__ == "__main__":
    correlation_heatmap()

