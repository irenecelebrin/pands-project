# Analyse -- main program for the project

from modules.read_dataset import read
from modules.summary import summary
from modules.histograms import plot_histograms
from modules.scatter import scatter_sepal, scatter_petal
from modules.boxplots import plot_boxplots 
from modules.heatmap import correlation_heatmap
import os 
import matplotlib.pyplot as plt


# Create the directory to save the plots in pands-project. Source: https://chatgpt.com/share/68179c6d-cd20-800f-8473-58e28f06aa34
# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the path to the 'plots' folder inside the repo
plot_dir = os.path.join(script_dir, 'plots')

# Create the folder if it doesn't exist
os.makedirs(plot_dir, exist_ok=True)

plot_path = os.path.join(plot_dir, '')



# 1. print in the console some information about the dataset. Enter a key to explore the dataset.
# Exit the program entering a blank value 
#read()

# 2. Save a summary of independent and dependent variables to a txt file and save it in a folder called 'plots'
#summary()

# 3. Plot histograms for each feature, and save them as .pgn files in a folder called 'plots'. 
#plot_histograms()

# 4. Plot boxplots for each feature and save them as .png files in a folder called 'plots'.
#plot_boxplots() 

# 5. Plot scatter plots comparing Sepal length vs Sepal width, and Petal length vs petal width, and save them as .png files in a folder called 'plots'.
scatter_sepal
plt.savefig(f'{plot_path}05_sepal.png')
scatter_petal()
plt.savefig(f'{plot_path}05_petal.png')

# 6. Create a Heatmap showing Person's correlation coefficients between the features and save it as a .png file in a folder called 'plots'. Create a .csv file with the correlation matrix.
#correlation_heatmap()

