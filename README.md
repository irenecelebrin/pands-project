# The Iris dataset 
Final project for the course 'Programming and Scripting'. 

This repository includes a programmatic analysis and plotting of the Iris dataset by R. Fisher. 

##  Requirements 

Requirements to run the code:
The code can be interpreted with python 3.12.
Required modules include: 

Sklearn.datasets 
Pandas
Numpy
Matplotlib.pyplot 


## The dataset 

The **Iris flower dataset** was created by the British biologist and statistician Ronald Fisher and first published in 1936 in *The use of multiple measurements in taxonomic problems*. 
The dataset includes 150 samples (50 each) from 3 different species of Iris flower: *Iris Setosa**, **Iris Virginica**, **Iris Versicolor**. 
For each sample in the dataset, the following variables are provided: 
- 4 Features: **Sepal length**, **Sepal width**, **Petal length**, **Petal width**. These measurements are expressed in cm.  
- 1 Target: 3 different Iris species (see above). These are also called classes. 
(source: https://en.wikipedia.org/wiki/Iris_flower_data_set)

The dataset also includes metadata about variable names, class distribution and references to papers investigating the dataset. 

The dataset was used by Fisher himself as an example for Linear Discriminant Analysis. The goal of LDA is to find a Linear Combination (or direct correlation) between features to prove that they characterise or seprate given classes of objects (in this case, the 3 iris species). This means that with the iris dataset a user can find and analyse the correlation of 2 or more features in the dataset. For example, by looking at the features of a sample, the corresponding iris species can be guessed. (source: https://en.wikipedia.org/wiki/Linear_discriminant_analysis)

The Iris dataset is commonly used as a beginner's dataset to approach machine learning for classification, data mining and clustering (source: http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html)

## The analysis 

The dataset is included in this repository for reference purposes. However, it is also imported from the module Sklearn.datasets to make it easier to load and explore the data and metadata. 

Analysis.py is an program that allows to perform several functions. 
Each component of the program was developed individually and is imported in the main python file as external module.
All modules are independent, so if a module is not required, it can be commented and the program run without it. 

The components of the program are: 

1) read_dataset.py 
This module will print in the console a brief description of the dataset. It can be used by the user to verify the properties of the dataset. The information includes: 

- Shape of the dataset (n. of instances, n. of columns)
- Names of the features
- Names of the target classes 
- Preview of the first rows of the dataset
- Keys of the datset. 


2) summary.py 
This module creates a text file with a summary of the variables included in the dataset: 
For features:
- names 
- max, min, avg, mean, std, unique values 
For target
- names
- unique values 

3) hist.py

4) scatter.py 

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
