# The Iris dataset 
Final project for the course 'Programming and Scripting'. 

This repository includes a programmatic analysis and plotting of the Iris dataset by R. Fisher. 

##  Requirements 

Requirements to run the code: The code can be interpreted with python 3.12.

A number of external libraries are used in this project: a complete list is provided in the file [*requirements.txt*](.\requirements.txt). 

To run the code, make sure these libraries are installed on your machine. If you are running the code in a codespace, they should already be installed. You can install them in two ways: 
1) individually, running the command 'pip install *library name*'
2) all together, running the command 'pip pip install -r requirements.txt'



## The dataset 

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

## The analysis 

The dataset is included in this repository for reference purposes. However, in the program the dataset is also imported from the module Sklearn.datasets to make it easier to load and explore the data. 

### analysis.py
**How it works** 

This is the main program, and it allows to perform several functions. 
Each component of the program was developed individually and is imported in the main python file as external module.
All modules are independent, so if a module is not required, it can be commented and the program run without it. 

The modules included in the main program are: 
1) read_dataset
2) summary
3) histograms
4) scatter

### 1. Reading the dataset 
**What it does**

Read_dataset.py will print in the console a brief description of the dataset. It can be used by the user to verify the properties of the dataset. The information includes: 
- Shape of the dataset (n. of instances, n. of columns)
- Names of the features
- Names of the target classes 
- Preview of the first rows of the dataset
- Keys of the datset. 
Additionally, this script allows the user to input a key of the dataset, and view corresponding value. 

**Looking at the output**


### 2. summary.py 
**What it does**

Summary.py creates a text file with a summary of the variables included in the dataset: 
For independent variables (features):
- name
- sample number in the dataset
- mathematical calculations: max, min, avg, mean, std, unique values 
For dependent variable (target, or class)
- sample number in the dataset
- unique values number
- names
- unique values 


### 3. Histograms 
**What it does**
Histograms.py loads the iris dataset and creates histograms for each feature and saves the histograms to .pgn files. 
Reference: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html

**About the histograms** 

### 4. scatter.py 
**What it does**
This modules loads the iris dataset and creates scatter plots for each pair of features: sepal length vs sepal width, petal length vs petal width. 
Reference: 
scatter plots https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
scatter plot with legend: https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_with_legend.html
grid: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html
ticks: https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xticks.html

**About the scatter plots**
- **Sepal** As for sepal length, for Iris Setosa the correlation bwteen sepal lenght and width show a clear trend, and makes the class easy to distinguish from the others. On the other hand, Iris Versicolor and Iris Virginica look quite similar and can't be easily distinguished one from the other. The only difference is that Versicolor samples tend to have smaller dimensions (there are mostly located in the lower part of the plot, on the left), while Virginica samples seem to be bigger in dimension (lower part of the plot, but on the right). If only Petal length and width are considered, it is possible to predict if a sample is Iris Setosa or not with a high degree of certainty, whereas it would be harder to predict if a sample is Virginica or Versicolor. 
- **Petal** As for petal length, a clear trend is visible from the plot. It looks like each class has its own characteristic dimensions -- smaller for Iris Setosa, bigger for Versicolor and more so for Virginica. Again, Iris Setosa is clearly separated from the other two classes. Versicolor and Virginica, although easy enough to separate, share a common area where samples have similar features but belong to one class or the other. 



5) ...


## References 

readme, aboout the dataset 
https://en.wikipedia.org/wiki/Iris_flower_data_set 
https://en.wikipedia.org/wiki/Linear_discriminant_analysis 
https://scikit-learn.org/1.4/auto_examples/datasets/plot_iris_dataset.html
https://www.kaggle.com/datasets/uciml/iris/data
https://www.kaggle.com/code/mrdheer/beginner-s-guide-to-iris-dataset

read_dataset 
https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html 
https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html#sphx-glr-auto-examples-decomposition-plot-pca-iris-py 
https://archive.ics.uci.edu/dataset/53/iris 
https://www.kaggle.com/code/kostasmar/exploring-the-iris-data-set-scikit-learn



//TODO 
