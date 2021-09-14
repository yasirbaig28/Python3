#Accseing any column from the csv file
import pandas as pd

data = pd.read_csv("diabetes.csv")
data1=data.iloc[::,-1]
print(data1)
