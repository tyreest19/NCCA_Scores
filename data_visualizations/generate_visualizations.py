import pandas as pd
import matplotlib.pyplot as plt


def generate_graph_of_highest_scores_by_sports():
    academic_scores_for_sports = pd.read_csv('data_sets/Cumalitive_Academic_Score.csv',index_col='Unnamed: 0')
    graph = academic_scores_for_sports.sort(columns='2014_CUMULATIVE_SCORE', ascending=True).plot(kind='bar',
                                                                                            width=0.8, figsize=(15, 20))
    graph.set_title("Sports With the Highest Academic Scores")
    graph.set_xlabel("Sports")
    graph.set_ylabel("Cumulative Academic Scores")
    plt.savefig("data_visualizations/Highest_Academic_Scores_By_Sport.pdf")

if __name__ == '__main__':
    generate_graph_of_highest_scores_by_sports()
