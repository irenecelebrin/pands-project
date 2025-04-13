# Read dataset 
# Explore the iris dataset. Print the properties of the dataset in the console.  

# Import libraries 
from sklearn.datasets import load_iris
import pandas as pd 

def read(): 

    # Load the iris dataset from sklearn
    # Source: https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
    iris = load_iris(as_frame=True)

    print('About this dataset:\n')

    # Display the shape of the dataset. 
    print("Shape of the dataset:\t", iris.frame.shape)

    # Display feature names and target names 
    print("Feature names:\t\t", iris.feature_names)
    print("Target names:\t\t", iris.target_names)

    # Load the iris dataset into a pandas dataframe to preview the data in a tabular format 
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    # Add the target column to the dataframe
    df['target'] = iris.target
    # Display the first 5 rows of the dataset. 
    print(f'The data looks like this:\n{df.head(5)}')

    # Print the keys of the dataset 
    print('Moreover, the datase contains the following information (keys):\n', iris.keys())

    # Explore any of the keys of the dataset. 
    # Loop to ask the user to input a key to explore, until user enters blank value. 
    your_key = input('Please enter the key you would like to explore (blank to exit):\n')
    while your_key != '':
        if your_key in iris.keys():
            print(f'{your_key}: {iris[your_key]}:\n')
            your_key = input(f'Would you like to explore another key? (blank to exit):\n')      
        else: 
            your_key = input('Please enter a valid key from the dataset:\n')


if __name__ == '__main__':
    read()
