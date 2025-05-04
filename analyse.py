# Analyse -- main program for the project

from modules.read_dataset import read
from modules.summary import summary
from modules.histograms import plot_histograms
from modules.scatter import plot_scatter
from modules.boxplots import plot_boxplots 
from modules.heatmap import correlation_heatmap



# 1. print in the console some information about the dataset. Enter a key to explore the dataset.
# Exit the program entering a blank value 
read()

# 2. Save a summary of independent and dependent variables to a txt file and save it in a folder called 'plots'
summary()

# 3. Plot histograms for each feature, and save them as .pgn files in a folder called 'plots'. 
plot_histograms()

# 4. Plot boxplots for each feature and save them as .png files in a folder called 'plots'.
plot_boxplots() 

# 5. Plot scatter plots comparing Sepal length vs Sepal width, and Petal length vs petal width, and save them as .png files in a folder called 'plots'.
plot_scatter()

# 6. Heatmap and ConnectionError
correlation_heatmap()