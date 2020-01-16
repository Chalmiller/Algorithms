def tennisSet(score1, score2):
    tennis_scores = [score1, score2]
    max_score = 7
    min_score = 6
    max_of_set = max(tennis_scores)
    min_of_set = min(tennis_scores)

    if max_of_set > max_score or max_of_set < min_score or score1 == score2:
        return False
    elif max_of_set == max_score:
        if min_of_set < 5:
            return False
        else:
            return True
    elif max_of_set == min_score:
        if min_of_set < 5:
            return True
        else:
            return False
