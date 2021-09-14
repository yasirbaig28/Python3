#Accseing any column from the csv file
import pandas as pd

data = pd.read_csv('diabetes.csv')
mylist=['Glucose','Insulin','BMI']
data2=data[mylist]
print(data2)
