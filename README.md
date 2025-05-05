# The Iris dataset 

## About this repository 

This repository includes the final project for the course 'Programming and Scripting' of the Higher Diploma in Computing for Data Analytics (year: 2025/2026). The project consists of a study of the Iris dataset by R. Fisher; the goal is to analyse and plot the data programmatically, in order to gain meaningful insights on the dataset. 

The repository includes the following files and folders: 
- **README** (i.e. this file). It includes information on each of the modules in the project, a comment on the project output, and references to external sosurces. 
- **requirements.txt**. A list of the requirements to run the code, more information in *I. Requirements*
- **.gitignore**. List of file formats that git will ignore and not include in the pushes
- **iris**. The complete iris dataset, for user reference *. 
- **modules**. More information in *III. The analysis*. 
    - read_dataset.py
    - summary.py
    - histograms.py
    - boxplots
    - scatter.py
    - linear_regression.py
    - heatmap.py
- **analyse.py**. Main file where the code can be run all at once. 

*The complete iris dataset available on [UCI Machine Learning](https://archive.ics.uci.edu/dataset/53/iris) is included in the repository for user reference. However, in the code the dataset is always imported through the Scikit learn library [load_iris()](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html), which makes it easier to explore and manipulate the data. 

## I. Requirements 

Requirements to run the code: The code can be interpreted with python 3.12.

A number of external libraries are used in this project: a complete list is provided in the file [*requirements.txt*](.\requirements.txt). 

If the code is executed locally, make sure these libraries are installed on your machine. If you are running the code in a virtual environment, that won't be necessary. You can install the libraries in two ways: 
1) individually, running the command 'pip install *library name*'
2) all together, running the command 'pip pip install -r requirements.txt'



## II. The dataset 

The **Iris flower dataset** was created by the British biologist and statistician Ronald Fisher and first published in 1936 in *The use of multiple measurements in taxonomic problems*. 
The dataset includes 150 samples (50 each) from 3 different species of Iris flower: **Iris Setosa**, **Iris Virginica**, **Iris Versicolor**. 
For each sample in the dataset, the following 5 variables are provided: 
- 4 Features: **Sepal length**, **Sepal width**, **Petal length**, **Petal width**. These measurements are expressed in cm.  
- 1 Target: 3 different Iris species (see above). These are also called classes. 
(source: [Iris flower dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set))
In this project, features will be considered and **ndipendent variables* and target as *dependent variable* (source: [Iris Dataset - Exploratory Data Analysis](https://www.kaggle.com/code/lalitharajesh/iris-dataset-exploratory-data-analysis)). 

The dataset also includes metadata about variable names, class distribution and references to papers investigating the dataset. 

The dataset was used by Fisher himself as an example for Linear Discriminant Analysis. The goal of LDA is to find a Linear Combination (or direct correlation) between features to prove that they characterise or separate  given classes of objects (in this case, the 3 iris species). This means that with the iris dataset a user can find and analyse the correlation of 2 or more features in the dataset. For example, by looking at the features of a sample, the corresponding iris species can be guessed. (source: [Linear discriminant analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis)). 

The Iris dataset is commonly used as a beginner's dataset to approach machine learning for classification, data mining and clustering (source: [Data Science Example - Iris dataset](http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html)).

## III. The analysis 

As explained in *About this repository*, the full dataset is included in this repository for reference purposes. However, in the program the dataset is also imported from the module Sklearn.datasets to make it easier to load and explore the data. 

### 0. Analyse
**How it works** 

This is the main program, and it allows to perform several functions. 
Each component of the program was developed individually and is imported in the main python file as external custom module.
All modules are independent, so if a module is not required, it can be commented and the program run without it. 

The modules included in the main program are: 
1) read_dataset.py
2) summary.py
3) histograms.py
4) boxplots.py
5) scatter.py
6) linear_regression.py
7) heatmap.py


### 1. Reading the dataset 

Module: read_dataset.py 

**What it does**

Read_dataset.py will print in the console a brief description of the dataset. It can be used by the user to verify the properties of the dataset. The information includes: 
- Shape of the dataset (n. of instances, n. of columns)
- Names of the features
- Names of the target classes 
- Preview of the first rows of the dataset
- Keys of the datset. 
Additionally, this script allows the user to input a key of the dataset, and view corresponding value. 

**Looking at the output**


### 2. The summary 

Module: summary.py

**What it does**

Summary.py creates a text file with a summary of the variables included in the dataset: 
For independent variables (features):
- name
- sample number in the dataset
- count of unique values 
- mathematical calculations: max, min, avg, mean, std, 1st quartile (25%), 3rd quartile(75%)

For dependent variable (target, or class)
- sample number in the dataset
- unique values number
- names
- unique values 

**Looking at the numbers**

[TO REPHRASE]
Features (independent variables): 
- petal width has the smallest dimensions 
- 

**About summary.txt**

Instead of writing the data to a text file, I would have tried to calculate the data and add them to a dictionnary, that I could have later converted to a Pandas dataframe and printed to a .csv file. This is because having individial blocks of information for each feature (as in summary.txt) makes it harder to compare numbers and gain insights on differences/similarities between features. 

### 3. Histograms 

Module: histograms.py

**What it does**

Histograms.py loads the iris dataset, creates histograms for each feature and saves them to .pgn files. 
Reference: [matplotlib.pyplot.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)

**About the histograms** 
[Petal Length and Width have similar trends]
[Sepal length: most samples are in the first 2/3 or the range, without a regular distribution]
[Sepal width: most samples are in the center of the range, showing that few samples are much smaller or bigger than that ]

### 4. Boxplots 

Module: boxplots.py

**What it does**

**About the plot**
Boxplots are used to verify feature variation and distribution. 

[Sepal width has the least degree of variation, but also some outliers]
[Sepal length has a long whisker in the upper part, showing few sparse samples much bigger than the others]
[Petal length has the highest degree of variation, median is close to 3rd quartile + long whisker in the upper part]
[Petal width has a similar trend to Petal length: median is close to 3rd quartile, long whisker in the upper part BUT lower variation in dimensions]


### 5. Scatterplots 

Module: scatterplots.py

**What it does**

This module loads the iris dataset and creates scatter plots for each pair of features: sepal length vs sepal width, petal length vs petal width. The script includes functions to plot each plot, and one function to save both plots to .png files. 
Reference: 
scatter plots https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
scatter plot with legend: https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html
grid: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html
ticks: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html

**About the scatter plots**

Scatter plots are used to highlight correlations between features, and verify if classes also play a role in the correlation. 

**Sepal:** 
Iris Setosa has smaller Sepal length but greater width, while Versicolor and Virgina have greater length and lower width. 
This trend makes it easy to distinguish Setosa species from the others; on the other hand, Versicolor and Iris Virginica look quite similar and can't be easily distinguished one from the other. The only difference is that Versicolor samples tend to have smaller dimensions (They are mostly located in the lower part of the plot, on the left), while Virginica samples seem to be bigger in dimension (lower part of the plot, but on the right). 

Based exclusively on Petal length and Petal width, it would not be possible to predict which species a sample belongs to. However, it could be possible to predict if a species is a Setosa or not. 

**Petal:** 
As for Petal length and Petal width, the plot highlights a direct positive correlation between the two features. It looks like each class has its own characteristic dimensions -- Iris Setosa has smaller dimensions, Versicolor tend to be bigger, and Virginica even more. 
Again, Iris Setosa can be more easily separated from the other two classes, whereas Versicolor and Virginica samples overlap in a small area of the plot.

### 6. Linear Regression 

Module: linear_regression.py

**What it does**

Linear_regression.py uses SciPy to calculate Simple linear regression for each pair of features from the scatter plots (Sepal length vs Sepal width, Petal length vs petal width).
It uses the values of slope and intercept to create an equation that represents a trend in the data. It re-creates the scatter plots from 5. Scatter, and plots a line to represent the Regression formula. 

**About the regression lines**
Explain what linear regression is 

Explain what it highlights 
- no trend in Sepal
- positive and direct correlation in Petal  

### 7. Heatmap 

**What it does** 

Heatmap.py uses Numpy to calculate Pearson's correlation coefficients for each pair of features in the dataset. 
Based on the resulting correlation matrix, it creates a heatmap highlighting the correlation amoung all features. The program also prints the correlation matrix to a .csv file, for further reference. 


**About the heatmap**

Calculate Pearson's correlation coefficient between the features 
show the correlation betwewn the features, and highlight if there is a positive or negative correlation, or no correlation at all. 


### 7. Heat map 

### 8. Line fitting 

### 9. Pairplot 


## IV. References 

README, About the dataset 
https://en.wikipedia.org/wiki/Iris_flower_data_set 

https://en.wikipedia.org/wiki/Linear_discriminant_analysis 

https://scikit-learn.org/1.4/auto_examples/datasets/plot_iris_dataset.html

https://www.kaggle.com/datasets/uciml/iris/data

https://www.kaggle.com/code/mrdheer/beginner-s-guide-to-iris-dataset/code

Read_dataset 

https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html 

https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html#sphx-glr-auto-examples-decomposition-plot-pca-iris-py 

https://archive.ics.uci.edu/dataset/53/iris 

https://www.kaggle.com/code/kostasmar/exploring-the-iris-data-set-scikit-learn

Summary 

Histograms 

Boxplots 

Scatter

Linear Regression 

Heatmap 


