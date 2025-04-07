# Explore the iris dataset 

# import libraries 
from sklearn.datasets import load_iris
import pandas as pd 



# Import the iris dataset from sklearn
# source: https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
iris = load_iris(as_frame=True)

# Load the iris dataset into a pandas dataframe to visualize it
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
# Add the target column to the dataframe
df['target'] = iris.target
# Display the first 5 rows of the dataset. Uncomment the next line to see the output 
#print(df.head(5))

# Display the shape of the dataset. Uncomment the next line to see the output
print("Shape of the dataset:\t", iris.frame.shape)

# Display feature names and target names 
print("Feature names:\t\t", iris.feature_names)
print("Target names:\t\t", iris.target_names)

# Load the iris dataset into a pandas dataframe to preview the data 
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
# Add the target column to the dataframe
df['target'] = iris.target
#Display the first 5 rows of the dataset. Uncomment the next line to see the output 
print(f'The data looks like this:\n{df.head(5)}')

# Print the keys of the dataset 
print('Moreover, the datase contains the following information (keys):\n', iris.keys())

