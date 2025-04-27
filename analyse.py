# Analyse -- main program for the project

from modules.read_dataset import read
from modules.summary import summary
from modules.histograms import plot_histograms



# print in the console some information about the dataset. Enter a key to explore the dataset.
# Exit the program entering a blank value 
read()

# Save a summary of independent and dependent variables to a txt file (variables.txt) 
summary()

# Plot histograms for each feature, and save them as .pgn files in a folder called 'Histograms'. 
plot_histograms()

# Plot scatter plots comparing Sepal length vs Sepal width, and Petal length vs petal width, and save them as .png files in a folder called 'Scatterplots'.
