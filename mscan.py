import pandas as pd 

data = pd.read_csv('mushrooms.csv')

missing_stalk_root = data['stalk-root'] == '?'
print('Number of missing values:', missing_stalk_root.sum())

most_common_value = data.loc[data['stalk-root'] != '?', 'stalk-root'].mode()[0]
print('Most common value in stalk root:', most_common_value)
# most common value is b = bulbous

data['stalk-root'] = data['stalk-root'].replace('?', most_common_value)
print(data['stalk-root'].value_counts())



