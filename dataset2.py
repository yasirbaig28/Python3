#Reading any csv and getting inside details
import pandas as pd

data = pd.read_csv('diabetes.csv')
count = 0
for i in data['Outcome']:
    if(i==1):
        count = count+1
print(count)
print("No of People Who are Diabetic")
