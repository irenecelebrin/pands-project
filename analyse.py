# Analyse -- main program for the project

from modules.read_dataset import read
from modules.summary import summary
from modules.histograms import plot_histograms
from modules.scatter import save_scatter
from modules.boxplots import save_boxplots 
from modules.heatmap import save_heatmap, save_correlation_matrix
from modules.linear_regression import save_regression
import os 
import matplotlib.pyplot as plt
import pandas as pd


# Create the directory to save the plots in pands-project. Source: https://chatgpt.com/share/68179c6d-cd20-800f-8473-58e28f06aa34
# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the 'plots' folder inside the repo
plot_dir = os.path.join(script_dir, 'plots')

# Create the folder if it doesn't exist
os.makedirs(plot_dir, exist_ok=True)

# 1. print in the console some information about the dataset. Enter a key to explore the dataset.
# Exit the program entering a blank value 
read()

# 2. Save a summary of independent and dependent variables to a txt file and save it in a folder called 'plots'. 
# set the path to save the file
summary_path = os.path.join(plot_dir, '02_summary.txt')
summary(summary_path)

# 3. Plot histograms for each feature, and save them as .pgn files in a folder called 'plots'. 
# set the path to save the plots
hist_path = os.path.join(plot_dir, '03')
plot_histograms(hist_path)

# 4. Plot boxplots for each feature and save them as .png files in a folder called 'plots'.
# set the path to save the boxplots
boxplot_path = os.path.join(plot_dir, '04')
save_boxplots(boxplot_path) 

# 5. Plot scatter plots comparing Sepal length vs Sepal width, and Petal length vs petal width, and save them as .png files in a folder called 'plots'.
# set the path to save the scatter plots
scatter_path = os.path.join(plot_dir, '05')
save_scatter(scatter_path)

# 6. Calculate simple linear regression for both plots in 5. and save the plots as .png files in a folder called 'plots'.
# set the path to save the linear regression plots
regression_path = os.path.join(plot_dir, '06')
save_regression(regression_path)

# 7. Create a Heatmap showing Person's correlation coefficients between the features and save it as a .png file in a folder called 'plots'. Create a .csv file with the correlation matrix.
# set the path to save the heatmap and correlation matrix 
corr_path = os.path.join(plot_dir, '07')
save_heatmap(corr_path)
save_correlation_matrix(corr_path)




