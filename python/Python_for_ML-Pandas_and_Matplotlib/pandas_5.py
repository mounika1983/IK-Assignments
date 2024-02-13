
# Grouping and Aggregating - Analyzing and Exploring the Data

import pandas as pd

people = {
    "first": ["Matt", 'Jane', 'John'],
    "last": ["Matt2", 'Doe', 'Doe'],
    "email": ["matt@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}


df1 = pd.DataFrame(people)

df2 = pd.read_csv('survey_results_public.csv')

# print(df2.sort_values(by=['Country']).head(10)['Country'])

titanic_df = pd.read_csv('titanic.csv')

print(titanic_df['sex'].value_counts())

print(df2['Gender'].value_counts())

print("=========")

print(df2['WebframeWantToWorkWith'].value_counts())

# print(df2['WebframeWantToWorkWith'].value_counts(normalize=True))

print("==================")

filt = df2['Country'] == 'India'
print(df2.loc[filt]['OpSysProfessional use'].value_counts())

print("==================")

print(df2['Country'].value_counts())

print("==================")

country_grp = df2.groupby(['Country'])
print(country_grp.get_group('India'))

print("==================")

filt = df2['Country'] == 'India'
print(df2.loc[filt]['OpSysProfessional use'].value_counts())

# Developers in India, who know Python

print("================== Python Developers from india ")
filt = df2['Country'] == 'India'
print(df2.loc[filt]['LanguageHaveWorkedWith'].str.contains('Python').sum())

print("==================")

print(country_grp['LanguageHaveWorkedWith'].apply(lambda x: x.str.contains('Python').sum()))

