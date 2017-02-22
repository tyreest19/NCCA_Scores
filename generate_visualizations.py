import pandas as pd
import seaborn as sns

scores_and_schools_dataframe = pd.read_csv('scores_by_schools_and_teams.csv')
sns.countplot(x='SCHOOL_NAME', data=scores_and_schools_dataframe)
sns.plt.show()