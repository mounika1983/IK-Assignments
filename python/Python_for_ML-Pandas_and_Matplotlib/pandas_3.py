
# Filtering

import pandas as pd

people = {
    "first": ["Matt", 'Jane', 'John'],
    "last": ["Matt2", 'Doe', 'Doe'],
    "email": ["matt@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}


df = pd.DataFrame(people)

# filt = (df['last'] == 'Matt2') | (df['first'] == 'John')

filter1 = df['last'] == 'Doe'

print(type(filter1))

print(df[filter1])

print(df[filter1]['email'])

filter2 = (df['last'] == 'Doe') & (df['first'] == 'John')  # |

print(df[filter2])


df = pd.read_csv('survey_results_public.csv')

filter3 = df['Employment']=='Employed, full-time'

# print(filter3)

print("=========")

print(df[filter3].head().to_string())



filter4 = df['Gender']=='Woman'

print(df[filter4].head().to_string())

print(df[filter4]['Country'].head().to_string())

print(print(df[filter4]['Gender'].head().to_string()))

filter5 = df['LanguageHaveWorkedWith'].str.contains('Python', na=False)

print(df[filter5]['LanguageHaveWorkedWith'].head().to_string())

countries = ["Croatia", "Australia", "Norway"]

filter6 = df['Country'].isin(countries)

print(df[filter6])

# filter2 = df['LanguageWorkedWith'].str.contains('Python', na=False)
