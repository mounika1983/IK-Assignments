import pandas as pd

# df = pd.read_csv('survey_results_public.csv') # DataFrame

person = {
    "first": "Matt",
    "last": "Matt2",
    "email": "matt@gmail.com"
}

people = {
    "first": ["Matt", 'Jane', 'John'],
    "last": ["Matt2", 'Doe', 'Doe'],
    "email": ["matt@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}

print(people['email'])

person_df = pd.DataFrame(people)

print(person_df)

print(person_df['email'])

print(person_df.email)

print(type(person_df['email']))

print(person_df[['last', 'email']])

# print(person_df.loc[0])

print(person_df.columns)

print(person_df.iloc[0, 1])

print(person_df.iloc[[0, 1], 1])


print(person_df.loc[[0, 1], ['email', 'last']])

# df.iloc[[0, 1], 2]

df = pd.read_csv('survey_results_public.csv')

print(df['Country'].count())
