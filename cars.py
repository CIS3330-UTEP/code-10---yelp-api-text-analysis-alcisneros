import pandas as pd
import seaborn as sns
import statsmodels.formula.api as sm_api
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = pd.read_csv('cars_dataset(1).csv')
print (df['Identification_Make'])

brands = ['Honda', 'Toyota', 'Infiniti']
new_df = df.query('Identification_Make == @brands')

# print(new_df.groupby('Identification_Make')['Identification_Make'].count())
print(new_df.groupby('Identification_Make').describe())
#Correlation
corr = new_df.corr(numeric_only=True)
print(corr)
sns.heatmap(corr)
#ANOVA
model = sm_api.ols('Fuel_Highway_mpg~ C(Identification_Make)', data=df).fit()
anova_table = sm.stats.anova_lm(model, type=1)
print(anova_table)
#BOXPLOTS
new_df.boxplot(column='Fuel_Highway_mpg', by='Identification_Make')
new_df.boxplot(column='Engine_Torque', by='Identification_Make')
plt.show()

