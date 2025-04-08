from sklearn.datasets import load_iris
import pandas as pd 

iris = load_iris(as_frame=True) 

print(iris.feature_names[0])
