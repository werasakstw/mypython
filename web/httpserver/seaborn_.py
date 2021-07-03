# pip install seaborn

import seaborn as sb
df = sb.load_dataset('diamonds')
print(df.shape)
print(df.head())

df.to_csv('diamonds.csv')

