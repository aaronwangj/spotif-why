import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(
    '../../Code/regression/data/clean.csv', index_col=0)
# print(df.shape)
# df.drop_duplicates(subset=['id'], inplace=True)
print(df.columns)
df.drop(['Unnamed: 0.1', 'Track Name', 'Artist',
         'id', 'explicit'], axis=1, inplace=True)
df['popularity'] = df.pop('popularity')
# print(df.shape)
# print(df.head())
triangle = np.triu(np.ones_like(df.corr()))

plt.figure(figsize=(9, 7))
ax = sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap='BrBG', mask=triangle)
ax.set_xticklabels(
    ax.get_xticklabels(),
    rotation=45,
    horizontalalignment='right'
)
ax.set_title("Correlation Heatmap")
ax.figure.tight_layout()
plt.savefig('features_heatmap.png')
plt.show()
