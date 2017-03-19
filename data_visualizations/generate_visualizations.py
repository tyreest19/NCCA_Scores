import pandas as pd
import matplotlib.pyplot as plt


def generate_graph(file_name, column_name, x_label, y_label, title, figure_name, index_col='Unnamed: 0'):
    academic_scores_for_sports = pd.read_csv(file_name,index_col='Unnamed: 0')
    graph = academic_scores_for_sports.sort(columns=column_name, ascending=True).plot(kind='bar',
                                                                                      width=0.8, figsize=(15, 20),
                                                                                      linewidth=5)
    graph.set_title(title)
    graph.set_xlabel(x_label)
    graph.set_ylabel(y_label)
    # Shrink current axis by 20%
    box = graph.get_position()
    graph.set_position([box.x0, box.y0, box.width * 0.8, box.height])
    # Put a legend to the right of the current axis
    graph.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.savefig(figure_name)



if __name__ == '__main__':
    generate_graph('data_sets/Cumulative_Academic_Score_By_Sport.csv',
                   '2014_CUMULATIVE_SCORE',
                   "Sports",
                   "Cumulative Academic Scores",
                   "Sports With the Highest Academic Scores",
                   "data_visualizations/Cumulative_Academic_Scores_By_Sport.pdf"
                  )
    generate_graph('data_sets/Average_Academic_Score_By_Sport.csv',
                   '2014_AVERAGE_SCORE',
                   'Sports',
                   'Cumulative Academic Scores',
                   'Average Academic Score For Sport',
                   'data_visualizations/Average_Academic_Score_By_Sport.pdf'
                   )
