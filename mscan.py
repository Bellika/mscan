import pandas as pd 
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('mushrooms.csv')


# fixing missing value (now changing with most common, maybe remove column?)
missing_stalk_root = data['stalk-root'] == '?'
print('Number of missing values:', missing_stalk_root.sum())

most_common_value = data.loc[data['stalk-root'] != '?', 'stalk-root'].mode()[0]
print('Most common value in stalk root:', most_common_value)
# most common value is b = bulbous

data['stalk-root'] = data['stalk-root'].replace('?', most_common_value)
print(data['stalk-root'].value_counts())


# transform strig values to numerical values
label_encoders = {}
for column in data.columns:
  le = LabelEncoder()
  data[column] = le.fit_transform(data[column])

  label_encoders[column] = le

print(f'\nTransformed data:\n {data.head}')


