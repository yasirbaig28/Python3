#Accseing any row from the csv file
import pandas as pd

data = pd.read_csv('diabetes.csv')
data1=data.iloc[0]
print(data1)
