import pandas as pd


'''
Creating data
There are two core objects in pandas: the DataFrame and the Series.

DataFrame
A DataFrame is a table. 
It contains an array of individual entries, 
each of which has a certain value.
Each entry corresponds to a row (or record) and a column.


Series
A Series, by contrast, is a sequence of data values. 
If a DataFrame is a table, a Series is a list. 
And in fact you can create one with nothing more than a list:

'''



df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
              'Sue': ['Pretty good.', 'Bland.']}
             )

print(df)
'''
df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

'''


#print(df)

se = pd.Series([1, 2, 3, 4, 5])

#print(se)

se2 = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

#print(se2)

df = pd.read_csv('survey_results_public.csv') # DataFrame

print(type(df))

print(df.head().to_string()) # 5 rows

print(df.head(10).to_string())

print(df)

# print(df.head())

# print(df.head().to_string())

# print(df.tail(10))

print(df.shape)

print(df.info())

print("============")

print((df.loc[2:5]))
print("============")

print(df.iloc[2:5])


df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])

print(df)

print(df.iloc[0])

print(df.loc['Product A'])
