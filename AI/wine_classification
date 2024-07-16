from ucimlrepo import fetch_ucirepo 
import pandas as pd
  
# fetch dataset 
wine = fetch_ucirepo(id=109) 
  
# data (as pandas dataframes) 
X = wine.data.features 
y = wine.data.targets 
  
# metadata 
# print(wine.metadata) 
  
# variable information 
# print(wine.variables) 

df = pd.concat([X, y], axis = 1)

print(df.info())
print(df.describe())
print(df.head())
print(df.iloc[:, -1].value_counts)
