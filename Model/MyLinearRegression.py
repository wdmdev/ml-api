import os
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
 
 
df = pd.read_csv(os.path.join('..', 'Data', 'hcoe_met_combined.csv'), sep=';')
df.drop('DateTime', axis=1, inplace=True)
X = df.iloc[:,:-1]
y = df.iloc[:,-1]

print(f'Saving Logistic Regression model to pickle format...')
pickle.dump(model, open('logistic_regression.pkl', 'wb'))
print(f'Save complete')