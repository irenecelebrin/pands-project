# Histograms 
# This scripts creates histograms for all the features in the iris dataset, and daves them to .png files. 

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import os 

def plot_histograms():
    # create directory to save the plots 
    if not os.path.exists('plots'):
        os.makedirs('plots')

    # load iris dataset 
    iris = load_iris()

    # create a dictionary storing feature names and colors for the histograms 
    features = {
        'sepal_length' : iris.data[:, 0],
        'sepal_width' : iris.data[:, 1],
        'petal_length' : iris.data[:, 2],
        'petal_width' : iris.data[:, 3]
    }

    # create lists for the colors in the histograms 
    colors = ['seagreen', 'lightgreen', 'darkorchid', 'plum']
    edgecolors = ['mediumseagreen', 'palegreen', 'mediumorchid', 'thistle']

    # for loop to create a histogram for each feature, apply desidered colors and save the plot to a .png file in the existing folder 'histograms'
    i = 0
    for feature in features:
        plt.hist(features[feature], color = colors[i], edgecolor = edgecolors[i])
        plt.xlabel('Dimensions (in cm)')
        plt.ylabel('N. in the dataset')
        plt.title(feature.replace('_', ' ').capitalize())
        plt.savefig(f'./plots/3_hist_{feature}.png')
        plt.close()
        i += 1


if __name__ == '__main__':
    plot_histograms()
