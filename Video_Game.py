import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as sm_api
import statsmodels.graphics.api as smg
import statsmodels.stats.anova as anova

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

# filter_query = "`Features.Max Players` == 1 or `Features.Max Players` == 2 or `Features.Max Players` == 3 or `Features.Max Players` == 4 or `Features.Max Players` == 5 or `Features.Max Players` == 6 or `Features.Max Players` == 7 or `Features.Max Players` == 8"
# players_df = df.query(filter_query)
# players_df.boxplot(column= "Metrics.Review Score", by="Features.Max Players")
# plt.show()

# df_top3 = df.query(`Features.Max Players` == 1 or `Features.Max Players` == 2 or `Features.Max Players` == 3)
# model = sm_api.ols('Metrics.Review Score ~ C(Features.Max Players)', data=df_top3).fit()
# anova_table = sm.stats.anova_lm(model, typ=2)
# print(anova_table)

# df_num = df.select_dtypes(['number'])
# game_corr_matrix = np.corrcoef(df_num.T)
# selected_colums = ['Metrics.Review Score','Metrics.Sales','Features.Max Players','Metrics.Used Price','Length.All PlayStyles.Average','Length.Completionists.Average']
# corr_matrix = df[selected_colums].corr(numeric_only=True).round(2) 
# sns.heatmap(corr_matrix, annot=True, vmax=1, vmin=-1, cmap='coolwarm')
# plt.show()

# categories = (df['Features.Online?'])
# values =(df['Length.All PlayStyles.Average'])
# plt.bar(categories, values)
# plt.xlabel('Online T or F')
# plt.ylabel('Length')
# plt.title('Bar Chart')
# plt.show()

# categories = (df['Features.Online?'])
# values =(df['Length.All PlayStyles.Average'])
# plt.scatter(categories, values)
# plt.xlabel('Online T or F')
# plt.ylabel('Length')
# plt.title('Scatter Chart')
# plt.show()

# categories = (df['Features.Max Players'])
# values =(df['Metrics.Sales'])
# plt.bar(categories, values)
# plt.xlabel('Number of Players')
# plt.ylabel('sales')
# plt.title('Bar Chart')
# plt.show()

# filter_query = "`Features.Max Players` == 1 or `Features.Max Players` == 2 or `Features.Max Players` == 3 or `Features.Max Players` == 4 or `Features.Max Players` == 5 or `Features.Max Players` == 6 or `Features.Max Players` == 7 or `Features.Max Players` == 8"
# players_df = df.query(filter_query)
# players_df.boxplot(column= "Metrics.Used Price", by="Features.Max Players")
# plt.show()