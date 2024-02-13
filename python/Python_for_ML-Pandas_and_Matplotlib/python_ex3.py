'''

Indexing, Selecting & Assigning

'''
import pandas as pd

survey = pd.read_csv('survey_results_public.csv')

print(survey['Employment'].head(10))

print(survey['Employment'][1:4])

# Index-based selection

print(survey.iloc[2])

# print(survey.iloc[:, 3])

print(survey.iloc[:5, 3])

# Label-based selection

print(survey.loc[2, 'Country'])


print(survey.loc[:5, ['Employment', 'Country']])

print("Survey data")

print(survey.isnull().sum())

'''This operation will delete any row with at least a single null value,
 but it will return a new DataFrame without altering the original one. 
 You could specify inplace=True in this method as well.

'''

print(survey.dropna())

####### Summary functions

gas_price = pd.read_csv('gas_prices.csv')

print("Info of gas_price")
print(gas_price.info())

print(gas_price['Germany'])

print(gas_price['Germany'].describe())

print(gas_price['Germany'].mean())


print(gas_price.rename(columns={'Germany': 'Germany4'}).to_string())
