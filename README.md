# The Iris dataset 

## About this repository 

This repository includes the final project for the course 'Programming and Scripting' of the Higher Diploma in Computing for Data Analytics (year: 2025/2026). The project consists of a study of the Iris dataset by R. Fisher; the goal is to analyse and plot the data programmatically, in order to gain meaningful insights on the dataset. 

The repository includes the following files and folders: 
- **README** (i.e. this file). It includes information on the dataset and on each of the modules in the project, a comment on the project output, and references to external sosurces. 
- **requirements.txt**. A list of the requirements to run the code, more information in *I. Requirements*.
- **.gitignore**. A list of file formats that git will ignore and not include in the pushes.
- **iris**. The complete iris dataset, for user reference *. 
- **analyse.py**. Main file where the code can be run all at once to produce the analysis of the dataset.
- **modules**. The individual modules that are imported in the main file analyse.py (more information in *III. The analysis*): 
    - read_dataset.py
    - summary.py
    - histograms.py
    - boxplots
    - scatter.py
    - linear_regression.py
    - heatmap.py
    - pairplot.py


*The complete Iris dataset available on [UCI Machine Learning](https://archive.ics.uci.edu/dataset/53/iris) is included in the repository for user reference. However, in the code the dataset is always imported through the Scikit learn library [load_iris()](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html), which makes it easier to explore and manipulate the data. 

## I. Requirements 

Requirements to run the code: the code can be interpreted with Python 3.12.

A number of external libraries are used in this project: a complete list is provided in the file [*requirements.txt*](.\requirements.txt). 

If the code is executed locally, make sure these libraries are installed on your machine. If you are running the code in a virtual environment, that won't be necessary. You can install the libraries in two ways: 
- individually, running the command 'pip install *library name*'
- all together, running the command 'pip pip install -r requirements.txt'



## II. The dataset 

The **Iris flower dataset** was created by the British biologist and statistician Ronald Fisher and first published in 1936 in *The use of multiple measurements in taxonomic problems*. 
The dataset includes 150 samples (50 each) from 3 different species of Iris flower: **Iris Setosa**, **Iris Virginica**, **Iris Versicolor**. 
For each sample in the dataset, the following 5 variables are provided: 
- 4 Features: **Sepal length**, **Sepal width**, **Petal length**, **Petal width**. These measurements are expressed in cm.  
- 1 Target: 3 different Iris species (see above). These are also called classes 
(source: [Iris flower dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set)).

In this project, features will be considered and **Independent variables* and target as *dependent variable* (source: [Iris Dataset - Exploratory Data Analysis](https://www.kaggle.com/code/lalitharajesh/iris-dataset-exploratory-data-analysis)). 

The dataset also includes metadata about variable names, class distribution and references to papers investigating the dataset. 

The dataset was used by Fisher himself as an example for Linear Discriminant Analysis. The goal of LDA is to find a Linear Combination (or direct correlation) between features, to prove that they characterise or separate  given classes of objects (in this case, the 3 iris species). This means that with the Iris dataset a user can find and analyse the correlation of 2 or more features in the dataset. For example, by looking at the features of a sample, the corresponding iris species can be guessed. (source: [Linear discriminant analysis](https://en.wikipedia.org/wiki/Linear_discriminant_analysis)). 

The Iris dataset is commonly used as a beginner's dataset to approach machine learning for classification, data mining and clustering (source: [Data Science Example - Iris dataset](http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html)).

## III. The analysis 

As explained in *About this repository*, the full dataset is included in this repository for reference purposes. However, in the program the dataset is also imported through sklearn.datasets (load_iris()) to make it easier to load and explore the data. 

The following sections explain the function of each module in the analysis: what it does, how the code works, and a comment on the output of the program (summary, plots...).  

### 0. The Analysis 

Module: analyse.py 

**What it does** 

This is the main program, and it allows to carry out an analysis of the dataset and print the outputs to a folder named '**plots**'. 

**How it works** 

Each component of the program was developed individually and is imported in the main Python file as an external custom module.
All modules are independent, so if a module is not required in the analysis, it can be commented and the program run without it. 

The modules included in the main program are stored in the folder 'modules'. They include: 
1) read_dataset.py
2) summary.py
3) histograms.py
4) boxplots.py
5) scatter.py
6) linear_regression.py
7) heatmap.py
8) pairplot.py


### 1. Reading the dataset 

Module: read_dataset.py 

**What it does**

Read_dataset.py will print in the console a brief description of the dataset. It can be used by the user to verify the properties of the dataset. The information includes: 
- Shape of the dataset (n. of instances, n. of variables)
- Names of the features
- Names of the target classes 
- Preview of the first 5 rows of the dataset
- Keys of the dataset. 

Additionally, this program allows the user to input a key of the dataset, and view the corresponding value. 

**How it works**

The iris dataset is imported through the Scikit Learn module [load_iris()](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html). 

The function load_iris() returns a bunch, that is a dictionary-like object that includes several keys: 
- data
- target
- frame
- target_names
- DESCR
- feature_names
- filename
- data_module

It is relevant to point out that the data of the dataset (data, targets, feature names, target names) are all Numpy arrays, so it is easy to manipulate them with Numpy to extract and plot the data. 
The key DESCR is a string, and provides useful metadata on the dataset, including information on author, literature, variables and statistics on the data (the same metadata that you can find in iris/iris.names).
The keys are leveraged to print in the console a introdution to the dataset, and ask the user for further input to continue exploring the data. 

Finally, Pandas is also used to convert the dataset to a dataframe and show a preview of the dataset in tabular format (source: [how to convert sklearn to pandas dataframe](https://www.geeksforgeeks.org/How-to-convert-sklearn-dataset-to-pandas-dataframe-in-python/)).

**Looking at the output**

The output of the program shows that the dataset consists of 150 samples. For each sample, 5 variables are provided (4 features, 1 target). 
Additionally, it shows the names of the features, specifying that they are expressed in cm, and the names of the targets. 

It is worth to mention that in the preview of the data in tabular format the targets are not referred to with the Iris species name (which would be strings), but with numbers (integers), probably to make it easier to manipulate the data. 


### 2. The summary 

Module: summary.py

**What it does**

Summary.py creates a text file (summary.txt) with a summary of the variables included in the dataset. 

For independent variables (features), the following information is provided:
- name
- number of samples in the dataset
- count of unique values 
- statistics: min, max, mean, std, median, 1st quartile, 3rd quartile 

For the dependent variable (target, or class), the information provided is: 
- number of samples in the dataset
- number of unique values
- names
- unique values 

**How it works**

The program consists of two functions, one for each variable type (features, targets). 
With regard to features (independent variables), to make the code more synthetic, I decided to create smaller functions to perform different operations. I carried out these operations for each feature using a for loop, and printed the results to a text file. 
As for the target (dependent variable), iterating was not necessary, so the operations are carried out on the variable and saved to a text file. 

The dataset was again imported with load_iris(). Numpy is used to perform all the operations: 
[np.size](https://numpy.org/doc/stable/reference/generated/numpy.size.html),
[np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html),
[np.min](https://numpy.org/doc/stable/reference/generated/numpy.min.html),
[np.max](https://numpy.org/doc/stable/reference/generated/numpy.max.html),
[np.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html),
[np.std](https://numpy.org/doc/stable/reference/generated/numpy.std.html),
[np.median](https://numpy.org/doc/stable/reference/generated/numpy.median.html),
[np.quantile](https://numpy.org/doc/stable/reference/generated/numpy.quantile.html).



**Looking at the numbers**

The file summary.txt provides the following useful information: 
- it verifies that each feature has 150 values, which means that all samples have 4 feature values -- none is Null. 
- it shows how many unique values each feature has: Petal length is the feature with the highest number of unique values (43).

It allows to gain insights from the following statistical operations: 
- **minimum**: the lowest value for each feature. Based on the data, Petal width stands out as the feature with the lowest minimum, while Sepal length is the feature with the greatest minimum. 
- **maximum**: the greatest value in the range. Again, Petal width has the lowest maximum, while Sepal length has the greatest maximum.
- **mean**: the sum of values divided by the count of vlaues ([Wikipedia](https://en.wikipedia.org/wiki/Arithmetic_mean)). 
- **median**: the 'middle' value, i.e. the value that separates the higher half from the lower half in a range ([Wikipedia](https://en.wikipedia.org/wiki/Median)). Comparing mean and median, it is possible to observe that they tend to be somehow similar for all features, with the greatest difference occurring for Petal Length, where the mean is 3.75 and the median 4.35. 
- **standard deviation**: the amount of variation of a variable from the mean value in the range ([Wikipedia](https://en.wikipedia.org/wiki/Standard_deviation)). Petal length has the greatest standard deviation, with a value (1.75) that is more than double that of the second highest standard deviation (Sepal length, 0.82). Sepal width has the lowest standard deviation. This means that Petal length dimensions vary a lot across samples, while Sepal width is somehow similar in all samples. 
- **1st quartile** (25%): cut point that divides a range of data in four equal parts. The 1st quantile corresponds to 25th percentile ([Wikipedia](https://en.wikipedia.org/wiki/Quartile)).
- **3rd quartile** (75%): the third quartile corresponds to 75th percentile ([Wikipedia](https://en.wikipedia.org/wiki/Quartile)). Quartiles will be useful to plot and understand boxplots. 


**EXTRA: limitations**

In hindsight, instead of writing and saving the data to a text file, I would have converted the dataset to a Pandas dataframe and used the function *df.describe()* to get the statistical data (min, max...). Then I could have added any other relevant information to that dataframe. This is because having individial blocks of information for each feature (as in summary.txt) makes it harder to compare numbers and gain insights on differences/similarities between features. About df.dataframe(): [Exploratory data analysis on Iris dataset](https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/). 



### 3. Histograms 

Module: histograms.py


**What it does**

Histograms.py loads the Iris dataset, creates histograms for each feature and saves them to .png files. 
Reference: [matplotlib.pyplot.hist](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)


**How it works** 

After loading the dataset, the features are extracted slicing the Numpy array *data*. Then, lists are created to set the colors for each plot. Finally, histograms are plotted iterating Matplotlib functions for each feature (creating the plot, adding labels and title, and saving the plot). 


A **stateless approach** (or object-oriented) (vs stateful) is used on Matplotlib. This means that pyplot is not used to store the information related to each plot, but this information is stored through variables (objects). In this case, I decided to do it in order to plot and then save the data through iterations (for loops), and in different functions. About stateful vs stateless approach: [Matplotlib essentials](https://medium.com/@The_Gambitier/matplotlib-essentials-e376ed954201). 

A separate function is created to save the plot to an image file. For all plots, it is possible to test the code running those scripts as main, crating the plots but not saving them. The plots can be saved only when the code is run in analyse.py. 


**About the histograms** 

The histograms highlight the distribution of each feature with regard to dimensions ([Exploratory Data Analysis on Iris Dataset](https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/)). What is worth pointing out is: 
- **Petal length and Petal width** have a similar frequency distribution: many samples have smaller dimensions (Petal length: 1-2cm, width: 0.1-0.5cm), then there is few samples in the range immediately after, and then frequency increases again (Petal length: 4+cm, width: 1.4cm). This similarity can be the sign of a correlation between the features.
- **Sepal length and Sepal width** do not seem to have a similar frequency distribution, if not that they tend to have higher frequency (more samples) in the centre of the range, and fewer at the lower and higher end.  However, Sepal length has higher frequency in the first 2/3 of the range  (5-6.5cm), while Sepal width has lower frequency at both ends, and high frequency in the center of the range (3-3.5cm). 


### 4. Boxplots 

Module: boxplots.py


**What it does**

Boxplots.py loads the Iris dataset and plots four boxplots representing the distribution of samples for each feature. About boxplots: [Matplotlib.axes.Axes.boxplot](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html).


**How it works**

A function is created to plot boxplots for each feature in the dataset.
To allow more personalization of the plot with regard to colors, a **stateless** (or object-oriented) approach to Matplotlib is used. 
The same colors used in the histograms are used, to make it easier to associate the plots and compare the data. 

Finally, another function is created to save the plot to an image file. 


**About the plot**

Boxplots are used to complement the distribution analysis performed with histograms. The boxplots highlight the following trends in the features: 

- **Sepal length**: The lower whisker and the plot (corresponding to 1st, 2nd and 3rd quartiles) seem to have similar dimensions, which means that the frequency of samples in those ranges is similar. On the other hand, the higher whisker is longer, showing that samples after the 3rd quartile (=75% of the samples) are more sparse and less frequent. 
- **Sepal width**: it is the feature with the lowest variation, with samples concentrated in a narrow range. In particular, the box (i.e. the range between the 1st and the 3rd quartile) is particularly narrow, showing a high frequency of values in that range. At the ends, particulary at the higher end, there are some fliers (outliers). This is coherent with what has been observed in the histogram. 
- **Petal length** has the highest distribution, which means that dimensions of samples vary more than for the other features. It is also worth pointing out that the box is particularly wide, showing low distribution between the 1st and 3rd quartile. 
- **Petal width** it shows a similar trend to Petal length, but with lower variation: short lower whisker, wide box, median line close to the higher end of the box, longer upper whisker. This is also coherent with the observations made about histograms. 


### 5. Scatterplots 

Module: scatterplots.py


**What it does**

This module loads the Iris dataset and creates scatter plots for each pair of features: sepal length vs sepal width, petal length vs petal width. About scatter plots: [matplotlib.axes.scatter](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html). More information on sources is provided in the code. 


**How it works** 

The script includes functions to plot each scatter plot, and one function to save both plots to .png files. 
In the first functions, the datased is loaded, the data array sliced to extract arrays for each feature. Arrays are created to set colors for both scatter plots. The module matplotlib.Line2D is used to dinamically assign different colors to each class and create a legend with the class names. 


**About the scatter plots**

Scatter plots are used to investigate if there is a relationship between two given variables, and verify if one variable can be used to predict the other (source: [Scatter Plot](https://www.geeksforgeeks.org/scatter-plot/)). In this case, they can also highlight if class distribution is meaningful, i.e. if based on the two variables it is possible to predict the class of a given sample. 

**Sepal.**
The Sepal scatter plot shows that Iris Setosa has smaller Sepal length but greater width, while Versicolor and Virgina have greater length and lower width ([Exploratory data analysis: iris dataset](https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda)). 
This trend makes it easy to distinguish Setosa species from the others. On the other hand, Iris Versicolor and Iris Virginica look quite similar and can't be easily distinguished one from the other. The only difference is that Versicolor samples tend to have smaller dimensions (they are mostly located in the lower part of the plot, on the left), while Virginica samples seem to have longer Sepal length (samples are more frequent in the lower part of the plot, but on the right). 

It is already clear that there is little correlation between the two features. Based on one of the two variables, it would not be possible to predict the value of the other variable. Also, based exclusively on Sepal length and Sepal width, it would not be possible to predict which species a sample belongs to. However, it could be possible to predict if a species is a Setosa or not. 

**Petal.** As for Petal length and Petal width, the plot confirms the correlation guessed looking at the histograms. 
In particular, the plot highlights a direct positive correlation between the two features: the longer the petal, the wider it is. It looks like each class has its own characteristic dimensions: Iris Setosa have smaller dimensions, Versicolor species tend to be bigger, and Virginica even more. 

Again, Iris Setosa can be more easily separated from the other two classes, whereas Versicolor and Virginica samples overlap in a small area of the plot. However, hypotheses can be made about the following points: 
- Based on Petal dimensions it could be possible to predict which species a sample belongs to. 
- Based on the value of one variable, the other variable could be predicted. 


### 6. Linear Regression 

Module: linear_regression.py


**What it does**

Linear_regression.py uses SciPy to calculate Simple linear regression for each pair of features from the scatter plots (Sepal length vs Sepal width, Petal length vs Petal width) and fit a line the scatter plots.

Specifically, for both pair of features, the program derives the values of slope and intercept to calculate Simple Linear Regression, and the coefficient of determination $R^2$ to verify the accuracy of the fitted line (source: [scipy.stats.linregress](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html)).


**How it works** 

Two functions are created in the program: each function calculates the values of slope and intercept of the ideal line fitting the data. The **slope** (or grandient) indicates how steep the line is, while the **intercept** is the value of y when x=0 ([Data Science - Slope and Intercept](https://www.w3schools.com/datascience/ds_linear_slope.asp)). Once these values are found, it is possible to derive the equation of Simple linear regression, and plot the line over the scatter plots. Based on this equation, and if this equation is accurate, it would be possible to perform Linear Regression Analysis, i.e. roughly derive the value of a variable, based on the value of the other variable.

Then the **coefficient of determination $R^2$** is calculated to verify if the equation of Simple Linear Regression is accurate ([Coefficient of Determination (R²) | Calculation & Interpretation](https://www.kaggle.com/discussions/questions-and-answers/62086)). The coefficient of determination is a number between 0 and 1, and tells how accurately a model can predict an output: 
- If $R^2$ = 0, the model cannot predict an outcome.
- If 0 < $R^2$ < 1, the model can partially predict an outcome.
- If $R^2$ = 1, the model can perfectly predict an outcome. 

Finally, the scatter plots are recreated and the lines plotted above. A function at the end of the program executes both functions and saves the plots to image files. 


**About the regression lines**

Simple linear regression is normally used to predict values, for example, to predict the value of a dependent variable based on the value of an independent variable. In this case, however, Simple linear regression is used to highlight if there is a trend in the data, and $R^2$ is used to further verify if Linear Regression can be calculated for those variables. In particular, the plots show that: 

- It would not be possible to predict values based on **Sepal length and Sepal width**. In this case, the line visibly does not fit the data. Most samples (or data points) in the scatter plot are very far from the line, which means that the line is not representative of the data. The coefficient of determination ($R^2$ = 0.01) confirms that the equation cannot be used to make predictions. 
- It could be possible to make predictions about **Petal length and Petal width**, because there is a positive  and direct correlation between the two variables. In my opinion, it could be possible to roughly predict the value of a dependent variable based on an independent variable, or to predict the class, based on the value of both variables. The coefficient of determination ($R^2$ =0.93) confirms that, althogh not perfectly, the equation can be used to make predictions.  


Note: another way of calculting Simple Linear Regression is through [numpy.polyfit](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html). Another way to verify the accuracy of a Simple linear regression model would be through root mean squared error ([Linear Regression, accuracy](https://www.kaggle.com/discussions/questions-and-answers/62086)). 



### 7. Heatmap 

Module: heatmap.py


**What it does** 

Heatmap.py uses Numpy to calculate Pearson's correlation coefficients for each pair of features in the dataset. 
Based on the resulting correlation matrix, it creates a heatmap highlighting the correlation among all features. The program also prints the correlation matrix to a .csv file, for further reference. 
About heatmaps: [Annotated heatmap](https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html#sphx-glr-gallery-images-contours-and-fields-image-annotated-heatmap-py). 


**How it works** 

Pearson's correlation coefficients for each pair of features in the dataset are calculated using [numpy.corrcoef](https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html). With numpy.corrcoef(), it is possible to provide as paramteres 1-D or 2-D arrays, and calculate the correlation between more than two sets of values at the same time. In this case, correlation coefficients are calculated for all four features at the same time: the x value is a NumPy 2-D array where each feature is a column of values.

Then, the resulting matrix is used to plot a heatmap showing the correlations. Finally, two functions are created to save the heatmap to a image file, and the correlation matrix to a .csv file through Pandas. 

Note: Correlation coefficients can be calculated in multiple ways, using NumPy, SciPy, or Pandas (source: [Real Python](https://realpython.com/numpy-scipy-pandas-correlation-python/#heatmaps-of-correlation-matrices)).


**About the heatmap**

**Pearson's correlation coefficient** is a number between -1 and 1 that measures the linear correlation between two sets of data (source: [wikipedia](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient)). In other words, it tells the strength and direction of the relationship between two variables, which means that it reflects how similar the measurements of two variables are across a dataset (source: [scribbr.com](https://www.scribbr.com/statistics/correlation-coefficient/#:~:text=A%20correlation%20coefficient%20is%20a,variables%20are%20across%20a%20dataset)). In particular:

- a correlation between 0 and 1, is a positive correlation. This means that y values increase, when x values increase. A correlation of 1 is a perfect positive linear relationship.
- a correlation of 0 means that there is no correlation between the features. 
- a correlation between 0 and -1 is a negative correlation. It means that when x values increase, y values decrease. A correlation of -1 is a perfect negative linear relationship. 

(Source: [Linear Correlation, Real Python](https://realpython.com/numpy-scipy-pandas-correlation-python/#linear-correlation)). 

The heatmap plotted from the correlation matrix shows that: 

- **Sepal length, Petal length and Petal width** have a positive correlation with each other. The scatter plot on Petal length vs Petal width (task 5) had already highlighted a direct and positive correlation between these two features, but the heatmap shows that there is some positive correlation between Sepal length and Petal length/Petal width, as well.
- **Sepal width** is the only feature which has a negative correlation with the other features. It looks like the bigger the petal is, and longer the sepal, the thinner the sepal width is.


### 9. Pairplot: Project conclusions 

module: pairplot.py


**What it does**

This program uses Seaborn to create a pairplot showing the relationship that each feature has with the other features in the dataset. About paiplots: [seaborn.pairplot](https://seaborn.pydata.org/generated/seaborn.pairplot.html). 

**How it works**

The code loads the iris dataset. Then it uses Pandas and Seaborn to plot a pairplot and save it to a png file. 


**About the plot: Project conclusions**

The pairplot includes multiple scatter plots showing the relationship that each feature has with any of the other features. Each row and each column of the plot correspond to a feature. That feature is plotted on the y ax (when in the row) or on the x ax (when in the column), while another feature is plotted on the other ax. Diagonally, where a variable would be plotted with itself, instead of the scatter plot, "a univariate distribution plot is drawn to show the marginal distribution of the data in each column" (source: [seaborn.paiplot](https://seaborn.pydata.org/generated/seaborn.pairplot.html)).

The pairplot seems to confirm many of the trends observed in the analysis: 

- **Feature correlation.** As shown by the heatmap, there seems to be a positive direct correlation beteen Sepal length, Petal length and Petal width. Setosa species are smaller, than dimensions increase for Versicolor and then Virginica species. 
    
    On the other hand, the smaller these features, the higher is Sepal Width. Contrarily to the other features, Setosa species tend to have the highest Sepal width dimensions, while the value is lower for Versicolor and Virginica species.

- **Feature similarity.** Iris Veriscolor and Iris Virginica tend to have more similar features, in some cases with overlapping characteristics, while it is always easier to distinguish Irish Setosa samples.

- **Sepal** seems to be the feature couple with the least degree of correlation -- that is, almost none. Based on one of the two variables, it would not be possible to predict the other. Based on the two variables, it would not be possible to predict with certainty which class a sample belongs to. However, it might be possible to predict if a sample belongs or not to the Setosa species, since that's the only class whose samples can be distinguished from the others.

- **Petal size.** As already pointed out in the analysis, between Petal length and Petal width there is such a correlation that, based on these variables, it would be possible to predict which species a sample belongs to, or to predict the value of a dependent variable from an independent variable. 

**Other possible investigations**

This analysis focused on the relationship between features, with little consideration to classes. However, it would be interesting to continue the analysis investigating the following points: 

- Plot boxplots to show class variation for each feature (as [here](https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/)).
- Plot violin plots to further verify distribution (as [here](https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda)).
- Describing the dataset  using Pandas (*describe* method) (as [here](https://www.angela1c.com/projects/iris_project/investigating-the-iris-dataset/)). 

## VI. Wins and challenges of this project

I decided to create the analysis of the dataset as a Python program so that I could practice what I had been learning during the course. When I started, my (probably too ambitious) plan was to create a small but mighty architecture to showcase my skills. I planned to have different custom modules to analyze and plot data. The reasons behind my choice are: 
- improve the readability of my code -- having smaller modules instead of one long script. 
- make it easier to find errors and fix them, when running the code.
- have a more complex but also agile code.

I still believe that developing smaller modules has helped me achive the first two points, so that counts as a win. 

However, the more I was working on the project, the more I realized that my code was not complex enough, and not agile at all. It is quite repetitive instead. I am sure that my code could be much more efficient, had I spent more time experimenting with the architecture (or just using Jupyter Notebook and one long file). I think this is a limitation of my project, but also a challenge for the projects that will come. 

Thank you, 

Irene Celebrin 




## IV. References 

About the dataset 

https://en.wikipedia.org/wiki/Iris_flower_data_set 

https://en.wikipedia.org/wiki/Linear_discriminant_analysis 

http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html

https://www.kaggle.com/code/lalitharajesh/iris-dataset-exploratory-data-analysis

https://www.kaggle.com/datasets/uciml/iris/data

https://www.kaggle.com/code/mrdheer/beginner-s-guide-to-iris-dataset/code

Read_dataset 

https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html 

https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html#sphx-glr-auto-examples-decomposition-plot-pca-iris-py 

https://archive.ics.uci.edu/dataset/53/iris 

https://www.kaggle.com/code/kostasmar/exploring-the-iris-data-set-scikit-learn

https://www.geeksforgeeks.org/How-to-convert-sklearn-dataset-to-pandas-dataframe-in-python/ 

Summary 

https://numpy.org/doc/stable/reference/generated/numpy.size.html

https://numpy.org/doc/stable/reference/generated/numpy.unique.html

https://numpy.org/doc/stable/reference/generated/numpy.min.html

https://numpy.org/doc/stable/reference/generated/numpy.max.html

https://numpy.org/doc/stable/reference/generated/numpy.mean.html

https://numpy.org/doc/stable/reference/generated/numpy.std.html

https://numpy.org/doc/stable/reference/generated/numpy.median.html

https://numpy.org/doc/stable/reference/generated/numpy.quantile.html

https://en.wikipedia.org/wiki/Arithmetic_mean

https://en.wikipedia.org/wiki/Median

https://en.wikipedia.org/wiki/Standard_deviation

https://en.wikipedia.org/wiki/Quartile

https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/


Histograms 

https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html

https://medium.com/@The_Gambitier/matplotlib-essentials-e376ed954201 

https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/


Boxplots 

https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.boxplot.html

Scatter

https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.scatter.html

https://www.geeksforgeeks.org/scatter-plot/

https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda 



Linear Regression 

https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html

https://www.w3schools.com/datascience/ds_linear_slope.asp

https://www.kaggle.com/discussions/questions-and-answers/62086

https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html

https://www.kaggle.com/discussions/questions-and-answers/62086



Heatmap 

https://matplotlib.org/stable/gallery/images_contours_and_fields/image_annotated_heatmap.html#sphx-glr-gallery-images-contours-and-fields-image-annotated-heatmap-py

https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html 

https://realpython.com/numpy-scipy-pandas-correlation-python/#heatmaps-of-correlation-matrices

https://en.wikipedia.org/wiki/Pearson_correlation_coefficient

https://www.scribbr.com/statistics/correlation-coefficient/#:~:text=A%20correlation%20coefficient%20is%20a,variables%20are%20across%20a%20dataset

https://realpython.com/numpy-scipy-pandas-correlation-python/#linear-correlation

Pairplot 

https://seaborn.pydata.org/generated/seaborn.pairplot.html

https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/

https://medium.com/analytics-vidhya/exploratory-data-analysis-iris-dataset-4df6f045cda

https://www.angela1c.com/projects/iris_project/investigating-the-iris-dataset/


Previous analyses

https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_iris.html 

https://scikit-learn.org/1.4/auto_examples/datasets/plot_iris_dataset.html 

https://www.kaggle.com/code/mrdheer/beginner-s-guide-to-iris-dataset/code 

https://eminebozkus.medium.com/exploring-the-iris-flower-dataset-4e000bcc266c

http://www.lac.inpe.br/~rafael.santos/Docs/CAP394/WholeStory-Iris.html

https://www.geeksforgeeks.org/exploratory-data-analysis-on-iris-dataset/

https://medium.com/analytics-vidhya/linear-regression-using-iris-dataset-hello-world-of-machine-learning-b0feecac9cc1 

https://medium.com/@nirajan.acharya777/exploratory-data-analysis-of-iris-dataset-9c0df76771df







