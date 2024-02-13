
# Sorting

import pandas as pd

people = {
    "first": ["Matt", 'Jane', 'John'],
    "last": ["Matt2", 'Doe', 'Doe'],
    "email": ["matt@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}


df = pd.DataFrame(people)

print(df.sort_values(by='last'))

# df.sort_values(by='last', ascending=False)

df.sort_values(by=['last', 'first'], ascending=False)

# df['last'].sort_values()

df = pd.read_csv('survey_results_public.csv')

print(df.sort_values(by=['Country']).head(10)['Country'])

df2 = pd.read_csv('titanic.csv')

# print(df2.sort_values(by='age').head(10)['name'], 'age'])

print(df2.sort_values(by='age').head(10)[['name', 'age']])
