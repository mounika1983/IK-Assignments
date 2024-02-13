import pandas as pd
import numpy as np

data = {
    'Column1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Column2': ['A', 'B', None, 'A', 'NA', 'C', 'A', 'B', 'C', 'A'],
    'Column3': [None, np.nan, 150, 120, np.nan, 180, 130, 220, np.nan, 140]
}
df = pd.DataFrame(data)

print(df)

print(type[df.iloc[2][1]])

# Handling missing data
missing_data = df.isnull()

print(missing_data)

not_missing_data = df.notnull()

df_filled = df.fillna(0)
df_dropped_rows = df.dropna(axis=0)
df_dropped_columns = df.dropna(axis=1)

# Data type conversion
df['Column1'] = df['Column1'].astype(int)

# Renaming columns and indexes
df.rename(columns={'Column1': 'NewName1', 'Column2': 'NewName2'}, inplace=True)
df.rename(index={0: 'Row1', 1: 'Row2'}, inplace=True)

# Replacing values
df['NewName2'].replace('A', 'X', inplace=True)

print(df)
