import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import  matplotlib.ticker

# ігноруємо warnings
import warnings
warnings.filterwarnings("ignore")

sns.set_context(
    "notebook",
    font_scale=1.5,
    rc={
        "figure.figsize": (12, 9),
        "axes.titlesize": 18
    }
)

df = pd.read_csv('mlbootcamp5_train.csv', sep=';', index_col='id')

# print(df.head()); print(); # вивести перші 5 записів

# df_uniques = pd.melt(frame=df, value_vars=['gender', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio'])
# df_uniques = pd.DataFrame(df_uniques.groupby(['variable', 'value'])['value'].count()) \
#     .sort_index(level=[0, 1]) \
#     .rename(columns={'value': 'count'}) \
#     .reset_index()
#
# sns.factorplot(x='variable', y='count', hue='value', data=df_uniques, kind='bar', size=12)
# plt.show()

# df_uniques = pd.melt(frame=df, value_vars=['gender', 'cholesterol', 'gluc', 'smoke', 'alco', 'active'],
#                      id_vars=['cardio'])
# df_uniques = pd.DataFrame(df_uniques.groupby(['variable', 'value', 'cardio'])['value'].count()) \
#     .sort_index(level=[0, 1]) \
#     .rename(columns={'value': 'count'}) \
#     .reset_index()
#
# sns.factorplot(x='variable', y='count', hue='value', col='cardio', data=df_uniques, kind='bar', size=9)
# plt.show()

for c in df.columns:
    n = df[c].nunique()
    print(c)
    if n <= 3:
        # print count of every element's value in column
        print(n, sorted(df[c].value_counts().to_dict().items()))
    else:
        print(n)
print(10 * '-')
