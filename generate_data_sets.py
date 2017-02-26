import pandas as pd
import matplotlib.pyplot as plt

data_set = pd.read_csv('data_sets/scores_by_schools_and_teams.csv')

def creates_data_for_sports_and_scores():
    sports_index = data_set['SPORT_NAME'].unique()
    scores_column = ['2004_CUMULATIVE_SCORE', '2005_CUMULATIVE_SCORE', '2006_CUMULATIVE_SCORE', '2007_CUMULATIVE_SCORE',
                     '2008_CUMULATIVE_SCORE', '2009_CUMULATIVE_SCORE','2010_CUMULATIVE_SCORE','2011_CUMULATIVE_SCORE',
                     '2012_CUMULATIVE_SCORE', '2013_CUMULATIVE_SCORE','2014_CUMULATIVE_SCORE']

    scores_column.reverse()
    acdemic_scores_by_sport = pd.DataFrame(0, index=sports_index, columns=scores_column)
    for unique_id, rows in data_set.iterrows():
        for i in range(11):
            yearly_score = str(2004 + i) + '_SCORE'
            cumalitive_score = str(2004 + i) + '_CUMULATIVE_SCORE'
            index = data_set.iloc[unique_id]['SPORT_NAME']
            row = data_set.iloc[unique_id][yearly_score]
            acdemic_scores_by_sport.loc[index][cumalitive_score] += row
    acdemic_scores_by_sport.to_csv('data_sets/Cumalitive_Academic_Score.csv')

if __name__ == '__main__':
    creates_data_for_sports_and_scores()
