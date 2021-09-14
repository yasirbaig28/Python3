import pandas as pd

data = pd.read_csv('D:/6th ECE/PAP/Dataset Example/Latest Covid-19 India Status.csv')

count = 0

for i in data['Total Cases']:
    if(i>=2000000):
        count+=1
print(count)
print("Covid Cases are high")
