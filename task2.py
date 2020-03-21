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

# Побудуйте heatmap кореляційної матриці. Матриця формується
# засобами Pandas, зі стандартним значенням параметрів.
#
# sns.heatmap(data=df.corr())
# plt.show()
#
# Визначте які дві ознаки найбільше корелюють (за Пірсоном) з
# ознакою height?
#
# gender and weight

# Побудуйте violinplot для росту і статі. Використовуйте:
#  hue - для розбивки за статтю;
#  scale - для оцінки кількості кожної статі.
# Для коректного відтворення, перетворіть DataFrame в «Long Format»-
# представлення за допомогою функції melt в pandas.
#
# long_format = pd.melt(df, id_vars='height', value_vars='gender')
# sns.violinplot(data=long_format, x='height', hue='height', scale='count')
# plt.show()

# Побудуйте violinplot для статі, росту і вагі.
#
# dfHeightWeightByGender = df[['height', 'weight']]
# sns.violinplot(data=dfHeightWeightByGender, scale='count')
# plt.show()

# Побудуйте на одному графіку два окремих kdeplot росту і вагі, окремо
# для чоловіків і жінок. На ньому різниця буде більш наочною, але не можна
# буде оцінити кількість чоловіків / жінок.
# dfMale = df[df['gender'] == 2][['height', 'weight']]
# dfFemale = df[df['gender'] == 1][['height', 'weight']]
# # sns.kdeplot(data=dfMale['height'])
# # sns.kdeplot(data=dfFemale['height'])
# # sns.kdeplot(data=dfMale['weight'])
# # sns.kdeplot(data=dfFemale['weight'])
# sns.kdeplot(data=dfMale, cmap='Reds')
# sns.kdeplot(data=dfFemale, cmap='Blues')
# plt.show()

# Побудуйте кореляційну матрицю, використовуючи коефіцієнт
# Спірмена.
#
# data = df.corr(method='spearman')
# print(data)
# sns.heatmap(data=data)
# plt.title('Spearman')
# plt.show()
#
# 3.1 Які ознаки тепер найбільше корелюють одна з одною за
# Спірменом?
#
# ap_hi and ap_lo
#
# 3.2 Чому значення рангової кореляції у цих ознаках таке велике
# (відносно)?
#
# При зростанні мінімального тиску найчастіше зростає і максимальний

# Побудуйте спільний графік розподілу jointplot двох ознак, що найбільш
# корелюють між собою за Спирменом.
#
# dfInternalPressure = df[(df['ap_lo'] > 0) & (df['ap_hi'] > 0)][['ap_lo', 'ap_hi']].apply(np.log1p)
# g = sns.jointplot(x='ap_lo',
#                   y='ap_hi',
#                   size=10,
#                   data=dfInternalPressure)
#
# # Сітка
# g.ax_joint.grid(True)
#
# # Перетворимо логарифмічні значення на шкалах в реальні
#
# g.ax_joint.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, pos: str(round(int(np.exp(x))))))
# g.ax_joint.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, pos: str(round(int(np.exp(x))))))
# plt.show()
#
# Скільки чітко виражених кластерів вийшло на спільному
# графіку обраних ознак, за логарифмічною шкалою? Під кластером іноді
# розуміють щільне скупчення точок, в околиці яких досить мало
# одиночних і які візуально відділені від інших кластерів
#
# вийшло 6

# # 5. Вік
# # Порахуємо, скільки повних років було респондентам на момент їх
# # занесення в базу.
#
# df['age_years'] = (df['age'] // 365.25).astype(int)
#
# # Побудуйте Countplot, де на осі абсцис буде відзначений вік, на осі
# # ординат - кількість. Кожне значення віку повинне мати два стовпці, що
# # відповідають кількості осіб кожного класу cardio (здоровий / хворий)
# # даного віку.
#
# sns.countplot(x='age_years', hue='cardio', data=df)
# plt.show()
#
# # В якому віці кількість пацієнтів з ССЗ вперше стає більше,
# # ніж здорових?
#
# # в 53 роки
