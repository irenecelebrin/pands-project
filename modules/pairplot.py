# Pairplot
# This program created a pairplot of the iris dataset using seaborn and matplotlib.
# Official documentation: https://seaborn.pydata.org/generated/seaborn.pairplot.html

from sklearn.datasets import load_iris
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load the iris dataset in tabular format setting the parameter as_frame=True
# Source: https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
iris = load_iris(as_frame=True)

# Plot pairplot with Searborn
def plot_pairplot(): 

    # Format the data in a pandas dataframe, bacause seaborn requires a Pandas dataframe as input data. 
    iris_df = iris.frame
    # Prepare legend for the plot. 
    # Capitalize variable names (features + target). source : https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html 
    iris_df.columns = iris_df.columns.str.capitalize()
    # Format target names replacing the numbers with the names of the species. source: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.map.html
    iris_df['Target'] = iris_df['Target'].map({0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'})
    # Prepare color palette for the plot. Sns requires a dict. 
    target_palette = {
        'Setosa' : 'orchid',
        'Versicolor' : 'mediumvioletred',
        'Virginica' : 'pink'
    }

    # Plot the data. Source: https://seaborn.pydata.org/generated/seaborn.pairplot.html
    plot = sns.pairplot(iris_df, hue='Target', palette=target_palette, height= 2)
    # add title. source: https://www.tutorialspoint.com/how-to-show-the-title-for-the-diagram-of-seaborn-pairplot-or-pridgrid-matplotlib
    plot.figure.suptitle('Pairplot of Iris Dataset', y=1) 
    
    # return plot object to save it later 
    return plot

# save the pairplot to a png file.
def save_pairplot(plot_path):
    plot = plot_pairplot()
    # save the plot to a .png file. Source: https://seaborn.pydata.org/generated/seaborn.objects.Plot.save.html
    plot.savefig(f'{plot_path}_pairplot.png')

# test the function without saving the plot
if __name__ == "__main__":
    plot_pairplot()
    plt.show()
    

