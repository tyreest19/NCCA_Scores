import pandas as pd
import matplotlib.pyplot as plt

data_set = pd.read_csv('scores_by_schools_and_teams.csv')

def creates_data_for_sports_and_scores():
    sports_index = data_set['SPORT_NAME'].unique()
    scores_column = ['2004_CUMULATIVE_SCORE', '2005_CUMULATIVE_SCORE', '2006_CUMULATIVE_SCORE', '2007_CUMULATIVE_SCORE',
                     '2008_CUMULATIVE_SCORE', '2009_CUMULATIVE_SCORE','2010_CUMULATIVE_SCORE','2011_CUMULATIVE_SCORE',
                     '2012_CUMULATIVE_SCORE', '2013_CUMULATIVE_SCORE','2014_CUMULATIVE_SCORE']

    scores_column.reverse()
    acdemic_scores_by_sport = pd.DataFrame(index=sports_index, columns=scores_column)
    print(acdemic_scores_by_sport.head())

if __name__ == '__main__':
    creates_data_for_sports_and_scores()
