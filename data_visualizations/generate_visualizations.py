import pandas as pd
import matplotlib.pyplot as plt


def generate_graph(file_name, column_name, x_label, y_label, title, figure_name, rows,index_col='Unnamed: 0'):
    academic_scores_for_sports = pd.read_csv(file_name,index_col='Unnamed: 0')
    graph = academic_scores_for_sports[rows].sort(ascending=True, columns=rows[0]).plot(kind='bar',
                                                                                        width=0.79, figsize=(25, 20),
                                                                                        linewidth=5)
    graph.set_title(title)
    graph.set_xlabel(x_label, fontsize=18)
    graph.set_ylabel(y_label, fontsize=18)
    # Shrink current axis by 20%
    box = graph.get_position()
    graph.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    # Put a legend to the right of the current axis
    graph.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig(figure_name)
    print(academic_scores_for_sports[rows].max())



if __name__ == '__main__':
    cumulative_academic_scores_rows = [str(2004 + i) + '_CUMULATIVE_SCORE' for i in range(6, 11)]
    average_academic_scores_rows = [str(2004 + i) + '_AVERAGE_SCORE' for i in range(6, 11)]
    generate_graph('data_sets/Cumulative_Academic_Score_By_Sport.csv',
                   '2014_CUMULATIVE_SCORE',
                   "Sports",
                   "Cumulative Academic Scores",
                   "Sports With the Highest Academic Scores",
                   "data_visualizations/Cumulative_Academic_Scores_By_Sport.png",
                   cumulative_academic_scores_rows
                   )
    generate_graph('data_sets/Average_Academic_Score_By_Sport.csv',
                   '2004_AVERAGE_SCORE',
                   'Sports',
                   'Cumulative Academic Scores',
                   'Average Academic Score For Sport',
                   'data_visualizations/Average_Academic_Score_By_Sport.png',
                    average_academic_scores_rows
                   )
