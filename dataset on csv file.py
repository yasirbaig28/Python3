#Reading any csv file and accessing any row or column
import pandas as pd

data = pd.read_csv('diabetes.csv')

print(data['Age'])
print(data.iloc[3:300])
