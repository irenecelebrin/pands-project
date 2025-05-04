# Boxplots
# This script allows to create boxplots showing the distribution of the features in the iris dataset. In particular, it shows maximum, minimum, median, first and thrid quartiles, and highlights any outliers. 
# Official documentation on Matplotlib: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html 

# import required modules: sklearn.datasets, matplotlib.pyplot, numpy, os 
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np 
import os 

def plot_boxplots():    
    # create directory to save the plots 
    if not os.path.exists('plots'):
        os.makedirs('plots')

    # import the dataset 
    iris = load_iris()

    # set labels for each feature
    feature_labels = []
    for name in iris.feature_names:
        feature_label = name.replace(' (cm)','').capitalize()
        feature_labels.append(feature_label)

    # set colors for each feature 
    colors = ['seagreen','lightgreen', 'darkorchid', 'plum']
    median_color = dict(color = 'red', linewidth = 1.5 )

    # Create subplot
    fig, ax = plt.subplots() 

    # Plot boxplots
    # Subplot includes different colors for each feature boxplot, ticks and labels for each feature 
    # about medianprops: https://stackoverflow.com/questions/57668399/change-the-colors-of-outline-and-median-lines-of-boxplot-in-matplotlib 
    feature_plot = ax.boxplot(iris.data, patch_artist=True, medianprops= median_color, tick_labels=feature_labels)


    # assign colors to each feature boxplot 
    # more here: https://matplotlib.org/stable/gallery/statistics/boxplot_color.html#sphx-glr-gallery-statistics-boxplot-color-py
    for patch, color in zip(feature_plot['boxes'], colors):
        patch.set_facecolor(color) 

    # add title 
    ax.set_title('Feature variation')
    # add x ticks and labels for each boxplot 
    # see https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html#matplotlib.axes.Axes.set_xticks
    #plt.xticks([1,2,3,4], feature_names)
    # add labels for axes 
    ax.set_xlabel('Features')
    ax.set_ylabel('Measure (in cm)')

    # uncomment to show plot
    # plt.show()
    # save plot to .png file 
    plt.savefig('plots/4_boxplots.png')

if __name__ == '__main__':
    plot_boxplots()
