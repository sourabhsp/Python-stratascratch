box_scores.head()
box_scores['total_score']=box_scores[['assignment1','assignment2','assignment3']]. sum(axis=1)
box_scores.total_score.max()-box_scores.total_score.min()