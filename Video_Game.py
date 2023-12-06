import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import statsmodels.graphics.api as smg

df = pd.read_csv('video_games.csv')
#print(df.describe())

# categories = (df['Features.Max Players'])
# values =(df['Metrics.Review Score'])
# plt.bar(categories, values)
# plt.xlabel('Number of Players')
# plt.ylabel('Rating')
# plt.title('Bar Chart')
# plt.show()

#categories = (df['Features.Max Players'])
# values =(df['Metrics.Review Score'])
# plt.scatter(categories, values)
# plt.xlabel('Number of Players')
# plt.ylabel('Rating')
# plt.title('Scatter Chart')
# plt.show()

# filter_query = "'Features.Max Players' == '1' or 'Features.Max Players' == '2'"
# players_df = df.query(filter_query)
# players_df.boxplot(column= "Metrics.Review Score", by="Features.Max Players")
# plt.show()

# df_num = df.select_dtypes(['number'])
# game_corr_matrix = np.corrcoef(df_num.T)
# selected_colums = ['Metrics.Review Score','Metrics.Sales','Features.Max Players','Metrics.Used Price','Length.All PlayStyles.Average','Length.Completionists.Average']
# corr_matrix = df[selected_colums].corr(numeric_only=True).round(2) 
# sns.heatmap(corr_matrix, annot=True, vmax=1, vmin=-1, cmap='coolwarm')
# plt.show()

categories = (df['Features.Online?'])
values =(df['Length.All PlayStyles.Average'])
plt.bar(categories, values)
plt.xlabel('Online T or F')
plt.ylabel('Length')
plt.title('Bar Chart')
plt.show()

categories = (df['Features.Online?'])
values =(df['Length.All PlayStyles.Average'])
plt.scatter(categories, values)
plt.xlabel('Online T or F')
plt.ylabel('Length')
plt.title('Scatter Chart')
plt.show()