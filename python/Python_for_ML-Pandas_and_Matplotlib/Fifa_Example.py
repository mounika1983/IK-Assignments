import matplotlib.pyplot as plt
import pandas as pd

fifa = pd.read_csv('fifa_data.csv')

print(fifa.head(5)['Preferred Foot'].to_string())

left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()

print(left)
print(right)

left = left[0]
right = right[0]

plt.figure(figsize=(8,5))

labels = ['Left', 'Right']
colors = ['red', 'green']

plt.pie([left, right], labels = labels, colors=colors)

plt.title('Foot Preference of FIFA Players')

plt.show()