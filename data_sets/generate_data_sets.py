import pandas as pd
import matplotlib.pyplot as plt

data_set = pd.read_csv('data_sets/scores_by_schools_and_teams.csv')

def create_data_set_of_cumulative_sport_scores():
    sports_index = data_set['SPORT_NAME'].unique()
    scores_column = ['2004_CUMULATIVE_SCORE', '2005_CUMULATIVE_SCORE', '2006_CUMULATIVE_SCORE', '2007_CUMULATIVE_SCORE',
                     '2008_CUMULATIVE_SCORE', '2009_CUMULATIVE_SCORE', '2010_CUMULATIVE_SCORE', '2011_CUMULATIVE_SCORE',
                     '2012_CUMULATIVE_SCORE', '2013_CUMULATIVE_SCORE', '2014_CUMULATIVE_SCORE']
    scores_column.reverse()
    acdemic_scores_by_sport = pd.DataFrame(0, index=sports_index, columns=scores_column)
    for unique_id, rows in data_set.iterrows():
        for i in range(11):
            yearly_score = str(2004 + i) + '_SCORE'
            cumalitive_score = str(2004 + i) + '_CUMULATIVE_SCORE'
            index = data_set.iloc[unique_id]['SPORT_NAME']
            row = data_set.iloc[unique_id][yearly_score]
            acdemic_scores_by_sport.loc[index][cumalitive_score] += row
    acdemic_scores_by_sport.to_csv('data_sets/Cumulative_Academic_Score_By_Sport.csv')

def create_data_set_of_average_sport_scores():
    amount_of_sport_teams = dict(data_set['SPORT_NAME'].value_counts())
    average_scores_column = ['2004_AVERAGE_SCORE', '2005_AVERAGE_SCORE', '2006_AVERAGE_SCORE', '2007_AVERAGE_SCORE',
                     '2008_AVERAGE_SCORE', '2009_AVERAGE_SCORE', '2010_AVERAGE_SCORE', '2011_AVERAGE_SCORE',
                     '2012_AVERAGE_SCORE', '2013_AVERAGE_SCORE', '2014_AVERAGE_SCORE']
    cumulative_academic_scores_data_set = pd.read_csv('data_sets/Cumulative_Academic_Score_By_Sport.csv',
                                                      index_col='Unnamed: 0')
    average_academic_scores_data_set = pd.DataFrame(index=amount_of_sport_teams.keys(), columns=average_scores_column)
    for i in range(11):
        cumulative_score_year = str(2004 + i) + '_CUMULATIVE_SCORE'
        average_score_year = str(2004 + i) + '_AVERAGE_SCORE'
        average_academic_scores_data_set[average_score_year] = cumulative_academic_scores_data_set[cumulative_score_year].mean()
    for sports in amount_of_sport_teams:
            for i in range(11):
                cumulative_score = cumulative_academic_scores_data_set.loc[sports][str(2004 + i) + '_CUMULATIVE_SCORE']
                average_academic_scores_data_set.loc[sports][str(2004 + i) + '_AVERAGE_SCORE'] = cumulative_score
                average_academic_scores_data_set.loc[sports][str(2004 + i) + '_AVERAGE_SCORE'] \
                    /= amount_of_sport_teams[sports]
    average_academic_scores_data_set.to_csv('data_sets/Average_Academic_Score_By_Sport.csv')

def create_data_set_of_cumulative_school_scores():
    orginal_data_set = data_set
    del orginal_data_set['SCHOOL_ID']
    orginal_data_set = orginal_data_set.set_index('SCHOOL_NAME')
    list_of_school_names = orginal_data_set.index.unique().tolist()
    list_of_columns = [str(2004 + i) + '_AVERAGE_SCORE' for i in range(11)]
    cumulative_score_for_schools = pd.DataFrame(index=list_of_school_names, columns=list_of_columns)
    for school in list_of_school_names:
        for i in range(11):
            average_score = orginal_data_set.loc[school][str(2004 + i) + '_SCORE'].tolist()
            if type(average_score) == list:
                average_score = sum(average_score)
                cumulative_score_for_schools.loc[school][str(2004 + i) + '_AVERAGE_SCORE'] = average_score
            else:
                cumulative_score_for_schools.loc[school][str(2004 + i) + '_AVERAGE_SCORE'] = average_score
    cumulative_score_for_schools.to_csv('data_sets/Cumulative_Academic_Score_By_School.csv')


if __name__ == '__main__':
    #create_data_set_of_cumulative_sport_scores()
    create_data_set_of_average_sport_scores()
    #create_data_set_of_cumulative_school_scores()